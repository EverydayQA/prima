
#include <stdio.h>

#include "isti.h"
#include "isti_flow.h"
#include "isti_sql.h"

ISTI_MEM_AS(mem)
ISTI_STR_AS(str)

/// @file
/// @brief Construction of SQL commands (implementation).
///
/// See header for documentation. @see isti_sql.h

int isti_sql_free_values(void *data, size_t n, int previous) {
  STATUS;
  isti_sql_value *values = (isti_sql_value*)data;
  for (size_t i = 0; i < n; ++i) {
    isti_sql_value value = values[i];
    switch(value.type) {
    case 's':
      free((char*)value.value);
      break;
    case 'd':
      free((int*)value.value);
      break;
    default:
      FAIL(ISTI_ERR_SQL, "Unexpected argument type: %%%c\n", value.type);
    }
  }
  free(data);
  EXIT_PREVIOUS;
}

int isti_sql_free(isti_sql *sql, int previous) {
  STATUS;
  if (sql) {
    status = mem.free(&sql->n_values, isti_sql_free_values, sql->values, status);
    status = str.free(sql->template, status);
    free(sql);
  }
  RETURN;
}

int isti_sql_alloc(isti_sql **sql) {
  STATUS;
  ASSERT_MEM(*sql = calloc(1, sizeof(**sql)));
  CHECK(str.alloc(&(*sql)->template));
  EXIT_STATUS;
}

int isti_sql_reset(isti_sql *sql) {
  STATUS;
  CHECK(mem.reset(&sql->n_values, isti_sql_free_values, sql->values, sizeof(*sql->values)));
  CHECK(str.reset(sql->template));
  EXIT_STATUS;
}

int isti_sql_sql(isti_sql **sql, const char *command) {
  STATUS;
  CHECK(isti_sql_alloc(sql));
  CHECK(str.append((*sql)->template, command));
  EXIT_STATUS;
}

// Value parsing

// The commands below support a syntax similar to `printf` and friends,
// but simplified.  The `command` string is of the form
//     "select * from foo where name=%s and age=%d"
// which will be converted into
//     "select * from foo where name=? and age=?"
// (the standard format for SQL substitution) while consuming two arguments,
// which will be assumed to have the given types (`char*` and `int`).

// The arguments are stored as `isti_sql_value` instances, with the values
// stored in newly allocated memory (so `int` is stored as an `int*`
// isti_sql_value).

// Delegate that implements the varag interfaces.  The `command` is appended
// to the template and one type/value pair stored for each "?".
int isti_sql_vappendf(isti_sql *sql, const char *command, va_list ap) {
  int *d;
  char *s;
  STATUS;
  for (const char *c = command; *c; ++c) {
    if (*c == '%') {
      ++c;
      ASSERT_MEM(sql->values = mem.inc(&sql->n_values, sql->values, sizeof(*sql->values)));
      sql->values[sql->n_values.used].type = *c;
      switch(*c) {
      case 's':
        s = va_arg(ap, char*);
        if (s) ASSERT_MEM(sql->values[sql->n_values.used].value = str.char_dup(s));
        else sql->values[sql->n_values.used].value = NULL;
        break;
      case 'd':
        d = calloc(1, sizeof(*d));
        *d = va_arg(ap, int);
        ASSERT_MEM(sql->values[sql->n_values.used].value = d);
        break;
      default:
        FAIL(ISTI_ERR_SQL, "Unexpected argument type: %%%c\n", *c);
      }
      sql->n_values.used++;
      str.inc(sql->template, '?');
    } else {
      str.inc(sql->template, *c);
    }
  }
  EXIT_STATUS;
}

int isti_sql_sqlf(isti_sql **sql, const char *command, ...) {
  STATUS;
  va_list ap;
  va_start(ap, command);
  CHECK(isti_sql_alloc(sql));
  CHECK(isti_sql_vappendf(*sql, command, ap));
  EXIT;
  va_end(ap);
  RETURN;
}

int isti_sql_appendf(isti_sql *sql, const char *command, ...) {
  STATUS;
  va_list ap;
  va_start(ap, command);
  CHECK(isti_sql_vappendf(sql, command, ap));
  EXIT;
  va_end(ap);
  RETURN;
}

// this is not quite the same as appendf with no varags because the
// escape character % is treated differently.
int isti_sql_append(isti_sql *sql, const char *command) {
  return str.append(sql->template, command);
}

int isti_sql_concatn(isti_sql *sql, ...) {
  STATUS;
  va_list ap;
  va_start(ap, sql);
  CHECK(str.vconcatn(sql->template, ap));
  EXIT;
  va_end(ap);
  RETURN;
}

int isti_sql_vconcatn(isti_sql *sql, va_list ap) {
  return str.vconcatn(sql->template, ap);
}

int isti_sql_unsafe(isti_sql *sql, char **text) {
  STATUS;
  isti_str *s = NULL;
  CHECK(str.str(&s, "-- "));
  int ivalue = 0;
  for (char *c = sql->template->c; *c; ++c) {
      if (*c == '?') {
        switch(sql->values[ivalue].type) {
        case 's':
          if ((char*)sql->values[ivalue].value)
            CHECK(str.appendf(s, "'%s'", (char*)sql->values[ivalue].value));
          else CHECK(str.append(s, "NULL"));
          break;
        case 'd':
          CHECK(str.appendf(s, "%d", *((int*)sql->values[ivalue].value)));
          break;
        default:
          FAIL(ISTI_ERR_SQL, "Unexpected argument type: %%%c\n", *c);
        }
        ivalue++;
      } else {
        str.inc(s, *c);
      }
  }
  ASSERT_MEM(*text = str.char_dup(s->c));
  EXIT;
  if (s) status = str.free(s, status);
  RETURN;
}
