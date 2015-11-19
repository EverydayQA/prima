
#include <stdio.h>
#include <stdbool.h>

#include "isti_log.h"


static FILE *out = NULL;
static bool on = true;


static void init() {
  if (! out) out = stderr;
}


FILE *isti_log_setf(FILE *stream) {
  init();
  FILE *previous = out;
  out = stream;
  return previous;
}


bool isti_log_set(bool flag) {
  init();
  bool previous = on;
  on = flag;
  return previous;
}


void isti_log(const char *template, ...) {
  if (on) {
    init();
    va_list(ap);
    va_start(ap, template);
    vfprintf(out, template, ap);
    fflush(out); // in case we forget the trailing linefeed
    va_end(ap);
  }
}
