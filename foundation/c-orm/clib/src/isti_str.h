
#ifndef ISTI_STR_H_
#define ISTI_STR_H_

/** @file

@brief Dynamic strings (interface).

Support for strings (char arrays) that tracks used and allocated
length, and can be extended as needed.  The internal representation is
null terminated.

Use via the ISTI_STR_AS() macro.  For example:

@code
ISTI_STR_AS(str)
...
  isti_str *s = NULL;
  STATUS;
  CHECK(str.str(&s, "a"));
  CHECK(str.append(s, "bc"));
  CHECK(strcmp(s->c, "abc"));
  ASSERT(s->n.used == 4, ERROR_CODE);  // includes zero padding
  EXIT;
  status = str.free(s, status);  // standard pattern for chaining return status
  RETURN;
...
@endcode

(The code above uses macros from @ref isti_flow.h;
the `n` member is @ref isti_mem from @ref isti_mem.h).

@see isti_str.c

*/

#include <stdarg.h>
#include <stdio.h>

#include "isti_array.h"

/// @brief The character array and metdata (`n.used` is the size of the string).
///
/// These are exposed directly to the user.  The intention is to support
/// *reading* data efficiently.  Modification should be done through the API.
ISTI_ARRAY_STRUCT_T(isti_str, char, c);

// The verbosity below is to support namespaced functions; it's regrettable,
// but checked at compile time and simplifies client use.

/// `previous` is the caller's status, used to chain status during exit.
ISTI_ARRAY_FREE_T(isti_str, str);
/// Release memory.
ISTI_ARRAY_FREE_H(isti_str);

ISTI_ARRAY_ALLOC_T(isti_str, str);
/// Allocate a new, empty string.
ISTI_ARRAY_ALLOC_H(isti_str);

ISTI_ARRAY_RESET_T(isti_str, str);
/// Re-allocate a string.
ISTI_ARRAY_RESET_H(isti_str);

ISTI_ARRAY_ALLOW_T(isti_str, str);
/// Guarantee space for extension.
ISTI_ARRAY_ALLOW_H(isti_str);

ISTI_ARRAY_EXTEND_T(isti_str, str);
/// Guarantee space for extension.
ISTI_ARRAY_EXTEND_H(isti_str);

typedef int isti_str_str_t(struct isti_str **str, const char *text);
/// Allocate a new string with the given contents.
isti_str_str_t isti_str_str;

typedef int isti_str_own_t(struct isti_str **str, char *text);
/// Allocate a new string with the given contents, which may be reallocated.
isti_str_own_t isti_str_own;

typedef int isti_str_strf_t(struct isti_str **str, const char *template, ...);
/// Allocate a new string with the given, formatted contents.
isti_str_strf_t isti_str_strf;

typedef int isti_str_append_t(struct isti_str *str, const char *text);
/// Append to the end of the string.
isti_str_append_t isti_str_append;

typedef int isti_str_appendf_t(struct isti_str *str, const char *template, ...);
/// Append to the end of the string with formatting.
isti_str_appendf_t isti_str_appendf;

typedef int isti_str_vappendf_t(struct isti_str *str, const char *template, va_list);
/// Append to the end of the string with formatting.
isti_str_vappendf_t isti_str_vappendf;

typedef int isti_str_concatn_t(struct isti_str *str, ...);
/// Append to the end of the string until NULL.
isti_str_concatn_t isti_str_concatn;

typedef int isti_str_vconcatn_t(struct isti_str *str, va_list);
/// Append to the end of the string until NULL.
isti_str_vconcatn_t isti_str_vconcatn;

typedef int isti_str_joinn_t(struct isti_str *str, const char *sep, ...);
/// Append to the end of the string, with separator, until NULL.
isti_str_joinn_t isti_str_joinn;

typedef int isti_str_vjoinn_t(struct isti_str *str, const char *sep, va_list);
/// Append to the end of the string, with separator,  until NULL.
isti_str_vjoinn_t isti_str_vjoinn;

typedef int isti_str_inc_t(struct isti_str *str, const char c);
/// Extend the string by a single character.
isti_str_inc_t isti_str_inc;

typedef int isti_str_split_t(struct isti_chars_array **chars, const char *text, const char *sep, int max);
isti_str_split_t isti_str_split;

typedef int isti_str_disown_t(struct isti_str *str, char **text);
isti_str_disown_t isti_str_disown;

typedef char *isti_str_char_dup_t(const char *text);
/// @brief A utility function for duplicating `char*` strings.
/// Caller must test for non-null allocation.
isti_str_char_dup_t isti_str_char_dup;

/// @brief The namespace returned by ISTI_STR_AS().
/// This provide the "variables" as fields with shorter names.
typedef struct isti_str_fn {
  isti_str_free_t *free;
  isti_str_alloc_t *alloc;
  isti_str_reset_t *reset;
  isti_str_allow_t *allow;
  isti_str_extend_t *extend;
  isti_str_str_t *str;
  isti_str_own_t *own;
  isti_str_strf_t *strf;
  isti_str_append_t *append;
  isti_str_appendf_t *appendf;
  isti_str_vappendf_t *vappendf;
  isti_str_concatn_t *concatn;
  isti_str_vconcatn_t *vconcatn;
  isti_str_joinn_t *joinn;
  isti_str_vjoinn_t *vjoinn;
  isti_str_inc_t *inc;
  isti_str_disown_t *disown;

  isti_str_split_t *split;

  isti_str_char_dup_t *char_dup;
} isti_str_fn;

/// Use this macro to define a namespace for the routines here.
#define ISTI_STR_AS(NAME) static isti_str_fn NAME = { \
  .free = isti_str_free, \
  .alloc = isti_str_alloc, \
  .reset = isti_str_reset, \
  .allow = isti_str_allow, \
  .extend = isti_str_extend, \
  .str = isti_str_str, \
  .own = isti_str_own, \
  .strf = isti_str_strf, \
  .append = isti_str_append, \
  .appendf = isti_str_appendf, \
  .vappendf = isti_str_vappendf, \
  .concatn = isti_str_concatn, \
  .vconcatn = isti_str_vconcatn, \
  .joinn = isti_str_joinn, \
  .vjoinn = isti_str_vjoinn, \
  .inc = isti_str_inc, \
  .disown = isti_str_disown, \
  \
  .split = isti_str_split, \
  \
  .char_dup = isti_str_char_dup \
};

#endif
