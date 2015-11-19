
#include <stdio.h>
#include <check.h>

#include "isti.h"
#include "isti_flow.h"
#include "isti_sql.h"

ISTI_SQL_AS(sql)

// Test a single select command with two values.
START_TEST(test_select)
{
  isti_sql *q = NULL;
  fail_if(sql.alloc(&q), "Could not allocate q");
  fail_if(!q, "q null after allocation");
  fail_if(sql.appendf(q, "select * from foo where a=%s and b=%d", "foo", 42),
          "could not append");
  fail_if(strcmp(q->template->c, "select * from foo where a=? and b=?"),
          q->template->c);
  fail_if(q->n_values.used != 2, 
          "unexpected n_values.used: %d", q->n_values.used);
  fail_if(strcmp(q->values[0].value, "foo"), q->values[0].value);
  fail_if(q->values[0].type != 's', "bad type: %c", q->values[0].type);
  fail_if(*((int*)q->values[1].value) != 42, 
          "bad int: %d", *((int*)q->values[1].value));
  fail_if(q->values[1].type != 'd', "bad type: %c", q->values[1].type);
  char *c;
  fail_if(sql.unsafe(q, &c));
  fail_if(strcmp(c, "-- select * from foo where a='foo' and b=42"), c);
  fail_if(sql.free(q, ISTI_OK), "Could not free q");
}
END_TEST

START_TEST(test_select_example)
{
  isti_sql *q = NULL;
  fail_if(sql.sqlf(&q, "select * from foo where a=%s and b=%d", "foo", 42), "sql error");
  fail_if(strcmp(q->template->c, "select * from foo where a=? and b=?"), "unexpected sql");
  fail_if(q->n_values.used != 2, "unexpected number used");
  fail_if(q->values[0].type != 's', "unexpected type");
  fail_if(strcmp((char*)q->values[0].value, "foo"), "unexpected value");
  fail_if(q->values[1].type != 'd', "unexpected type");
  fail_if(*((int*)q->values[1].value) != 42, "unexpected value");
}
END_TEST

START_TEST(test_insert)
{
  isti_sql *q = NULL;
  fail_if(sql.alloc(&q), "Could not allocate q");
  fail_if(!q, "q null after allocation");
  fail_if(sql.appendf(q, "insert into foo (a, b) values (%s, %d)", "foo", 42),
          "could not append");
  fail_if(strcmp(q->template->c, "insert into foo (a, b) values (?, ?)"),
          q->template->c);
  fail_if(q->n_values.used != 2,
          "unexpected n_values.used: %d", q->n_values.used);
  fail_if(strcmp(q->values[0].value, "foo"), q->values[0].value);
  fail_if(q->values[0].type != 's', "bad type: %c", q->values[0].type);
  fail_if(*((int*)q->values[1].value) != 42,
          "bad int: %d", *((int*)q->values[1].value));
  fail_if(q->values[1].type != 'd', "bad type: %c", q->values[1].type);
  char *c;
  fail_if(sql.unsafe(q, &c));
  fail_if(strcmp(c, "-- insert into foo (a, b) values ('foo', 42)"), c);
  fail_if(sql.free(q, ISTI_OK), "Could not free q");
}
END_TEST

Suite* sql_suite (void) {
  Suite *suite = suite_create("isti_sql");
  TCase *tcase = tcase_create("case");
  tcase_add_test(tcase, test_select);
  tcase_add_test(tcase, test_select_example);
  tcase_add_test(tcase, test_insert);
  suite_add_tcase(suite, tcase);
  return suite;
}

int main (int argc, char *argv[]) {
  int number_failed;
  Suite *suite = sql_suite();
  SRunner *runner = srunner_create(suite);
  srunner_set_xml(runner, "check-isti_sql.xml");
  srunner_run_all(runner, CK_NORMAL);
  number_failed = srunner_ntests_failed(runner);
  srunner_free(runner);
  return number_failed;
}
