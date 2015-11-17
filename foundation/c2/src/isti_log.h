
#ifndef ISTI_LOG_H_
#define ISTI_LOG_H_

#include <stdbool.h>
#include <stdarg.h>
#include <stdio.h>

FILE *ist_log_setf(FILE *stream);

bool isti_log_set(bool on);

void isti_log(const char *template, ...);

#define ISTI_LOG(...) do {isti_log("%s:%d ", __FILE__, __LINE__); isti_log(__VA_ARGS__);} while(0)

#endif
