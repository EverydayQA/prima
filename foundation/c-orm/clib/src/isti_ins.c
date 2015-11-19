
#include <stdio.h>

#include "isti_ins.h"
#include "isti_flow.h"
#include "isti_str.h"
#include "isti.h"

ISTI_SQL_AS(sql)
ISTI_STR_AS(str)

int isti_ins_col_free(void * data, size_t n, int previous) {
  STATUS;
  isti_ins_column** values = (isti_ins_column**)data;
  for (size_t i = 0; i < n; ++i) {
    free(values[i]->name);
    free(values[i]);
  }
  free(data);
  RETURN_PREVIOUS;
}

ISTI_ARRAY_C(isti_ins_col_array, c, isti_ins_column *, cols, isti_ins_col_free)
ALIAS_ARRAY_AS(isti_ins_col_array, cols)

#define EXIT_EARLY if (ins->status) return ins;
#define INS if (! ins->status) ins->status = status; return ins
#define EXIT_INS exit: INS; return ins
#define CHECK_INS(expr) expr; if (ins->status) goto exit

int isti_ins_free(isti_ins *ins, int previous) {
  STATUS;
  if (ins) {
    CHECK(sql.free(ins->sql, status));
    CHECK(cols.free(ins->_internal.columns, status));
    free(ins);
  }
  EXIT_PREVIOUS;
}

int isti_ins_reset(isti_ins *ins) {
  STATUS;
  CHECK(sql.reset(ins->sql));
  ins->status = ISTI_OK;
  ins->_internal.stmt = ISTI_INS_EMPTY;
  ins->_internal.column = 0;
  ins->_internal.key = 0;
  CHECK(cols.reset(ins->_internal.columns));
  EXIT_STATUS;
}

static isti_ins *table(isti_ins *ins, const char *name) {
  EXIT_EARLY;
  STATUS;
  if (ins->_internal.stmt == ISTI_INS_EMPTY) {
    CHECK(sql.concatn(ins->sql, "insert into \"", name, "\" ", NULL));
    ins->_internal.stmt = ISTI_INS_TABLE;
  } else {
    FAIL(ISTI_ERR_SQL, "Bad SQL order (table %s)\n", name);
  }
  EXIT_INS;
}

// check for duplicate names?
#define COLUMN(CODE) \
static isti_ins *CODE ## _column(isti_ins *ins, const char *name) { \
  EXIT_EARLY; \
  STATUS; \
  isti_ins_column *col = NULL; \
  ASSERT(ins->_internal.stmt == ISTI_INS_TABLE \
      || ins->_internal.stmt == ISTI_INS_COLUMNS, \
      ISTI_ERR_SQL, "Bad SQL order (column %s)\n", name); \
  if (ins->_internal.stmt == ISTI_INS_TABLE) CHECK(sql.append(ins->sql, "(")); \
  else CHECK(sql.append(ins->sql, ",")); \
  CHECK(sql.concatn(ins->sql, "\"", name, "\"", NULL)); \
  ins->_internal.stmt = ISTI_INS_COLUMNS; \
  ASSERT_MEM(col = calloc(1, sizeof(*col))); \
  ASSERT_MEM(col->name = str.char_dup(name)); \
  col->format = "%" #CODE; \
  cols.inc(ins->_internal.columns, col); \
  EXIT_INS; \
}

COLUMN(s)
COLUMN(d)

static isti_ins *set_key(isti_ins *ins, const char *key) {
  EXIT_EARLY;
  STATUS;
  ASSERT(! ins->_internal.key, ISTI_ERR_SQL, "Duplicate key\n");
  for (size_t i = 0; i < ins->_internal.columns->n.used; ++i) {
    if (!strcmp(key, ins->_internal.columns->cols[i]->name)) ins->_internal.key = i+1;
  }
  ASSERT(ins->_internal.key, ISTI_ERR_SQL, "Missing key %s\n", key);
  EXIT_INS;
}

static isti_ins *columns(isti_ins *ins, const char *template) {
  EXIT_EARLY;
  STATUS;
  isti_chars_array *cols = NULL, *toks = NULL;
  CHECK(str.split(&cols, template, ",", -1));
  for (int i = 0; i < cols->n.used; ++i) {
    str.split(&toks, cols->c[i], " =", 2);
    ASSERT(toks->n.used == 2, ISTI_ERR_SQL, "Cannot parse %s\n", cols->c[i]);
    if (!strcmp(toks->c[1], "KEY")) { // special case the key
      CHECK_INS(d_column(ins, toks->c[0]));
      CHECK_INS(set_key(ins, toks->c[0]));
    } else {
      ASSERT(strlen(toks->c[1]) == 2, ISTI_ERR_SQL, "Cannot parse %s\n", cols->c[i]);
      ASSERT(toks->c[1][0] == '%', ISTI_ERR_SQL, "Cannot parse %s\n", cols->c[i]);
      switch (toks->c[1][1]) {
      case 's': CHECK_INS(s_column(ins, toks->c[0])); break;
      case 'd': CHECK_INS(d_column(ins, toks->c[0])); break;
      default: FAIL(ISTI_ERR_SQL, "Unexpected argument type: %%%c\n", toks->c[1][1]);
      }
    }
    status = isti_chars_array_free(toks, status); toks = NULL; CHECK(status);
  }
  EXIT;
  if (cols) status = isti_chars_array_free(cols, status);
  if (toks) status = isti_chars_array_free(toks, status);
  INS;
}

static isti_ins *key(isti_ins *ins, const char *key) {
  EXIT_EARLY;
  STATUS;
  ASSERT(ins->_internal.stmt == ISTI_INS_COLUMNS,
      ISTI_ERR_SQL, "Bad SQL order (key %s)\n", key);
  CHECK_INS(set_key(ins, key));
  ins->_internal.stmt = ISTI_INS_KEY;
  EXIT_INS;
}

#define VALUE(CODE, TYPE) \
static isti_ins *CODE ## _value(isti_ins *ins, TYPE value) { \
  EXIT_EARLY; \
  STATUS; \
  ASSERT(ins->_internal.stmt == ISTI_INS_COLUMNS \
      || ins->_internal.stmt == ISTI_INS_KEY \
      || ins->_internal.stmt == ISTI_INS_VALUES, \
      ISTI_ERR_SQL, "Bad SQL order (value before key / column)\n"); \
  if (ins->_internal.column) { \
    if (ins->_internal.stmt == ISTI_INS_VALUES) CHECK(sql.append(ins->sql, ",")); \
  } else { \
    if (ins->_internal.stmt != ISTI_INS_VALUES) CHECK(sql.append(ins->sql, ") values (")); \
    else CHECK(sql.append(ins->sql, ", (")); \
  } \
  if (ins->_internal.column + 1 == ins->_internal.key) { \
    CHECK(sql.append(ins->sql, "NULL")); \
  } else { \
    CHECK(sql.appendf(ins->sql, \
        ins->_internal.columns->cols[ins->_internal.column]->format, \
        value)); \
  } \
  ins->_internal.column = \
      (ins->_internal.column + 1) % ins->_internal.columns->n.used; \
  if (! ins->_internal.column) CHECK(sql.append(ins->sql, ")")); \
  ins->_internal.stmt = ISTI_INS_VALUES; \
  EXIT_INS; \
}

VALUE(s, const char*)
VALUE(d, int)

static isti_ins *values(isti_ins *ins, ...) {
  EXIT_EARLY;
  STATUS;
  va_list ap;
  va_start(ap, ins);
  int d;
  char *s;
  ASSERT(! ins->_internal.column, ISTI_ERR_SQL, "Incomplete values\n");
  for (size_t i = 0; i < ins->_internal.columns->n.used; ++i) {
    switch (ins->_internal.columns->cols[i]->format[1]) {
    case 'd':
      d = va_arg(ap, int);
      CHECK_INS(d_value(ins, d));
      break;
    case 's':
      s = va_arg(ap, char*);
      CHECK_INS(s_value(ins, s));
      break;
    default:
      FAIL(ISTI_ERR_SQL, "Unexpected argument type: %%%c\n",
          ins->_internal.columns->cols[i]->format[1]);
    }
  }
  ASSERT(! ins->_internal.column, ISTI_ERR_SQL, "Incomplete values\n");
  EXIT;
  va_end(ap);
  INS;
}

int isti_ins_alloc(isti_ins **ins) {
  STATUS;
  ASSERT_MEM(*ins = calloc(1, sizeof(**ins)));
  CHECK(sql.alloc(&(*ins)->sql));
  CHECK(cols.alloc(&(*ins)->_internal.columns));
  (*ins)->table = table;
  (*ins)->columns = columns;
  (*ins)->s_column = s_column;
  (*ins)->d_column = d_column;
  (*ins)->key = key;
  (*ins)->values = values;
  (*ins)->s_value = s_value;
  (*ins)->d_value = d_value;
  EXIT_STATUS;
}

