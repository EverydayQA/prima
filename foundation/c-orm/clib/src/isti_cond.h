
#ifndef ISTI_COND_H_
#define ISTI_COND_H_

#include <stdarg.h>

#include "isti_sql.h"
#include "isti_array.h"


// Fluent interface support for conditional statements.  Used for select and
// update, but not for insert.


struct isti_cond;


typedef int isti_cond_free_t(struct isti_cond *, int previous);
isti_cond_free_t isti_cond_free;

typedef int isti_cond_alloc_t(struct isti_cond **);
isti_cond_alloc_t isti_cond_alloc;

typedef int isti_cond_reset_t(struct isti_cond *);
isti_cond_reset_t isti_cond_reset;

typedef struct isti_cond *isti_cond_select_t(struct isti_cond *, const char *targets);
isti_cond_select_t isti_cond_select;

typedef struct isti_cond *isti_cond_selectn_t(struct isti_cond *, ...);
isti_cond_selectn_t isti_cond_selectn;

typedef struct isti_cond *isti_cond_from_t(struct isti_cond *, const char *table);
isti_cond_from_t isti_cond_from;

typedef struct isti_cond *isti_cond_where_and_t(struct isti_cond *);
isti_cond_where_and_t isti_cond_where_and;

typedef struct isti_cond *isti_cond_s_param_t(struct isti_cond *,
    const char *name, const char *relation, const char *value);
isti_cond_s_param_t isti_cond_s_param;

typedef struct isti_cond *isti_cond_d_param_t(struct isti_cond *,
    const char *name, const char *relation, const int value);
isti_cond_d_param_t isti_cond_d_param;

typedef struct isti_cond *isti_cond_s_params_t(struct isti_cond *,
    const char *name, const char *relation, const char **value, size_t n);
isti_cond_s_params_t isti_cond_s_params;

typedef struct isti_cond *isti_cond_d_params_t(struct isti_cond *,
    const char *name, const char *relation, const int *value, size_t n);
isti_cond_d_params_t isti_cond_d_params;

typedef struct isti_cond *isti_cond_append_t(struct isti_cond *, const char *sql);
isti_cond_append_t isti_cond_append;

typedef struct isti_cond *isti_cond_appendf_t(struct isti_cond *, const char *template, ...);
isti_cond_appendf_t isti_cond_appendf;

typedef struct isti_cond *isti_cond_vappendf_t(struct isti_cond *, const char *template, va_list);
isti_cond_vappendf_t isti_cond_vappendf;

typedef struct isti_cond *isti_cond_concatn_t(struct isti_cond *, ...);
isti_cond_concatn_t isti_cond_concatn;

typedef struct isti_cond *isti_cond_vconcatn_t(struct isti_cond *, va_list ap);
isti_cond_vconcatn_t isti_cond_vconcatn;


typedef struct isti_cond *isti_cond_literal_t(struct isti_cond *);
isti_cond_literal_t isti_cond_delete;
isti_cond_literal_t isti_cond_where;
isti_cond_literal_t isti_cond_and;
isti_cond_literal_t isti_cond_or;
isti_cond_literal_t isti_cond_bra;
isti_cond_literal_t isti_cond_ket;


typedef enum isti_cond_where_state {
  ISTI_COND_UNKNOWN=0,
  ISTI_COND_WHERE,
  ISTI_COND_AND
} isti_cond_where_state;

typedef struct isti_cond_internal {
  isti_cond_where_state where;
  isti_cond_where_and_t *where_and;
} isti_cond_internal;


typedef struct isti_cond {
  isti_sql *sql;
  int status;
  isti_cond_select_t *select;
  isti_cond_selectn_t *selectn;
  isti_cond_literal_t *delete;
  isti_cond_from_t *from;
  isti_cond_literal_t *where;
  isti_cond_literal_t *and;
  isti_cond_literal_t *or;
  isti_cond_literal_t *bra;
  isti_cond_literal_t *ket;
  isti_cond_appendf_t *_;
  isti_cond_s_param_t *_s;
  isti_cond_d_param_t *_d;
  isti_cond_s_params_t *_s_;
  isti_cond_d_params_t *_d_;
  isti_cond_append_t *_append;
  isti_cond_appendf_t *_appendf;
  isti_cond_vappendf_t *_vappendf;
  isti_cond_concatn_t *_concatn;
  isti_cond_vconcatn_t *_vconcatn;
  isti_cond_internal _internal;
} isti_cond;

typedef struct isti_cond_fn {
  isti_cond_free_t *free;
  isti_cond_alloc_t *alloc;
  isti_cond_reset_t *reset;
} isti_cond_fn;


#define ISTI_COND_AS(NAME) static isti_cond_fn NAME = { \
  .free = isti_cond_free, \
  .alloc = isti_cond_alloc, \
  .reset = isti_cond_reset \
};


// shorthand for adding literal text (with surrounding spaces)
#define ISTI_COND_LITERAL_C(NAME, TEXT) \
isti_cond *isti_cond_ ## NAME(isti_cond *cond) {return cond->_(cond, " " TEXT " ");}

// parameter support

#define ISTI_COND_PARAM_R(NAME, RECORD) NAME ## _t *RECORD;
#define ISTI_COND_PARAM_S(PREFIX, NAME, RECORD) .PREFIX.RECORD = NAME
#define ISTI_COND_PARAM_T(NAME, CODE, TYPE) \
typedef isti_cond *NAME ## _t(isti_cond *cond, const char *relation, const TYPE value);
#define ISTI_COND_PARAM_H(NAME) NAME ## _t NAME;
#define ISTI_COND_PARAM_C(NAME, COLUMN, CODE, TYPE) \
isti_cond *NAME(isti_cond *cond, const char *relation, const TYPE value) { \
  return isti_cond_ ## CODE ## _param(isti_cond_where_and(cond), COLUMN, relation, value); \
}

#define ISTI_COND_PARAMS_R(NAME, RECORD) NAME ## _t *RECORD ## _;
#define ISTI_COND_PARAMS_S(PREFIX, NAME, RECORD) .PREFIX.RECORD ## _ = NAME
#define ISTI_COND_PARAMS_T(NAME, CODE, TYPE) \
typedef isti_cond *NAME ## _t(isti_cond *cond, const char *relation, const TYPE *value, size_t n);
#define ISTI_COND_PARAMS_H(NAME) NAME ## _t NAME;
#define ISTI_COND_PARAMS_C(NAME, COLUMN, CODE, TYPE) \
isti_cond *NAME(isti_cond *cond, const char *relation, const TYPE *value, size_t n) { \
  return isti_cond_ ## CODE ## _params(isti_cond_where_and(cond), COLUMN, relation, value, n); \
}


#endif
