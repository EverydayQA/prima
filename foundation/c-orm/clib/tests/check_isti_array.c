
#include <stdio.h>
#include <check.h>

#include "isti.h"
#include "isti_flow.h"
#include "isti_array.h"
#include "isti_str.h"

ISTI_STR_AS(str)

ISTI_ARRAY_H(test_chars, chars, char, c)
ISTI_ARRAY_C(test_chars, chars, char, c, isti_free1)

START_TEST(test_char)
{
  test_chars *c = NULL;
  fail_if(test_chars_alloc(&c), "failed to alloc");
  if (c) fail_if(test_chars_free(c, 0), "failed to free");
}
END_TEST

ALIAS_ARRAY_AS(isti_int_array, ints)

START_TEST(test_int)
{
  isti_int_array *i = NULL;
  fail_if(ints.alloc(&i), "failed to alloc");
  if (i) fail_if(ints.free(i, 0), "failed to free");
}
END_TEST

ALIAS_ARRAY_AS(isti_chars_array, chars)

START_TEST(test_inbuilt_chars)
{
  isti_chars_array *c = NULL;
  fail_if(chars.alloc(&c), "failed to alloc");
  for (int i = 0; i < 5; ++i) {
    isti_str *s = NULL;
    fail_if(isti_str_strf(&s, "%d", i), "cannot create string");
    fail_if(chars.inc(c, str.char_dup(s->c)), "cannot add string");
    fail_if(strcmp(c->c[i], s->c), "bad string stored: %s", c->c[i]);
    fail_if(str.free(s, 0), "cannot free string");
  }
  fail_if(c->n.used != 5, "unexpected length %d", c->n.used);
  fail_if(chars.free(c, 0), "cannot free chars");
}
END_TEST


Suite* array_suite (void) {
  Suite *suite = suite_create("isti_array");
  TCase *tcase = tcase_create("case");
  tcase_add_test(tcase, test_char);
  tcase_add_test(tcase, test_int);
  tcase_add_test(tcase, test_inbuilt_chars);
  suite_add_tcase(suite, tcase);
  return suite;
}

int main (int argc, char *argv[]) {
  int number_failed;
  Suite *suite = array_suite();
  SRunner *runner = srunner_create(suite);
  srunner_set_xml(runner, "check-isti_array.xml");
  srunner_run_all(runner, CK_NORMAL);
  number_failed = srunner_ntests_failed(runner);
  srunner_free(runner);
  return number_failed;
}
