
#ifndef ISTI_CORM_H_
#define ISTI_CORM_H_

#include <stdarg.h>

#include "isti_sql.h"
#include "isti_db.h"
#include "isti_array.h"
#include "isti_cond.h"



// below are macros that help simplify the auto-generation of ORM code


// often we want to delegate literals to an "underlying" isti_cond structure
// (for example in a select struct).

#define ISTI_CORM_DELEGATE_LITERAL_C(STRUCT, PREFIX, TARGET) \
STRUCT *PREFIX ## _ ## TARGET(STRUCT *s) {s->_cond->TARGET(s->_cond); return s;};

#define ISTI_CORM_DELEGATE_S_PARAM_C(STRUCT, NAME, TARGET) \
STRUCT *NAME(STRUCT *s, const char *relation, const char *value) { \
  TARGET(s->_cond, relation, value); return s; \
}

#define ISTI_CORM_DELEGATE_D_PARAM_C(STRUCT, NAME, TARGET) \
STRUCT *NAME(STRUCT *s, const char *relation, int value) { \
  TARGET(s->_cond, relation, value); return s; \
}

#define ISTI_CORM_DELEGATE_S_PARAMS_C(STRUCT, NAME, TARGET) \
STRUCT *NAME(STRUCT *s, const char *relation, const char **value, size_t n) { \
  TARGET(s->_cond, relation, value, n); return s; \
}

#define ISTI_CORM_DELEGATE_D_PARAMS_C(STRUCT, NAME, TARGET) \
STRUCT *NAME(STRUCT *s, const char *relation, const int *value, size_t n) { \
  TARGET(s->_cond, relation, value, n); return s; \
}

// delegate the entire set of "standard" words

#define ISTI_CORM_DELEGATE_LITERALS_C(STRUCT, PREFIX) \
static ISTI_CORM_DELEGATE_LITERAL_C(STRUCT, PREFIX, where) \
static ISTI_CORM_DELEGATE_LITERAL_C(STRUCT, PREFIX, and) \
static ISTI_CORM_DELEGATE_LITERAL_C(STRUCT, PREFIX, or) \
static ISTI_CORM_DELEGATE_LITERAL_C(STRUCT, PREFIX, bra) \
static ISTI_CORM_DELEGATE_LITERAL_C(STRUCT, PREFIX, ket)


// every sql command (select etc) includes those words, within a struct

#define ISTI_CORM_LITERAL_R(PREFIX, TARGET) PREFIX ## _literal_t * _ ## TARGET;
#define ISTI_CORM_LITERALS_R(PREFIX) \
ISTI_CORM_LITERAL_R(PREFIX, where) \
ISTI_CORM_LITERAL_R(PREFIX, and) \
ISTI_CORM_LITERAL_R(PREFIX, or) \
ISTI_CORM_LITERAL_R(PREFIX, bra) \
ISTI_CORM_LITERAL_R(PREFIX, ket)

#define ISTI_CORM_LITERAL_S(PTR, PREFIX, TARGET) PTR -> _ ## TARGET = PREFIX ## _ ## TARGET;
#define ISTI_CORM_LITERALS_S(PTR, PREFIX) \
ISTI_CORM_LITERAL_S(PTR, PREFIX, where) \
ISTI_CORM_LITERAL_S(PTR, PREFIX, and) \
ISTI_CORM_LITERAL_S(PTR, PREFIX, or) \
ISTI_CORM_LITERAL_S(PTR, PREFIX, bra) \
ISTI_CORM_LITERAL_S(PTR, PREFIX, ket)


// a select has a bunch of standard types.  these assume that they will be
// defined using a struct called PREFIX_select

#define ISTI_CORM_SELECTS_T(PREFIX, PTR, ARRAY) \
typedef int PREFIX ## _select_alloc_t(struct PREFIX ## _select **, isti_db *); \
typedef int PREFIX ## _select_free_t(struct PREFIX ## _select *, int); \
typedef int PREFIX ## _select_reset_t(struct PREFIX ## _select *); \
typedef struct PREFIX ## _select * PREFIX ## _select_literal_t(struct PREFIX ## _select *); \
typedef struct PREFIX ## _select * PREFIX ## _select_text_t(struct PREFIX ## _select *, const char *, ...); \
typedef int PREFIX ## _select_go_one_t(struct PREFIX ## _select *, PTR **); \
typedef int PREFIX ## _select_go_count_t(struct PREFIX ## _select *, int *); \
typedef int PREFIX ## _select_go_any_t(struct PREFIX ## _select *, ARRAY **);

#define ISTI_CORM_SELECT_ALLOC_H(PREFIX) \
int PREFIX ## _select_alloc(struct PREFIX ## _select **, isti_db *);

// and many of those are records inside that struct

#define ISTI_CORM_SELECTS_R(PREFIX) \
PREFIX ## _select_free_t *_free; \
PREFIX ## _select_reset_t *_reset; \
PREFIX ## _select_text_t *_; \
PREFIX ## _select_go_one_t *_go_one; \
PREFIX ## _select_go_count_t *_go_count; \
PREFIX ## _select_go_any_t *_go_any;

// most of which are set on the struct

#define ISTI_CORM_SELECTS_S(PARENT, PREFIX) \
PARENT ._ = PREFIX ## _select_text; \
PARENT ._go_one = PREFIX ## _select_one; \
PARENT ._go_count = PREFIX ## _select_count; \
PARENT ._go_any = PREFIX ## _select_any; \
PARENT ._reset = PREFIX ## _select_reset; \
PARENT ._free = PREFIX ## _select_free;

// and the implementations, which typically delegate to COND functions

#define ISTI_CORM_SELECT_TEXT_C(PREFIX) \
static PREFIX ## _select *PREFIX ## _select_text(PREFIX ## _select *s, const char *template, ...) { \
  va_list ap; va_start(ap, template); \
  isti_cond_vappendf(s->_cond, template, ap); \
  va_end(ap); \
  return s; \
}

#define ISTI_CORM_SELECT_ONE_C(PREFIX, TYPE, CODES, READ) \
static int PREFIX ## _select_one(PREFIX ## _select *s, TYPE **v) { \
  STATUS; \
  CHECK(s->_cond->status); \
  isti_db *db = s->_db; \
  ASSERT_MEM(*v = calloc(1, sizeof(**v))); \
  CHECK(db->sql_one(db, s->_cond->sql, #CODES, READ, *v)); \
  EXIT; \
  if (status && v) {free(*v); *v = NULL;} \
  RETURN; \
}

#define ISTI_CORM_SELECT_COUNT_C(PREFIX) \
static int PREFIX ## _select_count(PREFIX ## _select *s, int *count) { \
  STATUS; \
  CHECK(s->_cond->status); \
  isti_db *db = s->_db; \
  CHECK(db->sql_count(db, s->_cond->sql, count)); \
  EXIT_STATUS; \
}

#define ISTI_CORM_SELECT_ANY_C(PREFIX, ARRAY, CODES, READ) \
static int PREFIX ## _select_any(PREFIX ## _select *s, ARRAY **a) { \
  STATUS; \
  CHECK(s->_cond->status); \
  isti_db *db = s->_db; \
  CHECK(ARRAY ## _alloc(a)); \
  CHECK(db->sql_any(db, s->_cond->sql, #CODES, READ, *a)); \
  EXIT_STATUS; \
}

#define ISTI_CORM_SELECT_FREE_C(PREFIX) \
int PREFIX ## _select_free(PREFIX ## _select *s, int previous) { \
  STATUS; \
  if (s) { \
    status = isti_cond_free(s->_cond, status); \
    free(s); \
  } \
  RETURN_PREVIOUS; \
}


// a delete has a bunch of standard types.  these assume that they will be
// defined using a struct called PREFIX_delete

#define ISTI_CORM_DELETES_T(PREFIX, PTR, ARRAY) \
typedef int PREFIX ## _delete_alloc_t(struct PREFIX ## _delete **, isti_db *); \
typedef int PREFIX ## _delete_free_t(struct PREFIX ## _delete *, int); \
typedef int PREFIX ## _delete_reset_t(struct PREFIX ## _delete *); \
typedef struct PREFIX ## _delete * PREFIX ## _delete_literal_t(struct PREFIX ## _delete *); \
typedef struct PREFIX ## _delete * PREFIX ## _delete_text_t(struct PREFIX ## _delete *, const char *, ...); \
typedef int PREFIX ## _delete_go_t(struct PREFIX ## _delete *);

#define ISTI_CORM_DELETE_ALLOC_H(PREFIX) \
int PREFIX ## _delete_alloc(struct PREFIX ## _delete **, isti_db *);

// and many of those are records inside that struct

#define ISTI_CORM_DELETES_R(PREFIX) \
PREFIX ## _delete_free_t *_free; \
PREFIX ## _delete_reset_t *_reset; \
PREFIX ## _delete_text_t *_; \
PREFIX ## _delete_go_t *_go;

// most of which are set on the struct

#define ISTI_CORM_DELETES_S(PARENT, PREFIX) \
PARENT ._ = PREFIX ## _delete_text; \
PARENT ._go = PREFIX ## _delete_go; \
PARENT ._reset = PREFIX ## _delete_reset; \
PARENT ._free = PREFIX ## _delete_free;

// and the implementations, which typically delegate to COND functions

#define ISTI_CORM_DELETE_TEXT_C(PREFIX) \
static PREFIX ## _delete *PREFIX ## _delete_text(PREFIX ## _delete *s, const char *template, ...) { \
  va_list ap; va_start(ap, template); \
  isti_cond_vappendf(s->_cond, template, ap); \
  va_end(ap); \
  return s; \
}

#define ISTI_CORM_DELETE_GO_C(PREFIX) \
static int PREFIX ## _delete_go(PREFIX ## _delete *s) { \
  STATUS; \
  CHECK(s->_cond->status); \
  isti_db *db = s->_db; \
  CHECK(db->sql(db, s->_cond->sql)); \
  EXIT_STATUS; \
}

#define ISTI_CORM_DELETE_FREE_C(PREFIX) \
int PREFIX ## _delete_free(PREFIX ## _delete *s, int previous) { \
  STATUS; \
  if (s) { \
    status = isti_cond_free(s->_cond, status); \
    free(s); \
  } \
  RETURN_PREVIOUS; \
}


// an insert has a bunch of standard types.  these assume that they will be
// defined using a struct called PREFIX_insert

#define ISTI_CORM_INSERTS_T(PREFIX, PTR, ARRAY) \
typedef int PREFIX ## _insert_alloc_t(struct PREFIX ## _insert **, isti_db *); \
typedef int PREFIX ## _insert_free_t(struct PREFIX ## _insert *, int); \
typedef int PREFIX ## _insert_reset_t(struct PREFIX ## _insert *); \
typedef struct PREFIX ## _insert * PREFIX ## _insert_key_t(struct PREFIX ## _insert *); \
typedef int PREFIX ## _insert_go_one_t(struct PREFIX ## _insert *, PTR *); \
typedef int PREFIX ## _insert_go_any_t(struct PREFIX ## _insert *, ARRAY *);

#define ISTI_CORM_INSERT_ALLOC_H(PREFIX) \
int PREFIX ## _insert_alloc(struct PREFIX ## _insert **, isti_db *);

// and many of those are records inside that struct

#define ISTI_CORM_INSERTS_R(PREFIX) \
PREFIX ## _insert_free_t *_free; \
PREFIX ## _insert_reset_t *_reset; \
PREFIX ## _insert_go_one_t *_go_one; \
PREFIX ## _insert_go_any_t *_go_any;

// most of which are set on the struct

#define ISTI_CORM_INSERTS_S(PARENT, PREFIX) \
PARENT ._go_one = PREFIX ## _insert_one; \
PARENT ._go_any = PREFIX ## _insert_any; \
PARENT ._reset = PREFIX ## _insert_reset; \
PARENT ._free = PREFIX ## _insert_free;

// and the implementations (for insert, most are auto-generated)

#define ISTI_CORM_INSERT_FREE_C(PREFIX) \
int PREFIX ## _insert_free(PREFIX ## _insert *s, int previous) { \
  STATUS; \
  if (s) { \
    status = isti_ins_free(s->_ins, status); \
    free(s); \
  } \
  RETURN_PREVIOUS; \
}

// also, delegate keys

#define ISTI_CORM_DELEGATE_KEY_C(STRUCT, NAME, TARGET) \
STRUCT *NAME(STRUCT *s) { \
  TARGET(s->_ins); return s; \
}


#endif
