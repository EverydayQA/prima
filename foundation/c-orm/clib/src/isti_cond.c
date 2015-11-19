
#include <stdio.h>

#include "isti_cond.h"
#include "isti_flow.h"
#include "isti_str.h"
#include "isti.h"

ISTI_SQL_AS(sql)
ISTI_STR_AS(str)

#define EXIT_EARLY if (cond->status) return cond;
#define COND if (! cond->status) cond->status = status; return cond
#define EXIT_COND exit: COND; return cond
#define CHECK_COND(expr) expr; if (cond->status) goto exit


int isti_cond_free(isti_cond *cond, int previous) {
  STATUS;
  if (cond) {
    CHECK(sql.free(cond->sql, status));
    free(cond);
  }
  EXIT_PREVIOUS;
}

int isti_cond_reset(isti_cond *cond) {
  STATUS;
  CHECK(sql.reset(cond->sql));
  cond->status = ISTI_OK;
  cond->_internal.where = ISTI_COND_UNKNOWN;
  EXIT_STATUS;
}

isti_cond *isti_cond_select(isti_cond *cond, const char *target) {
  STATUS;
  CHECK(sql.concatn(cond->sql, "select ", target, NULL));
  EXIT_COND;
}

isti_cond *isti_cond_selectn(isti_cond *cond, ...) {
  STATUS;
  isti_str *sql = NULL;
  va_list ap;
  va_start(ap, cond);
  CHECK(str.alloc(&sql));
  CHECK(str.vjoinn(sql, ",", ap));
  CHECK_COND(isti_cond_select(cond, sql->c));
  EXIT;
  if (sql) status = str.free(sql, status);
  va_end(ap);
  COND;
}

isti_cond *isti_cond_from(isti_cond *cond, const char *table) {
  STATUS;
  CHECK(sql.concatn(cond->sql, " from ", table, " ", NULL));
  cond->_internal.where = ISTI_COND_WHERE;
  EXIT_COND;
}

isti_cond *isti_cond_where_and(isti_cond *cond) {
  EXIT_EARLY;
  STATUS;
  switch (cond->_internal.where) {
  case ISTI_COND_WHERE:
    CHECK(sql.appendf(cond->sql, " where "));
    cond->_internal.where = ISTI_COND_UNKNOWN;
    break;
  case ISTI_COND_AND:
    CHECK(sql.appendf(cond->sql, " and "));
    cond->_internal.where = ISTI_COND_UNKNOWN;
    break;
  default:
  case ISTI_COND_UNKNOWN:
    break;
  }
  EXIT_COND;
}

#define PARAM(CODE, TYPE) \
isti_cond *isti_cond_ ## CODE ## _param(isti_cond *cond, \
        const char *name, const char *relation, const TYPE value) { \
  EXIT_EARLY; \
  STATUS; \
  isti_str *template = NULL; \
  CHECK_COND(isti_cond_where_and(cond)); \
  CHECK(str.alloc(&template)); \
  CHECK(str.concatn(template, " ", name, " ", relation, " %", #CODE, " ", NULL)); \
  CHECK_COND(isti_cond_appendf(cond, template->c, value)); \
  cond->_internal.where = ISTI_COND_AND; \
  EXIT; \
  if (template) status = str.free(template, status); \
  COND; \
}

PARAM(s, char *)
PARAM(d, int)

#define PARAMS(CODE, TYPE) \
isti_cond *isti_cond_ ## CODE ## _params(isti_cond *cond, \
        const char *name, const char *relation, const TYPE *value, size_t n) { \
  EXIT_EARLY; \
  STATUS; \
  CHECK_COND(isti_cond_where_and(cond)); \
  CHECK(sql.concatn(cond->sql, " ", name, " in (", NULL)); \
  for (size_t i = 0; i < n; ++i) { \
    if (i) CHECK(sql.append(cond->sql, ",")); \
    CHECK(sql.appendf(cond->sql, "%" #CODE, value[i])); \
  } \
  CHECK(sql.append(cond->sql, ") ")); \
  cond->_internal.where = ISTI_COND_AND; \
  EXIT_COND; \
}

PARAMS(s, char *)
PARAMS(d, int)

isti_cond *isti_cond_append(isti_cond *cond, const char *text) {
  STATUS;
  CHECK(sql.append(cond->sql, text));
  EXIT_COND;
}

isti_cond *isti_cond_appendf(isti_cond *cond, const char *template, ...) {
  EXIT_EARLY;
  STATUS;
  va_list ap; va_start(ap, template);
  CHECK(sql.vappendf(cond->sql, template, ap));
  cond->_internal.where = ISTI_COND_UNKNOWN;
  EXIT;
  va_end(ap);
  COND;
}

isti_cond *isti_cond_vappendf(isti_cond *cond, const char *template, va_list ap) {
  EXIT_EARLY;
  STATUS;
  CHECK(sql.vappendf(cond->sql, template, ap));
  cond->_internal.where = ISTI_COND_UNKNOWN;
  EXIT_COND;
}

isti_cond *isti_cond_concatn(isti_cond *cond, ...) {
  EXIT_EARLY;
  STATUS;
  va_list ap; va_start(ap, cond);
  CHECK(sql.vconcatn(cond->sql, ap));
  cond->_internal.where = ISTI_COND_UNKNOWN;
  EXIT;
  va_end(ap);
  COND;
}

isti_cond *isti_cond_vconcatn(isti_cond *cond, va_list ap) {
  EXIT_EARLY;
  STATUS;
  CHECK(sql.vconcatn(cond->sql, ap));
  cond->_internal.where = ISTI_COND_UNKNOWN;
  cond->_internal.where_and = isti_cond_where_and;
  EXIT_COND;
}

ISTI_COND_LITERAL_C(delete, "delete")
ISTI_COND_LITERAL_C(where, "where")
ISTI_COND_LITERAL_C(and, "and")
ISTI_COND_LITERAL_C(or, "or")
ISTI_COND_LITERAL_C(bra, "(")
ISTI_COND_LITERAL_C(ket, ")")

int isti_cond_alloc(isti_cond **cond) {
  STATUS;
  ASSERT_MEM(*cond = calloc(1, sizeof(**cond)));
  CHECK(sql.alloc(&(*cond)->sql));
  (*cond)->select = isti_cond_select;
  (*cond)->selectn = isti_cond_selectn;
  (*cond)->delete = isti_cond_delete;
  (*cond)->from = isti_cond_from;
  (*cond)->where = isti_cond_where;
  (*cond)->and = isti_cond_and;
  (*cond)->or = isti_cond_or;
  (*cond)->bra = isti_cond_bra;
  (*cond)->ket = isti_cond_ket;
  (*cond)->_ = isti_cond_appendf;
  (*cond)->_s = isti_cond_s_param;
  (*cond)->_d = isti_cond_d_param;
  (*cond)->_s_ = isti_cond_s_params;
  (*cond)->_d_ = isti_cond_d_params;
  (*cond)->_append = isti_cond_append;
  (*cond)->_appendf = isti_cond_appendf;
  (*cond)->_vappendf = isti_cond_vappendf;
  (*cond)->_concatn = isti_cond_concatn;
  (*cond)->_vconcatn = isti_cond_vconcatn;
  EXIT_STATUS;
}

