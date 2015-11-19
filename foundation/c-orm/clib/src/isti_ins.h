
#ifndef ISTI_INS_H_
#define ISTI_INS_H_

#include <stdarg.h>
#include <stdbool.h>

#include "isti_sql.h"
#include "isti_array.h"


// Fluent interface support for insert statements (not that fluent, really).


struct isti_ins;


typedef int isti_ins_free_t(struct isti_ins *, int previous);
isti_ins_free_t isti_ins_free;

typedef int isti_ins_alloc_t(struct isti_ins **);
isti_ins_alloc_t isti_ins_alloc;

typedef int isti_ins_reset_t(struct isti_ins *);
isti_ins_reset_t isti_ins_reset;

typedef struct isti_ins *isti_ins_table_t(struct isti_ins *, const char *name);
typedef struct isti_ins *isti_ins_columns_t(struct isti_ins *, const char *template);
typedef struct isti_ins *isti_ins_column_t(struct isti_ins *, const char *name);
typedef struct isti_ins *isti_ins_values_t(struct isti_ins *, ...);
typedef struct isti_ins *isti_ins_s_value_t(struct isti_ins *, const char *value);
typedef struct isti_ins *isti_ins_d_value_t(struct isti_ins *, int value);
typedef struct isti_ins *isti_ins_key_t(struct isti_ins *, const char *name);


typedef struct isti_ins_column {
  char *name;
  char *format;
} isti_ins_column;

ISTI_ARRAY_H(isti_ins_col_array, c, isti_ins_column *, cols)

typedef enum isti_ins_stmt_state {
  ISTI_INS_EMPTY=0,
  ISTI_INS_TABLE,
  ISTI_INS_COLUMNS,
  ISTI_INS_KEY,
  ISTI_INS_VALUES
} isti_ins_stmt_state;

typedef struct isti_ins_internal {
  isti_ins_stmt_state stmt;
  isti_ins_col_array *columns;
  size_t column;
  size_t key; // 1-based (0 is no key)
} isti_ins_internal;

typedef struct isti_ins {
  isti_sql *sql;
  int status;
  isti_ins_table_t *table;
  isti_ins_columns_t *columns;
  isti_ins_column_t *s_column;
  isti_ins_column_t *d_column;
  isti_ins_key_t *key;
  isti_ins_values_t *values;
  isti_ins_s_value_t *s_value;
  isti_ins_d_value_t *d_value;
  isti_ins_internal _internal;
} isti_ins;

typedef struct isti_ins_fn {
  isti_ins_free_t *free;
  isti_ins_alloc_t *alloc;
  isti_ins_reset_t *reset;
} isti_ins_fn;


#define ISTI_INS_AS(NAME) static isti_ins_fn NAME = { \
  .free = isti_ins_free, \
  .alloc = isti_ins_alloc, \
  .reset = isti_ins_reset \
};


// shorthand for defining a key
#define ISTI_INS_KEY_C(NAME, KEY) \
isti_ins *NAME(isti_ins *ins) {return ins->key(ins, #KEY);}


#endif
