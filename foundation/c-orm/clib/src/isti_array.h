
#ifndef ISTI_ARRAY_H_
#define ISTI_ARRAY_H_

#include <string.h>

#include "isti_mem.h"
#include "isti_flow.h"
#include "isti.h"



#define ISTI_ARRAY_STRUCT_T(NAME, TYPE, PTR) \
typedef struct NAME { \
  TYPE *PTR; \
  isti_mem n; \
} NAME


#define ISTI_ARRAY_FREE_T(NAME, ABBRV) typedef int NAME ## _free_t(NAME *ABBRV, int previous)
#define ISTI_ARRAY_FREE_H(NAME) NAME ## _free_t NAME ## _free
#define ISTI_ARRAY_FREE_R(NAME) NAME ## _free_t *free
#define ISTI_ARRAY_FREE_S(PREFIX, NAME) PREFIX .free = NAME ## _free

#define ISTI_ARRAY_FREE_C(NAME, ABBRV, TYPE, PTR, FREE) \
int NAME ## _free(NAME *ABBRV, int previous) { \
  STATUS; \
  if (ABBRV) { \
    status = isti_mem_free(&ABBRV->n, FREE, ABBRV->PTR, status); \
    free(ABBRV); \
  } \
  RETURN_PREVIOUS; \
}


#define ISTI_ARRAY_ALLOC_T(NAME, ABBRV) typedef int NAME ## _alloc_t(NAME **ABBRV)
#define ISTI_ARRAY_ALLOC_H(NAME) NAME ## _alloc_t NAME ## _alloc
#define ISTI_ARRAY_ALLOC_R(NAME) NAME ## _alloc_t *alloc
#define ISTI_ARRAY_ALLOC_S(PREFIX, NAME) PREFIX .alloc = NAME ## _alloc

#define ISTI_ARRAY_ALLOC_C(NAME, ABBRV, TYPE, PTR) \
int NAME ## _alloc(NAME **ABBRV) { \
  STATUS; \
  ASSERT_MEM(*ABBRV = calloc(1, sizeof(**ABBRV))); \
  EXIT_STATUS; \
}


#define ISTI_ARRAY_OWN_T(NAME, ABBRV, TYPE) typedef int NAME ## _own_t(NAME **ABBRV, TYPE *value, size_t size)
#define ISTI_ARRAY_OWN_H(NAME) NAME ## _own_t NAME ## _own
#define ISTI_ARRAY_OWN_R(NAME) NAME ## _own_t *own
#define ISTI_ARRAY_OWN_S(PREFIX, NAME) PREFIX .own = NAME ## _own

#define ISTI_ARRAY_OWN_C(NAME, ABBRV, TYPE, PTR) \
int NAME ## _own(NAME **ABBRV, TYPE *value, size_t size) { \
  STATUS; \
  ASSERT_MEM(*ABBRV = calloc(1, sizeof(**ABBRV))); \
  (*ABBRV)->PTR = value; \
  (*ABBRV)->n.used = size; \
  (*ABBRV)->n.available = size; \
  EXIT_STATUS; \
}


#define ISTI_ARRAY_RESET_T(NAME, ABBRV) typedef int NAME ## _reset_t(NAME *ABBRV)
#define ISTI_ARRAY_RESET_H(NAME) NAME ## _reset_t NAME ## _reset
#define ISTI_ARRAY_RESET_R(NAME) NAME ## _reset_t *reset
#define ISTI_ARRAY_RESET_S(PREFIX, NAME) PREFIX .reset = NAME ## _reset

#define ISTI_ARRAY_RESET_C(NAME, ABBRV, TYPE, PTR, FREE) \
int NAME ## _reset(NAME *ABBRV) { \
  STATUS; \
  CHECK(isti_mem_reset(&ABBRV->n, FREE, ABBRV->PTR, sizeof(*ABBRV->PTR))); \
  EXIT_STATUS; \
}


#define ISTI_ARRAY_ALLOW_T(NAME, ABBRV) typedef int NAME ## _allow_t(NAME *ABBRV, size_t n)
#define ISTI_ARRAY_ALLOW_H(NAME) NAME ## _allow_t NAME ## _allow
#define ISTI_ARRAY_ALLOW_R(NAME) NAME ## _allow_t *allow
#define ISTI_ARRAY_ALLOW_S(PREFIX, NAME) PREFIX .allow = NAME ## _allow

#define ISTI_ARRAY_ALLOW_C(NAME, ABBRV, TYPE, PTR) \
int NAME ## _allow(NAME *ABBRV, size_t n) { \
  STATUS; \
  ASSERT_MEM(ABBRV->PTR = isti_mem_allow(&ABBRV->n, ABBRV->PTR, n, sizeof(*ABBRV->PTR))); \
  EXIT_STATUS; \
}


#define ISTI_ARRAY_EXTEND_T(NAME, ABBRV) typedef int NAME ## _extend_t(NAME *ABBRV, size_t n)
#define ISTI_ARRAY_EXTEND_H(NAME) NAME ## _extend_t NAME ## _extend
#define ISTI_ARRAY_EXTEND_R(NAME) NAME ## _extend_t *extend
#define ISTI_ARRAY_EXTEND_S(PREFIX, NAME) PREFIX .extend = NAME ## _extend

#define ISTI_ARRAY_EXTEND_C(NAME, ABBRV, TYPE, PTR) \
int NAME ## _extend(NAME *ABBRV, size_t n) { \
  STATUS; \
  ASSERT_MEM(ABBRV->PTR = isti_mem_extend(&ABBRV->n, ABBRV->PTR, n, sizeof(*ABBRV->PTR))); \
  EXIT_STATUS; \
}


#define ISTI_ARRAY_INC_T(NAME, ABBRV, TYPE) typedef int NAME ## _inc_t(NAME *ABBRV, TYPE v)
#define ISTI_ARRAY_INC_H(NAME) NAME ## _inc_t NAME ## _inc
#define ISTI_ARRAY_INC_R(NAME) NAME ## _inc_t *inc
#define ISTI_ARRAY_INC_S(PREFIX, NAME) PREFIX .inc = NAME ## _inc

#define ISTI_ARRAY_INC_C(NAME, ABBRV, TYPE, PTR) \
int NAME ## _inc(NAME *ABBRV, TYPE v) { \
  STATUS; \
  CHECK(NAME ## _extend(ABBRV, 1)); \
  ABBRV->PTR[ABBRV->n.used++] = v; \
  EXIT_STATUS; \
}


#define ISTI_ARRAY_INCP_T(NAME, ABBRV, TYPE) typedef int NAME ## _incp_t(NAME *ABBRV, TYPE **v)
#define ISTI_ARRAY_INCP_H(NAME) NAME ## _incp_t NAME ## _incp
#define ISTI_ARRAY_INCP_R(NAME) NAME ## _incp_t *incp
#define ISTI_ARRAY_INCP_S(PREFIX, NAME) PREFIX .incp = NAME ## _incp

#define ISTI_ARRAY_INCP_C(NAME, ABBRV, TYPE, PTR) \
int NAME ## _incp(NAME *ABBRV, TYPE **v) { \
  STATUS; \
  CHECK(NAME ## _extend(ABBRV, 1)); \
  *v = &ABBRV->PTR[ABBRV->n.used++]; \
  EXIT_STATUS; \
}


#define ISTI_ARRAY_ADD_T(NAME, ABBRV, TYPE) typedef int NAME ## _add_t(NAME *ABBRV, TYPE *v, size_t n)
#define ISTI_ARRAY_ADD_H(NAME) NAME ## _add_t NAME ## _add
#define ISTI_ARRAY_ADD_R(NAME) NAME ## _add_t *add
#define ISTI_ARRAY_ADD_S(PREFIX, NAME) PREFIX .add = NAME ## _add

#define ISTI_ARRAY_ADD_C(NAME, ABBRV, TYPE, PTR) \
int NAME ## _add(NAME *ABBRV, TYPE *v, size_t n) { \
  STATUS; \
  CHECK(NAME ## _extend(ABBRV, n)); \
  memmove(&ABBRV->PTR[ABBRV->n.used], v, n * sizeof(*ABBRV->PTR)); \
  ABBRV->n.used += n; \
  EXIT_STATUS; \
}


#define ISTI_ARRAY_DISOWN_T(NAME, ABBRV, TYPE) typedef int NAME ## _disown_t(NAME *ABBRV, TYPE **v, size_t *n)
#define ISTI_ARRAY_DISOWN_H(NAME) NAME ## _disown_t NAME ## _disown
#define ISTI_ARRAY_DISOWN_R(NAME) NAME ## _disown_t *disown
#define ISTI_ARRAY_DISOWN_S(PREFIX, NAME) PREFIX .disown = NAME ## _disown

#define ISTI_ARRAY_DISOWN_C(NAME, ABBRV, TYPE, PTR, FREE) \
int NAME ## _disown(NAME *ABBRV, TYPE **v, size_t *n) { \
  STATUS; \
  *v = ABBRV->PTR; \
  if (n) *n = ABBRV->n.used; \
  ABBRV->PTR = NULL; \
  ABBRV->n.used = 0; \
  ABBRV->n.available = 0; \
  CHECK(isti_mem_reset(&ABBRV->n, FREE, ABBRV->PTR, sizeof(*ABBRV->PTR))); \
  EXIT_STATUS; \
}


#define ISTI_ARRAY_FNS_C(NAME, ABBRV, TYPE, PTR, FREE) \
ISTI_ARRAY_FREE_C(NAME, ABBRV, TYPE, PTR, FREE) \
ISTI_ARRAY_ALLOC_C(NAME, ABBRV, TYPE, PTR) \
ISTI_ARRAY_OWN_C(NAME, ABBRV, TYPE, PTR) \
ISTI_ARRAY_RESET_C(NAME, ABBRV, TYPE, PTR, FREE) \
ISTI_ARRAY_ALLOW_C(NAME, ABBRV, TYPE, PTR) \
ISTI_ARRAY_EXTEND_C(NAME, ABBRV, TYPE, PTR) \
ISTI_ARRAY_INC_C(NAME, ABBRV, TYPE, PTR) \
ISTI_ARRAY_INCP_C(NAME, ABBRV, TYPE, PTR) \
ISTI_ARRAY_ADD_C(NAME, ABBRV, TYPE, PTR) \
ISTI_ARRAY_DISOWN_C(NAME, ABBRV, TYPE, PTR, FREE)

#define ISTI_ARRAY_FNS_T(NAME, ABBRV, TYPE) \
ISTI_ARRAY_FREE_T(NAME, ABBRV); \
ISTI_ARRAY_ALLOC_T(NAME, ABBRV); \
ISTI_ARRAY_OWN_T(NAME, ABBRV, TYPE); \
ISTI_ARRAY_RESET_T(NAME, ABBRV); \
ISTI_ARRAY_ALLOW_T(NAME, ABBRV); \
ISTI_ARRAY_EXTEND_T(NAME, ABBRV); \
ISTI_ARRAY_INC_T(NAME, ABBRV, TYPE); \
ISTI_ARRAY_INCP_T(NAME, ABBRV, TYPE); \
ISTI_ARRAY_ADD_T(NAME, ABBRV, TYPE); \
ISTI_ARRAY_DISOWN_T(NAME, ABBRV, TYPE);

#define ISTI_ARRAY_FNS_H(NAME) \
ISTI_ARRAY_FREE_H(NAME); \
ISTI_ARRAY_ALLOC_H(NAME); \
ISTI_ARRAY_OWN_H(NAME); \
ISTI_ARRAY_RESET_H(NAME); \
ISTI_ARRAY_ALLOW_H(NAME); \
ISTI_ARRAY_EXTEND_H(NAME); \
ISTI_ARRAY_INC_H(NAME); \
ISTI_ARRAY_INCP_H(NAME); \
ISTI_ARRAY_ADD_H(NAME); \
ISTI_ARRAY_DISOWN_H(NAME);

#define ISTI_ARRAY_FNS_R(NAME) \
ISTI_ARRAY_FREE_R(NAME); \
ISTI_ARRAY_ALLOC_R(NAME); \
ISTI_ARRAY_OWN_R(NAME); \
ISTI_ARRAY_RESET_R(NAME); \
ISTI_ARRAY_ALLOW_R(NAME); \
ISTI_ARRAY_EXTEND_R(NAME); \
ISTI_ARRAY_INC_R(NAME); \
ISTI_ARRAY_INCP_R(NAME); \
ISTI_ARRAY_ADD_R(NAME); \
ISTI_ARRAY_DISOWN_R(NAME);

#define ISTI_ARRAY_FNS_S(PREFIX, NAME) \
ISTI_ARRAY_FREE_S(PREFIX, NAME), \
ISTI_ARRAY_ALLOC_S(PREFIX, NAME), \
ISTI_ARRAY_OWN_S(PREFIX, NAME), \
ISTI_ARRAY_RESET_S(PREFIX, NAME), \
ISTI_ARRAY_ALLOW_S(PREFIX, NAME), \
ISTI_ARRAY_EXTEND_S(PREFIX, NAME), \
ISTI_ARRAY_INC_S(PREFIX, NAME), \
ISTI_ARRAY_INCP_S(PREFIX, NAME), \
ISTI_ARRAY_ADD_S(PREFIX, NAME), \
ISTI_ARRAY_DISOWN_S(PREFIX, NAME)


// combine the above for a simple header and source file

#define ISTI_ARRAY_H(NAME, ABBRV, TYPE, PTR) \
ISTI_ARRAY_STRUCT_T(NAME, TYPE, PTR); \
ISTI_ARRAY_FNS_T(NAME, ABBRV, TYPE) \
ISTI_ARRAY_FNS_H(NAME)

#define ISTI_ARRAY_C(NAME, ABBRV, TYPE, PTR, FREE) \
ISTI_ARRAY_FNS_C(NAME, ABBRV, TYPE, PTR, FREE)


// allow for namespacing

#define ALIAS_ARRAY_AS(NAME, ALIAS) \
typedef struct ALIAS ## _fn { \
ISTI_ARRAY_FNS_R(NAME) \
} ALIAS ## _fn; \
static ALIAS ## _fn ALIAS = { \
ISTI_ARRAY_FNS_S(,NAME) \
};


// provided by this library

ISTI_ARRAY_H(isti_int_array, ints, int, i);
ISTI_ARRAY_H(isti_chars_array, chars, char *, c);

#endif
