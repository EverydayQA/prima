
#include <stdio.h>
#include <string.h>

#include <sql.h>
#include <sqlext.h>

#include "isti.h"
#include "isti_flow.h"
#include "isti_str.h"
#include "isti_sql.h"

#include "isti_odbc.h"

ISTI_STR_AS(str)
ISTI_SQL_AS(sql)

/// @file
/// @brief The ODBC database connection (implementation).
///
/// See header for documentation. @see isti_odbc.h

// The private ADT
typedef struct odbc {
  SQLHENV env;
  SQLHDBC dbc;
} odbc;

// Extract the ADT from the public struct.
#define DBC SQLHDBC *dbc = ((odbc*)db->internal)->dbc; ASSERT(dbc, ISTI_ERR_ODBC, "Connection not opened\n")
#define ENV SQLHENV *env = ((odbc*)db->internal)->env; ASSERT(env, ISTI_ERR_ODBC, "Environment not opened\n")

static int unpack(SQLSMALLINT type, SQLHANDLE h, SQLRETURN retext) {

  int count = 0;
  SQLSMALLINT i = 0;
  SQLINTEGER native;
  SQLCHAR state[ 7 ];
  SQLCHAR text[256];
  SQLSMALLINT len;
  SQLRETURN ret;

  if (!SQL_SUCCEEDED(retext)) {
    if (h == SQL_NULL_HANDLE) {
      ISTI_LOG("odbc: error making initial connection");
      count++;
    } else {
      do {
        ret = SQLGetDiagRec(type, h, ++i, state, &native, text, sizeof(text), &len);
        if (SQL_SUCCEEDED(ret)) {
          ISTI_LOG("odbc: %s:%ld:%ld:%s\n", state, i, native, text);
          count++;
        }
      } while (SQL_SUCCEEDED(ret));
    }
    if (!count) {
      ISTI_LOG("odbc: unknown error");
    }
    return ISTI_ERR_ODBC;
  } else {
    return ISTI_OK;
  }
}

static int close(isti_db *db, int previous) {
  STATUS;
  if (db) {
    if (db->internal) {
      DBC;
      SQLDisconnect(dbc);
      SQLFreeHandle(SQL_HANDLE_DBC, dbc);
      ENV;
      SQLFreeHandle(SQL_HANDLE_ENV, env);
      free(db->internal);
    }
    free(db);
  }
  EXIT_PREVIOUS;
}

static int connect(isti_db *db, const char *dsn) {
  STATUS;
  SQLHENV *env = &((odbc*)db->internal)->env;
  SQLHDBC *dbc = &((odbc*)db->internal)->dbc;
  isti_str *cnxn = NULL;
  CHECK(unpack(SQL_HANDLE_ENV, SQL_NULL_HANDLE,
      SQLAllocHandle(SQL_HANDLE_ENV, SQL_NULL_HANDLE, env)));
  CHECK(unpack(SQL_HANDLE_ENV, *env,
      SQLSetEnvAttr(*env, SQL_ATTR_ODBC_VERSION, (void *) SQL_OV_ODBC3, 0)));
  CHECK(unpack(SQL_HANDLE_ENV, *env,
      SQLAllocHandle(SQL_HANDLE_DBC, *env, dbc)));
  CHECK(str.strf(&cnxn, "DSN=%s", dsn));
  CHECK(unpack(SQL_HANDLE_DBC, *dbc,
      SQLDriverConnect(*dbc, NULL, (SQLCHAR *) cnxn->c, SQL_NTS, NULL, 0, NULL, SQL_DRIVER_COMPLETE)));
  EXIT;
  if (cnxn) status = str.free(cnxn, status);
  RETURN;
}

static int single_stmt(SQLHDBC dbc, SQLHSTMT *stmt, const isti_sql *sql) {
  STATUS;
  SQLLEN ignored;
  CHECK(unpack(SQL_HANDLE_STMT, stmt,
      SQLAllocHandle(SQL_HANDLE_STMT, dbc, stmt)));
  for (int i = 0; i < sql->n_values.used; ++i) {
    isti_sql_value val = sql->values[i];
    switch (val.type) {
    case 's':
      // TODO - handle NULL?  handle length better?
      CHECK(unpack(SQL_HANDLE_STMT, stmt,
          SQLBindParameter(*stmt, (SQLUSMALLINT) (i+1), SQL_PARAM_INPUT,
              SQL_C_DEFAULT, SQL_CHAR, 0, 0, val.value, SQL_NTS, &ignored)));
      break;
    case 'd':
      CHECK(unpack(SQL_HANDLE_STMT, stmt,
          SQLBindParameter(*stmt, (SQLUSMALLINT) (i+1), SQL_PARAM_INPUT,
              SQL_C_DEFAULT, SQL_INTEGER, 0, 0, val.value, 0, &ignored)));
      break;
    default:
      FAIL(ISTI_ERR_ODBC, "Unexpected argument type: %%%c\n", val.type);
    }
  }
  CHECK(unpack(SQL_HANDLE_STMT, stmt,
      SQLPrepare(*stmt, (SQLCHAR *) sql->template->c, SQL_NTS)));
  CHECK(unpack(SQL_HANDLE_STMT, stmt,
      SQLExecute(*stmt)));
  EXIT_STATUS;
}

static int sql_exec(isti_db *db, const isti_sql *sql) {
  STATUS;
  SQLHSTMT stmt = NULL;
  DBC;
  CHECK(single_stmt(dbc, &stmt, sql));
  EXIT;
  if (stmt) SQLFreeHandle(SQL_HANDLE_STMT, stmt);
  RETURN;
}

static int fetch(SQLHDBC dbc, SQLHSTMT stmt, int *readable) {
  SQLRETURN ret = SQLFetch(stmt);
  *readable = 0;
  switch (ret) {
  case SQL_SUCCESS:
    *readable = 1;
    return ISTI_OK;
  case SQL_NO_DATA:
    return ISTI_OK;
  default:
    return unpack(SQL_HANDLE_STMT, stmt, ret);
  }
}

static int read(SQLHDBC dbc, SQLHSTMT stmt,
                const char *types, void *s, isti_db_cb_t *cb) {
  STATUS;
  char *string;
  int integer;
  SQLLEN len;
  SQLRETURN ret;
  for (SQLUSMALLINT i = 0; i < strlen(types); ++i) {
    char type = types[i];
    switch (type) {
    case 's':
      // first try with no space, to get total length, then retry with full length
      ret = SQLGetData(stmt, (SQLUSMALLINT) (i+1), SQL_C_CHAR, NULL, 0, &len);
      if (ret == SQL_SUCCESS_WITH_INFO) {
        len++;  // trailing NULL
        ASSERT_MEM(string = calloc((size_t) len, sizeof(*string)));
        ret = SQLGetData(stmt, (SQLUSMALLINT) (i+1), SQL_C_CHAR, string, len, &len);
      }
      CHECK(unpack(SQL_HANDLE_STMT, stmt, ret));
      CHECK(cb(s, i, type, string));
      break;
    case 'd':
      CHECK(unpack(SQL_HANDLE_STMT, stmt,
          SQLGetData(stmt, (SQLUSMALLINT) (i+1), SQL_C_DEFAULT, &integer, 0, &len)));
      CHECK(cb(s, i, type, &integer));
      break;
    }
  }
  EXIT_STATUS;
}

static int sql_one(isti_db *db, const isti_sql *sql,
                   const char *types, isti_db_cb_t *cb, void *s) {
  STATUS;
  int readable;
  SQLHSTMT stmt = NULL;
  DBC;
  CHECK(single_stmt(dbc, &stmt, sql));
  CHECK(fetch(dbc, stmt, &readable));
  ASSERT_SILENT(readable, ISTI_ERR_NO_RESULT);
  CHECK(read(dbc, stmt, types, s, cb));
  EXIT;
  if (stmt) SQLFreeHandle(SQL_HANDLE_STMT, stmt);
  RETURN;
}

static int sql_count(isti_db *db, const isti_sql *sql, int *count) {
  STATUS;
  SQLHSTMT stmt = NULL;
  SQLLEN n;
  DBC;
  CHECK(single_stmt(dbc, &stmt, sql));
  CHECK(unpack(SQL_HANDLE_STMT, stmt, SQLRowCount(stmt, &n)));
  *count = (int) n;
  EXIT;
  if (stmt) SQLFreeHandle(SQL_HANDLE_STMT, stmt);
  RETURN;
}

static int sql_any(isti_db *db, const isti_sql *sql,
                   const char *types, isti_db_cb_t *cb, void *s) {
  STATUS;
  int readable;
  SQLHSTMT stmt = NULL;
  DBC;
  CHECK(single_stmt(dbc, &stmt, sql));
  CHECK(fetch(dbc, stmt, &readable));
  while (readable) {
    CHECK(read(dbc, stmt, types, s, cb));
    CHECK(fetch(dbc, stmt, &readable));
  }
  EXIT;
  if (stmt) SQLFreeHandle(SQL_HANDLE_STMT, stmt);
  RETURN;
}

static int sql_key(isti_db *db, const isti_sql *sql,
                   size_t index, isti_db_cb_t *cb, void *s) {
  STATUS;
  FAIL(ISTI_ERR_ODBC, "No ODBC support for previous autoinc value");
  EXIT_STATUS;
}

static int str_exec(isti_db *db, const char* text) {
  STATUS;
  SQLHSTMT stmt = NULL;
  DBC;
  isti_sql *q = NULL;
  CHECK(sql.sqlf(&q, text));
  CHECK(single_stmt(dbc, &stmt, q));
  EXIT;
  if (q) CLEANUP(sql.free(q, status));
  if (stmt) SQLFreeHandle(SQL_HANDLE_STMT, stmt);
  RETURN;
}

/// Public Interface
/// @param db Returned @ref isti_db instance
/// @param path Path to file containing database
/// @param timeout SQLite busy timeout
int isti_odbc_open(struct isti_db **db, const char *dsn) {
  STATUS;
  ASSERT_MEM(*db = calloc(1, sizeof(**db)));
  (*db)->close = close;
  (*db)->sql = sql_exec;
  (*db)->sql_one = sql_one;
  (*db)->sql_any = sql_any;
  (*db)->sql_count = sql_count;
  (*db)->sql_key = sql_key;
  (*db)->str = str_exec;
  ASSERT_MEM((*db)->internal = calloc(1, sizeof(odbc)));
  CHECK(connect(*db, dsn));
  EXIT_STATUS;
}
