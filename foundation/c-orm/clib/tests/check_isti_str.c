
#include <stdio.h>
#include <check.h>

#include "isti.h"
#include "isti_str.h"
#include "isti_array.h"

ISTI_STR_AS(str)

// A very basic test of memory use.
START_TEST(test_str)
{
  isti_str *s = NULL;
  fail_if(str.alloc(&s), "could not allocate s");
  fail_if(!s, "s null after allocation");
  fail_if(str.free(s, ISTI_OK), "could not free s");
  fail_if(str.str(&s, "foo"), "could not create s");
  fail_if(!s, "s null after creation");
  fail_if(str.free(s, ISTI_OK), "could not free s");
}
END_TEST

START_TEST(test_append)
{
  isti_str *s = NULL;
  fail_if(str.str(&s, "a"), "could not allocate s");
  fail_if(!s, "s null after allocation");
  fail_if(str.append(s, "bc"), "could not append bc");
  fail_if(strcmp(s->c, "abc"), "%s != 'abc'", s->c);
  fail_if(s->n.used != 4, "wrong length: %d", s->n.used);
  fail_if(str.free(s, ISTI_OK), "could not free s");
}
END_TEST

START_TEST(test_split)
{
  isti_chars_array *c = NULL;
  fail_if(str.split(&c, " one  two   three  ", " ", -1), "cannot split string");
  fail_if(c->n.used != 3, "wrong number of words");
  fail_if(strcmp(c->c[1], "two"), "unexpected second word");
  fail_if(isti_chars_array_free(c, 0), "cannot free chars");
  fail_if(str.split(&c, " one  two   three  ", " ", 2), "cannot split string");
  fail_if(c->n.used != 2, "wrong number of words");
  fail_if(strcmp(c->c[1], "two"), "unexpected second word");
  fail_if(isti_chars_array_free(c, 0), "cannot free chars");
  fail_if(str.split(&c, " one\ttwo  \t three  ", " \t", -1), "cannot split string");
  fail_if(c->n.used != 3, "wrong number of words");
  fail_if(strcmp(c->c[1], "two"), "unexpected second word");
  fail_if(isti_chars_array_free(c, 0), "cannot free chars");
}
END_TEST

Suite* str_suite (void) {
  Suite *suite = suite_create("isti_str");
  TCase *tcase = tcase_create("case");
  tcase_add_test(tcase, test_str);
  tcase_add_test(tcase, test_append);
  tcase_add_test(tcase, test_split);
  suite_add_tcase(suite, tcase);
  return suite;
}

int main (int argc, char *argv[]) {
  int number_failed;
  Suite *suite = str_suite();
  SRunner *runner = srunner_create(suite);
  srunner_set_xml(runner, "check-isti_str.xml");
  srunner_run_all(runner, CK_NORMAL);
  number_failed = srunner_ntests_failed(runner);
  srunner_free(runner);
  return number_failed;
}
