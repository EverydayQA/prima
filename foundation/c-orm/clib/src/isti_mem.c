
#include "isti.h"
#include "isti_flow.h"

#include "isti_mem.h"

/// @file
/// @brief Dynamic memory, with amortized O(n) cost (implementation).
///
/// See header for documentation. @see isti_mem.h

// no error handling here - callers assert the value
void *isti_mem_allow(isti_mem *n, void *data, size_t minimum, size_t size) {
  if (minimum <= n->available) return data;
  if (n->available) {
    minimum = ISTI_MAX(minimum, (size_t)(1.5 * (double)n->available));
    data = realloc(data, size * minimum);
  } else {
    minimum = ISTI_MAX(minimum, 2);
    data = calloc(minimum, size);
  }
  n->available = minimum;
  return data;
}

void *isti_mem_inc(isti_mem *n, void *data, size_t size) {
  return isti_mem_allow(n, data, n->used + 1, size);
}

void *isti_mem_extend(isti_mem *n, void *data, size_t delta, size_t size) {
  return isti_mem_allow(n, data, n->used + delta, size);
}

int isti_mem_free(isti_mem *n, isti_free_t *free, void *data, int previous) {
  STATUS;
  if (n->available) {
    status = free(data, n->used, status);
    n->used = 0;
    n->available = 0;
  }
  RETURN;
}

int isti_free1(void *data, size_t n, int previous) {
  free(data);
  return previous;
}

int isti_mem_reset(isti_mem *n, isti_free_t *free, void *data, size_t size) {
  STATUS;
  if (n->available) CHECK(free(data, n->used, status));
  n->used = 0;
  n->available = 0;
  EXIT_STATUS;
}
