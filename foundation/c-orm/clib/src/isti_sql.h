
#ifndef ISTI_SQL_H_
#define ISTI_SQL_H_

#include <stdarg.h>

#include "isti_mem.h"
#include "isti_str.h"

/** @file

@brief Construction of SQL commands (interface).

Allow SQL commands to be constructed via a typed template, with
arguments.  The types follow standard (printf) conventions.  Commands
can also be extended further, via `append`.

Use via the ISTI_SQL_AS() macro.  For example, here is a statement
with string and integer parameters:

@code
ISTI_SQL_AS(sql)
...
  isti_sql *q = NULL;
  STATUS;
  CHECK(sql.sql(&q, "select * from foo where a=%s and b=%d", "foo", 42));
  ASSERT(! strcmp(q->template.c, "select * from foo where a=? and b=?"), ISTI_ERR_SQL)
  ASSERT(q->n_values.used == 2, ISTI_ERR_SQL)
  ASSERT(q->values[0].type == 's', ISTI_ERR_SQL);
  ASSERT(! strcmp((char*)q->values[0].value, "foo"), ISTI_ERR_SQL);
  ASSERT(q->values[1].type == 'd', ISTI_ERR_SQL);
  ASSERT(*((int*)q->values[1].value) == 42, ISTI_ERR_SQL);
  CHECK(sql.append(&q, " and c=%d", 3));
  EXIT;
  status = sql->free(q, status);
  RETURN;
...
@endcode

(The code above uses macros from @ref isti_flow.h).

@see isti_sql.c

*/

/// @brief Associate a pointer to a value with a type.  This is a single
/// entry in a list of arguments (eg. "where" conditions).
typedef struct isti_sql_value {
  void *value;
  char type;
} isti_sql_value;

/// @brief The SQL phrase, which can be extended incrementally.
typedef struct isti_sql {
  isti_str *template;
  isti_sql_value *values;
  isti_mem n_values;
} isti_sql;

typedef int isti_sql_free_values_t(void *data, size_t n, int previous);
isti_sql_free_values_t isti_sql_free_values;

/// `previous` is the caller's status, used to chain status during exit.
typedef int isti_sql_free_t(struct isti_sql *sql, int previous);
/// Release memory.
isti_sql_free_t isti_sql_free;

typedef int isti_sql_alloc_t(struct isti_sql **sql);
/// @brief Allocate a new, empty statement.  Called by `sql`, so direct
/// use is unusual.
isti_sql_alloc_t isti_sql_alloc;

typedef int isti_sql_reset_t(struct isti_sql *sql);
isti_sql_reset_t isti_sql_reset;

typedef int isti_sql_sql_t(struct isti_sql **sql, const char *text);
/// Allocate a new statement and add the given text.
isti_sql_sql_t isti_sql_sql;

typedef int isti_sql_sqlf_t(struct isti_sql **sql, const char *template, ...);
/// Allocate a new statement and add the given text and parameters.
isti_sql_sqlf_t isti_sql_sqlf;

typedef int isti_sql_append_t(struct isti_sql *sql, const char *text);
/// Append text to an existing statement.
isti_sql_append_t isti_sql_append;

typedef int isti_sql_appendf_t(struct isti_sql *sql, const char *template, ...);
/// Append text and parameters to an existing statement.
isti_sql_appendf_t isti_sql_appendf;

typedef int isti_sql_vappendf_t(struct isti_sql *sql, const char *template, va_list);
/// Varags alternative to the above.
isti_sql_vappendf_t isti_sql_vappendf;

typedef int isti_sql_concatn_t(struct isti_sql *sql, ...);
/// Append text until NULL.
isti_sql_concatn_t isti_sql_concatn;

typedef int isti_sql_vconcatn_t(struct isti_sql *sql, va_list);
/// Varags alternative to the above.
isti_sql_vconcatn_t isti_sql_vconcatn;

typedef int isti_sql_unsafe_t(struct isti_sql *sql, char **text);
/// Convert SQL to text.
isti_sql_unsafe_t isti_sql_unsafe;

  /// @brief The namespace returned by ISTI_SQL_AS().
/// This provide the "variables" as fields with shorter names.
typedef struct isti_sql_fn {
  isti_sql_free_values_t *free_values;
  isti_sql_free_t *free;
  isti_sql_alloc_t *alloc;
  isti_sql_reset_t *reset;
  isti_sql_sql_t *sql;
  isti_sql_sqlf_t *sqlf;
  isti_sql_append_t *append;
  isti_sql_appendf_t *appendf;
  isti_sql_vappendf_t *vappendf;
  isti_sql_concatn_t *concatn;
  isti_sql_vconcatn_t *vconcatn;
  isti_sql_unsafe_t *unsafe;
} isti_sql_fn;

/// Use this macro to define a namespace for the routines here.
#define ISTI_SQL_AS(NAME) static isti_sql_fn NAME = { \
    .free_values = isti_sql_free_values, \
    .free = isti_sql_free, \
    .alloc = isti_sql_alloc, \
    .reset = isti_sql_reset, \
    .sql = isti_sql_sql, \
    .sqlf = isti_sql_sqlf, \
    .append = isti_sql_append, \
    .appendf = isti_sql_appendf, \
    .vappendf = isti_sql_vappendf, \
    .concatn = isti_sql_concatn, \
    .vconcatn = isti_sql_vconcatn, \
    .unsafe = isti_sql_unsafe \
  };

#endif
