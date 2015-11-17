
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/// @file
/// @brief Dynamic strings (implementation).
///
/// See header for documentation. @see isti_str.h

#include "isti.h"
#include "isti_flow.h"

#include "isti_str.h"

ISTI_MEM_AS(mem)

ISTI_ARRAY_FREE_C(isti_str, str, char, c, isti_free1)
ISTI_ARRAY_ALLOW_C(isti_str, str, char, c)
ISTI_ARRAY_EXTEND_C(isti_str, str, char, c)
ALIAS_ARRAY_AS(isti_chars_array, isti_chars)

int isti_str_reset(isti_str *str) {
  STATUS;
  CHECK(mem.reset(&str->n, isti_free1, str->c, sizeof(*str->c)));
  CHECK(isti_str_allow(str, 2));
  str->c[0] = '\0';
  str->n.used = 1;
  EXIT_STATUS;
}

int isti_str_own(isti_str **s, char *text) {
  STATUS;
  ASSERT_MEM(*s = calloc(1, sizeof(**s)));
  (*s)->c = text;
  (*s)->n.used = strlen(text) + 1;
  (*s)->n.available = (*s)->n.used;
  EXIT_STATUS;
}

int isti_str_disown(isti_str *s, char **text) {
  STATUS;
  *text = s->c;
  s->c = NULL;
  s->n.used = 0;
  s->n.available = 0;
  CHECK(isti_str_allow(s, 2));
  s->c[0] = '\0';
  EXIT_STATUS;
}

int isti_str_vappendf(isti_str *s, const char *template, va_list ap) {
  STATUS;
  va_list copy;
  va_copy(copy, ap);
  char *start = s->c;
  // if we have any string at all, drop trailing null
  if (s->n.used) s->n.used--;
  if (start) start += s->n.used;
  size_t capacity = s->n.available - s->n.used;
  int used = vsnprintf(start, capacity, template, ap);
  ASSERT(used >= 0, ISTI_ERR_STR, "Error for %s", template);
  size_t sused = (size_t)used;
  if (used >= capacity) {
    CHECK(isti_str_extend(s, sused + 1));
    used = vsnprintf(s->c + s->n.used, s->n.available - s->n.used, template, copy);
    ASSERT(used >= 0, ISTI_ERR_STR, "Error for %s", template);
    s->n.used += (size_t)used;
  } else {
    s->n.used += sused;
  }
  s->n.used++;
  EXIT;
  va_end(copy);
  RETURN;
}

int isti_str_strf(isti_str **s, const char *template, ...) {
  STATUS;
  va_list ap;
  va_start(ap, template);
  ASSERT_MEM(*s = calloc(1, sizeof(**s)));
  CHECK(isti_str_vappendf(*s, template, ap));
  EXIT;
  va_end(ap);
  RETURN;
}

int isti_str_str(isti_str **s, const char *text) {
  return isti_str_strf(s, "%s", text);
}

// this is not quite the same as appendf with no varags because the
// escape character % is treated differently.
int isti_str_append(isti_str *s, const char *text) {
  return isti_str_appendf(s, "%s", text);
}

int isti_str_appendf(isti_str *s, const char *template, ...) {
  STATUS;
  va_list ap;
  va_start(ap, template);
  CHECK(isti_str_vappendf(s, template, ap));
  EXIT;
  va_end(ap);
  RETURN;
}

// write alloc in terms of str (rather than vice-versa) because we want an
// empty string to be null-terminated.
int isti_str_alloc(isti_str **s) {
  return isti_str_str(s, "");
}

int isti_str_vconcatn(isti_str *s, va_list ap) {
  STATUS;
  for (;;) {
    char *word = va_arg(ap, char*);
    if (! word) break;
    CHECK(isti_str_append(s, word));
  }
  EXIT_STATUS;
}

int isti_str_concatn(isti_str *s, ...) {
  STATUS;
  va_list(ap);
  va_start(ap, s);
  CHECK(isti_str_vconcatn(s, ap));
  EXIT;
  va_end(ap);
  RETURN;
}

int isti_str_vjoinn(isti_str *s, const char *sep, va_list ap) {
  STATUS;
  for (int first = 1;; first = 0) {
    char *word = va_arg(ap, char*);
    if (! word) break;
    if (! first) CHECK(isti_str_append(s, sep));
    CHECK(isti_str_append(s, word));
  }
  EXIT_STATUS;
}

int isti_str_joinn(isti_str *s, const char *sep, ...) {
  STATUS;
  va_list(ap);
  va_start(ap, sep);
  CHECK(isti_str_vjoinn(s, sep, ap));
  EXIT;
  va_end(ap);
  RETURN;
}

// this is for efficiency in callers that incrementally construct a string.
int isti_str_inc(isti_str *s, char c) {
  STATUS;
  CHECK(isti_str_extend(s, 1));
  // if we have any string at all, then we also have a trailing null, which
  // we must drop before appending
  if (s->n.used) s->n.used--;
  s->c[s->n.used++] = c;
  s->c[s->n.used++] = '\0';
  EXIT_STATUS;
}

int isti_str_split(isti_chars_array **chars, const char *text, const char *sep, int max) {
  STATUS;
  isti_str *line = NULL;
  CHECK(isti_chars.alloc(chars));
  CHECK(isti_str_alloc(&line));
  const char *p = text;
  while (*p && (max < 0 || (*chars)->n.used < max)) {
    while (*p && strchr(sep, *p)) p++;
    if (*p) {
      while (*p && !strchr(sep, *p)) isti_str_inc(line, *p++);
      char *word;
      CHECK(isti_str_disown(line, &word));
      CHECK(isti_chars.inc(*chars, word));
    }
  }
  EXIT;
  if (line) status = isti_str_free(line, status);
  RETURN;
}

char *isti_str_char_dup(const char *src) {
  char *dest = calloc(strlen(src)+1, sizeof(*dest));
  if (dest) strcpy(dest, src);
  return dest;
}
