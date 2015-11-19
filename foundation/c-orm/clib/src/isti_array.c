

#include "isti_array.h"


ISTI_ARRAY_C(isti_int_array, ints, int, i, isti_free1)

ISTI_MEM_FREE2(isti_chars_free2, char)
ISTI_ARRAY_C(isti_chars_array, chars, char *, c, isti_chars_free2)

