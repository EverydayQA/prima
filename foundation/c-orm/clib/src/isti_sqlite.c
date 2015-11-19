
#include <stdio.h>
#include <string.h>

#include <sqlite3.h>

#include "isti.h"
#include "isti_flow.h"
#include "isti_str.h"

#include "isti_sqlite.h"

ISTI_STR_AS(str)

/// @file
/// @brief The SQLite database connection (implementation).
///
/// See header for documentation. @see isti_sqlite.h

// The private ADT
typedef struct sqlite {
  sqlite3 *db;
} sqlite;

// Extract the ADT from the public struct.
#define DB3 sqlite3 *db3 = ((sqlite*)db->internal)->db; ASSERT(db3, ISTI_ERR_SQLITE, "Database not opened\n")

// Convert the SQLite error code to one we can work with more easily.
static int unpack(sqlite3 *db, int *readable, int err) {
  if (readable) *readable = err == SQLITE_ROW;
  if (err && err != SQLITE_DONE && err != SQLITE_ROW) {
    ISTI_LOG("sqlite: %s\n", sqlite3_errmsg(db));
    return ISTI_ERR_SQLITE;
  }
  return ISTI_OK;
}

static int close(isti_db *db, int previous) {
  STATUS;
  if (db) {
    if (db->internal) {
      DB3;
      sqlite3_close(db3);
      free(db->internal);
    }
    free(db);
  }
  EXIT_PREVIOUS;
}

static int connect(isti_db *db, const char *path, int timeout) {
  STATUS;
  sqlite3 *db3 = NULL;
  if ((status = unpack(db3, NULL, sqlite3_open(path, &db3)))) {
    sqlite3_close(db3);
  } else {
    ((sqlite*)db->internal)->db = db3;
    if (timeout) {
      CHECK(unpack(db3, NULL, sqlite3_busy_timeout(db3, timeout)));
    }
  }
  EXIT_STATUS;
}

static int single_stmt(sqlite3 *db3, sqlite3_stmt **stmt, int *readable,
                   const isti_sql *sql) {
  STATUS;
  CHECK(unpack(db3, NULL,
               sqlite3_prepare_v2(db3, sql->template->c,
                                  (int)sql->template->n.used, stmt, NULL)));
  for (int i = 0; i < sql->n_values.used; ++i) {
    isti_sql_value val = sql->values[i];
    switch (val.type) {
    case 's':
      if ((char *)val.value) {
        CHECK(unpack(db3, NULL,
            sqlite3_bind_text(*stmt, i+1, (char *)val.value, -1, SQLITE_TRANSIENT)));
      } else {
        CHECK(unpack(db3, NULL, sqlite3_bind_null(*stmt, i+1)));
      }
      break;
    case 'd':
      CHECK(unpack(db3, NULL,
          sqlite3_bind_int(*stmt, i+1, *((int *)val.value))));
      break;
    default:
      FAIL(ISTI_ERR_SQLITE, "Unexpected argument type: %%%c\n", val.type);
    }
  }
  CHECK(unpack(db3, readable, sqlite3_step(*stmt)));
  EXIT_STATUS;
}

static int sql_exec(isti_db *db, const isti_sql *sql) {
  STATUS;
  int readable = 0;
  sqlite3_stmt *stmt = NULL;
  DB3;
  CHECK(single_stmt(db3, &stmt, &readable, sql));
  EXIT;
  if (stmt) CLEANUP(unpack(db3, NULL, sqlite3_finalize(stmt)));
  RETURN;
}

static int read(sqlite3 *db, sqlite3_stmt *stmt,
                const char *types, void *s, isti_db_cb_t *cb) {
  STATUS;
  char *string;
  int integer, *p_int;
  for (size_t i = 0; i < strlen(types); ++i) {
    char type = types[i];
    switch (type) {
    case 's':
      string = NULL;
      if (SQLITE_NULL != sqlite3_column_type(stmt, (int)i)) {
        ASSERT_MEM(string = str.char_dup((char *)sqlite3_column_text(stmt, (int)i)));
      }
      CHECK(cb(s, i, type, string));
      break;
    case 'd':
      p_int = &integer;
      if (SQLITE_NULL == sqlite3_column_type(stmt, (int)i)) {
        p_int = NULL;
      } else {
        *p_int = sqlite3_column_int(stmt, (int)i);
      }
      CHECK(cb(s, i, type, p_int));
      break;
    }
  }
  EXIT_STATUS;
}

static int sql_one(isti_db *db, const isti_sql *sql,
                   const char *types, isti_db_cb_t *cb, void *s) {
  STATUS;
  int readable = 0;
  sqlite3_stmt *stmt = NULL;
  DB3;
  CHECK(single_stmt(db3, &stmt, &readable, sql));
  ASSERT_SILENT(readable, ISTI_ERR_NO_RESULT);
  CHECK(read(db3, stmt, types, s, cb));
  EXIT;
  if (stmt) CLEANUP(unpack(db3, NULL, sqlite3_finalize(stmt)));
  RETURN;
}

// there seems to be nothing faster than looping through results
static int sql_count(isti_db *db, const isti_sql *sql, int *count) {
  STATUS;
  int readable = 0;
  sqlite3_stmt *stmt = NULL;
  DB3;
  CHECK(single_stmt(db3, &stmt, &readable, sql));
  *count = 0;
  while (readable) {
    CHECK(unpack(db3, &readable, sqlite3_step(stmt)));
    ++*count;
  }
  EXIT;
  if (stmt) CLEANUP(unpack(db3, NULL, sqlite3_finalize(stmt)));
  RETURN;
}

static int sql_any(isti_db *db, const isti_sql *sql,
                   const char *types, isti_db_cb_t *cb, void *s) {
  STATUS;
  int readable = 0;
  sqlite3_stmt *stmt = NULL;
  DB3;
  CHECK(single_stmt(db3, &stmt, &readable, sql));
  while (readable) {
    CHECK(read(db3, stmt, types, s, cb));
    CHECK(unpack(db3, &readable, sqlite3_step(stmt)));
  }
  EXIT;
  if (stmt) CLEANUP(unpack(db3, NULL, sqlite3_finalize(stmt)));
  RETURN;
}

static int sql_key(isti_db *db, const isti_sql *sql,
                   size_t index, isti_db_cb_t *cb, void *s) {
  STATUS;
  DB3;
  CHECK(sql_exec(db, sql));
  int key = (int)sqlite3_last_insert_rowid(db3);
  CHECK(cb(s, index, 'd', &key));
  EXIT_STATUS;
}

static int str_exec(isti_db *db, const char* sql) {
  STATUS;
  char *error;
  DB3;
  CHECK(sqlite3_exec(db3, sql, NULL, NULL, &error));
  EXIT;
  if (error) {
    ISTI_LOG("sqlite: %s\n", error);
    ISTI_LOG("sql: %s\n", sql);
    sqlite3_free(error);
  }
  RETURN;
}

/// Public Interface
/// @param db Returned @ref isti_db instance
/// @param path Path to file containing database
/// @param timeout SQLite busy timeout
int isti_sqlite_open(struct isti_db **db, const char *path, int timeout) {
  STATUS;
  ASSERT_MEM(*db = calloc(1, sizeof(**db)));
  (*db)->close = close;
  (*db)->sql = sql_exec;
  (*db)->sql_one = sql_one;
  (*db)->sql_any = sql_any;
  (*db)->sql_count = sql_count;
  (*db)->sql_key = sql_key;
  (*db)->str = str_exec;
  ASSERT_MEM((*db)->internal = calloc(1, sizeof(sqlite)));
  CHECK(connect(*db, path, timeout));
  EXIT_STATUS;
}
