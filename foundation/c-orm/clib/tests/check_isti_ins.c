
#include <stdio.h>
#include <check.h>

#include "isti.h"
#include "isti_flow.h"
#include "isti_sql.h"
#include "isti_ins.h"

ISTI_INS_AS(ins)
ISTI_SQL_AS(sql)

START_TEST(test_no_key)
{
  isti_ins *i = NULL;
  char *q = NULL;

  fail_if(ins.alloc(&i), "cannot alloc ins");

  fail_if(i->table(i, "foo")->status, "cannot define table");
  fail_if(sql.unsafe(i->sql, &q), "cannot generate sql");
  fail_if(strcmp(q, "-- insert into \"foo\" "), "%s", q);
  free(q);
  fail_if(i->columns(i, "id=%d, bar=%d, baz=%s")->status, "cannot define columns");
  fail_if(sql.unsafe(i->sql, &q), "cannot generate sql");
  fail_if(strcmp(q, "-- insert into \"foo\" (\"id\",\"bar\",\"baz\""), "%s", q);
  free(q);
  fail_if(i->values(i, 1, 2, "foo")->status, "cannot add values");
  fail_if(sql.unsafe(i->sql, &q), "cannot generate sql");
  fail_if(strcmp(q, "-- insert into \"foo\" (\"id\",\"bar\",\"baz\") values (1,2,'foo')"), "%s", q);
  free(q);

  fail_if(ins.reset(i), "cannot reset i");
  fail_if(i->table(i, "foo")->status, "cannot define table");
  fail_if(i->columns(i, "id=%d, bar=%d, baz=%s")->status, "cannot define columns");
  fail_if(i->d_value(i, 1)->status, "cannot add value");
  fail_if(i->d_value(i, 2)->status, "cannot add value");
  fail_if(i->s_value(i, "foo")->status, "cannot add value");
  fail_if(sql.unsafe(i->sql, &q), "cannot generate sql");
  fail_if(strcmp(q, "-- insert into \"foo\" (\"id\",\"bar\",\"baz\") values (1,2,'foo')"), "%s", q);
  free(q);

  fail_if(ins.reset(i), "cannot reset i");
  fail_if(i->table(i, "foo")->status, "cannot define table");
  fail_if(i->columns(i, "id=%d, bar=%d, baz=%s")->status, "cannot define columns");
  fail_if(i->values(i, 1, 2, "foo")->status, "cannot add values");
  fail_if(i->values(i, 3, 4, "bar")->status, "cannot add values");
  fail_if(sql.unsafe(i->sql, &q), "cannot generate sql");
  fail_if(strcmp(q, "-- insert into \"foo\" (\"id\",\"bar\",\"baz\") values (1,2,'foo'), (3,4,'bar')"), "%s", q);
  free(q);

  if (i) fail_if(ins.free(i, 0), "cannot free i");
}
END_TEST

START_TEST(test_key)
{
  isti_ins *i = NULL;
  char *q = NULL;

  fail_if(ins.alloc(&i), "cannot alloc ins");

  fail_if(i->table(i, "foo")->status, "cannot define table");
  fail_if(i->columns(i, "id=%d, bar=%d, baz=%s")->status, "cannot define columns");
  fail_if(i->key(i, "id")->status, "cannot define key");
  fail_if(i->values(i, 1, 2, "foo")->status, "cannot add values");
  fail_if(sql.unsafe(i->sql, &q), "cannot generate sql");
  fail_if(strcmp(q, "-- insert into \"foo\" (\"id\",\"bar\",\"baz\") values (NULL,2,'foo')"), "%s", q);
  free(q);

  fail_if(ins.reset(i), "cannot reset i");
  fail_if(i->table(i, "foo")->status, "cannot define table");
  fail_if(i->columns(i, "id=KEY, bar=%d, baz=%s")->status, "cannot define columns");
  fail_if(i->values(i, 1, 2, "foo")->status, "cannot add values");
  fail_if(sql.unsafe(i->sql, &q), "cannot generate sql");
  fail_if(strcmp(q, "-- insert into \"foo\" (\"id\",\"bar\",\"baz\") values (NULL,2,'foo')"), "%s", q);
  free(q);

  if (i) fail_if(ins.free(i, 0), "cannot free i");
}
END_TEST


Suite* sql_suite (void) {
  Suite *suite = suite_create("isti_ins");
  TCase *tcase = tcase_create("case");
  tcase_add_test(tcase, test_no_key);
  tcase_add_test(tcase, test_key);
  suite_add_tcase(suite, tcase);
  return suite;
}

int main (int argc, char *argv[]) {
  int number_failed;
  Suite *suite = sql_suite();
  SRunner *runner = srunner_create(suite);
  srunner_set_xml(runner, "check-isti_ins.xml");
  srunner_run_all(runner, CK_NORMAL);
  number_failed = srunner_ntests_failed(runner);
  srunner_free(runner);
  return number_failed;
}
