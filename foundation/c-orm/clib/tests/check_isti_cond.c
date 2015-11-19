
#include <stdio.h>
#include <check.h>

#include "isti.h"
#include "isti_flow.h"
#include "isti_db.h"
#include "isti_sqlite.h"
#include "isti_sql.h"
#include "isti_cond.h"

ISTI_COND_AS(cond)
ISTI_SQL_AS(sql)

START_TEST(test_eq)
{
  isti_cond *c = NULL;
  char *q = NULL;

  fail_if(cond.alloc(&c), "cannot alloc cond");

  fail_if(c->delete(c)->from(c, "mytable")->_s(c, "foo", "=", "bar")->status, "cannot append to c");
  fail_if(sql.unsafe(c->sql, &q), "cannot generate sql");
  fail_if(strcmp(q, "--  delete  from mytable  where  foo = 'bar' "), "'%s'", q);
  free(q);
  if (c) fail_if(cond.free(c, 0), "cannot free c");
}
END_TEST

START_TEST(test_in)
{
  isti_cond *c = NULL;
  char *q = NULL;
  int i[3] = {1, 2, 3};

  fail_if(cond.alloc(&c), "cannot alloc cond");

  fail_if(c->selectn(c, "poop", "a", "doop", NULL)->from(c, "mytable")->_d_(c, "foo", "in", i, 3)->status, "cannot append to c");
  fail_if(sql.unsafe(c->sql, &q), "cannot generate sql");
  fail_if(strcmp(q, "-- select poop,a,doop from mytable  where  foo in (1,2,3) "), "'%s'", q);
  free(q);
  if (c) fail_if(cond.free(c, 0), "cannot free c");
}
END_TEST


Suite* cond_suite (void) {
  Suite *suite = suite_create("isti_cond");
  TCase *tcase = tcase_create("case");
  tcase_add_test(tcase, test_eq);
  tcase_add_test(tcase, test_in);
  suite_add_tcase(suite, tcase);
  return suite;
}

int main (int argc, char *argv[]) {
  int number_failed;
  Suite *suite = cond_suite();
  SRunner *runner = srunner_create(suite);
  srunner_set_xml(runner, "check-isti_cond.xml");
  srunner_run_all(runner, CK_NORMAL);
  number_failed = srunner_ntests_failed(runner);
  srunner_free(runner);
  return number_failed;
}
