
#ifndef ISTI_MEM_H_
#define ISTI_MEM_H_

#include<stdlib.h>

/** @file

@brief Dynamic memory, with amortized O(n) cost (interface).

These routines manage memory for the `void *data` pointer, allocating
memory in `size` byte chunks, in geometric progression (to give O(n)
amortized cost on insertion).  The metadata for the memory management
is stored in `isti_mem *n`.

Use via the ISTI_MEM_AS() macro.  For example:

@code
ISTI_MEM_AS(mem)

int isti_str_allow(isti_str *s, char *chars) {
  STATUS;
  ASSERT(s->c = mem.extend(s->c, strlen(chars)+1, sizeof(*s->c), &s->n),
         ISTI_ERR_MEM);
  EXIT_STATUS;
}
@endcode

@see isti_mem.c

*/


/// @brief The information needed to manage the memory, except the pointer
/// itself (which will be part of some parent struct).
typedef struct isti_mem {
  /// The number of entries occupied.
  size_t used;
  /// The number of entries allocated.
  size_t available;
} isti_mem;

typedef int isti_free_t(void * data, size_t n, int previous);
isti_free_t isti_free1;

typedef void *isti_mem_allow_t(isti_mem *mem, void *data, size_t minimum, size_t size);
/// Ensure that we have allocated space for at least `minimum` entries.
isti_mem_allow_t isti_mem_allow;

typedef void *isti_mem_inc_t(isti_mem *mem, void *data, size_t size);
/// Ensure that we can add at least one more entry.
isti_mem_inc_t isti_mem_inc;

typedef void *isti_mem_extend_t(isti_mem *mem, void *data, size_t delta, size_t size);
/// Ensure that we can add at least `delta` more entries.
isti_mem_extend_t isti_mem_extend;

/// `previous` is the caller's status, used to chain status during exit.
typedef int isti_mem_free_t(isti_mem *mem, isti_free_t *free, void *data, int previous);
/// Release memory.  The mem structure itself is not freed because it
/// is likely a part of a containing structure,
isti_mem_free_t isti_mem_free;

typedef int isti_mem_reset_t(isti_mem *, isti_free_t *free, void *data, size_t size);
isti_mem_reset_t isti_mem_reset;

/// @brief The namespace returned by ISTI_MEM_AS().
/// This provide the "variables" as fields with shorter names.
typedef struct isti_mem_fn {
  isti_mem_allow_t *allow;
  isti_mem_inc_t *inc;
  isti_mem_extend_t *extend;
  isti_mem_free_t *free;
  isti_mem_reset_t *reset;
} isti_mem_fn;

/// Use this macro to define a namespace for the routines here.
#define ISTI_MEM_AS(NAME) static isti_mem_fn NAME = { \
    .allow = isti_mem_allow, \
    .inc = isti_mem_inc, \
    .extend = isti_mem_extend, \
    .free = isti_mem_free, \
    .reset = isti_mem_reset \
  };

#define ISTI_MEM_FREE2(NAME, TYPE) \
int NAME(void *data, size_t n, int previous) { \
  TYPE **p = (TYPE **)data; \
  int i; \
  for (i = 0; i < n; i++) free(*p++); \
  free(data); \
  return previous; \
}

#endif
