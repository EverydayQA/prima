
#ifndef ISTI_SQLITE_H_
#define ISTI_SQLITE_H_

#include <stdarg.h>

#include "isti_db.h"

/** @file

@brief The SQLite database connection (interface).

An implementation of @ref isti_db for SQLite3.

Use via the ISTI_SQLITE_AS() macro.

@see isti_sqlite.c

*/

typedef int isti_sqlite_open_t(struct isti_db **db, const char *path, int timeout);
/// Create a new @ref isti_db instance.
isti_sqlite_open_t isti_sqlite_open;

/// @brief The namespace returned by ISTI_SQLITE_AS().
/// This provide the "variables" as fields with shorter names.
typedef struct isti_sqlite_fn {
  isti_sqlite_open_t *open;
} isti_sqlite_fn;

/// Use this macro to define a namespace for the routines here.
#define ISTI_SQLITE_AS(NAME) static isti_sqlite_fn NAME = { \
    .open = isti_sqlite_open \
};

#endif
