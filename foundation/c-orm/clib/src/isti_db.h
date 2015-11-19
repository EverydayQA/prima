
#ifndef ISTI_DB_H
#define ISTI_DB_H

#include <stdarg.h>

#include "isti_sql.h"

/** @file

@brief The database interface.

Different database implementations can implement this interface.
Each will provide an "open" method, separate from the interface,
which accepts a `char *` and returns an instance.  The `void *internal`
member is available for internal state and functions.

Note: Unlike many other interfaces here, which are static namespaces,
this represents a single database connection.

**Incomplete and very open to change.**

*/

struct isti_db;

/// Close the connection and free associated memory.
typedef int (isti_db_close_t)(struct isti_db *db, int previous);

/// The callback used to return data (appears below).  Values are always
/// pointers (char * is char *, but int is int *).
typedef int (isti_db_cb_t)(void *ptr, size_t index, char type, void *value);

/// Execute a statement, but retrieve nothing.
typedef int (isti_db_sql_t)(struct isti_db *db, const isti_sql *sql);

/// Execute a statement and retrieve a single row of data via the callback.
typedef int (isti_db_sql_one_t)(struct isti_db *db, const isti_sql *sql,
                                const char *code, isti_db_cb_t *cb, void *cb_value);

/// Execute a statement and retrieve multiple rows.
typedef int (isti_db_sql_any_t)(struct isti_db *db, const isti_sql *sql,
                                const char *codes, isti_db_cb_t *cb, void *cb_value);

/// Retrieve the number of results returned by a statement (not used in
/// the framework, but may be useful for someone wanting to pre-allocate
/// space (but note that SQLite is inefficient)).
typedef int (isti_db_sql_count_t)(struct isti_db *db, const isti_sql *sql,
                                  int *n);

/// Execute a statement and retrieve the latest key via the callback.
typedef int (isti_db_sql_key_t)(struct isti_db *db, const isti_sql *sql,
                                size_t index, isti_db_cb_t *cb, void *cb_value);

/// Execute multiple statements, without parameters (eg DDL).
typedef int (isti_db_str_t)(struct isti_db *db, const char *sql);


/// The interface to a database.
typedef struct isti_db {
  isti_db_close_t *close;
  isti_db_sql_t *sql;
  isti_db_sql_one_t *sql_one;
  isti_db_sql_any_t *sql_any;
  isti_db_sql_count_t *sql_count;
  isti_db_sql_key_t *sql_key;
  isti_db_str_t *str;
  /// The implementation's ADT.
  void *internal;
} isti_db;


#endif
