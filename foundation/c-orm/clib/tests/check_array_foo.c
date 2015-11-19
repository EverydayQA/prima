
#include <check.h>
#include <stdio.h>

#include "isti.h"
#include "isti_flow.h"

#include "foo.corm.h"

CORM_FOO_AS(corm_foo)

void assert_foo(foo *f, int id, int bar, const char *baz) {
  fail_if(!f, "null");
  fail_if(f->id != id, "bad id %d", f->id);
  fail_if(f->bar != bar, "bad bar %d", f->bar);
  fail_if(!f->baz ,"null baz");
  fail_if(!baz ,"null baz");
  fail_if(baz && f && f->baz && strcmp(f->baz, baz) ,"bad baz %s", f->baz);
}

START_TEST(test_array)
{
  corm_foo_array *a = NULL;
  fail_if(corm_foo.array.alloc(&a), "cannot alloc a");
  foo *f = calloc(1, sizeof(*f));
  f->id = 1;
  fail_if(corm_foo.array.inc(a, f), "cannot inc a");
  f = calloc(1, sizeof(*f));
  f->id = 2;
  fail_if(corm_foo.array.inc(a, f), "cannot inc a");
  fail_if(a->n.used != 2, "bad used %d", a->n.used);
  for (int i = 0; i < a->n.used; ++i) {
    fail_if(a->foo[i]->id != i+1, "bad id at %d %d", i, a->foo[i]->id);
  }
  fail_if(corm_foo.array.free(a, 0), "cannot free a");
}
END_TEST


// Everything below is boilerplate for the tests.

Suite* sqlite_suite (void) {
  Suite *suite = suite_create("foo");
  TCase *tcase = tcase_create("case");
  tcase_add_test(tcase, test_array);
  suite_add_tcase(suite, tcase);
  return suite;
}

int main (int argc, char *argv[]) {
  int number_failed;
  Suite *suite = sqlite_suite();
  SRunner *runner = srunner_create(suite);
  srunner_set_xml(runner, "check-array_foo.xml");
  srunner_run_all(runner, CK_NORMAL);
  number_failed = srunner_ntests_failed(runner);
  srunner_free(runner);
  return number_failed;
}
