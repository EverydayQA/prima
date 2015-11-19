
#ifndef ISTI_ODBC_H_
#define ISTI_ODBC_H_

#include <stdarg.h>

#include "isti_db.h"

/** @file

@brief The ODBC database connection (interface).

An implementation of @ref isti_db for ODBC.

Use via the ISTI_ODBC_AS() macro.

@see isti_osbc.c

*/

typedef int isti_odbc_open_t(struct isti_db **db, const char *dsn);
/// Create a new @ref isti_db instance.
isti_odbc_open_t isti_odbc_open;

/// @brief The namespace returned by ISTI_ODBC_AS().
/// This provide the "variables" as fields with shorter names.
typedef struct isti_odbc_fn {
  isti_odbc_open_t *open;
} isti_odbc_fn;

/// Use this macro to define a namespace for the routines here.
#define ISTI_ODBC_AS(NAME) static isti_odbc_fn NAME = { \
    .open = isti_odbc_open \
};

#endif
