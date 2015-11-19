
#include <stdio.h>
#include <check.h>

#include "isti.h"
#include "isti_sql.h"
#include "isti_odbc.h"

#include "foo.h"
#include "foo.corm.h"

ISTI_SQL_AS(sql)
ISTI_ODBC_AS(odbc)
CORM_FOO_AS(corm_foo)

// http://stackoverflow.com/questions/195975/how-to-make-a-char-string-from-a-c-macros-value
#define QUOTE(name) #name
#define STR(macro) QUOTE(macro)

START_TEST(test_read)
{
  isti_db *db = NULL;
  fail_if(odbc.open(&db, STR(DSN)), "Could not connect to database");
  isti_sql *q = NULL;
  fail_if(sql.sqlf(&q, "select id, bar, baz from foo where id = %d", 1),
          "Could not create SQL");

  foo f1;
  fail_if(db->sql_one(db, q, "dds", corm_foo_read_one, &f1), "Could not load foo");
  fail_if(f1.id != 1, "Bad id: %d", f1.id);
  fail_if(f1.bar != 42, "Bad bar: %d", f1.bar);
  fail_if(strcmp(f1.baz, "towel"), "Bad baz: %s", f1.baz);
  fail_if(sql.free(q, 0), "Could not free q");

  // now repeat via cgen
  foo *f2 = NULL;
  corm_foo_select *s;
  fail_if(corm_foo.select(&s, db), "Could not create select");
  fail_if(s->_where(s)->id(s, "=", 1)->_go_one(s, &f2), "Cannot select");
  fail_if(f1.id != 1, "Bad id: %d", f2->id);
  fail_if(f1.bar != 42, "Bad bar: %d", f2->bar);
  fail_if(strcmp(f1.baz, "towel"), "Bad baz: %s", f2->baz);
  free(f2);

  fail_if(db->close(db, 0), "Could not free db");
}
END_TEST

START_TEST(test_error)
{
  isti_db *db = NULL;
  fail_if(!odbc.open(&db, STR("bad dsn")), "Could connect to database");
}
END_TEST

START_TEST(test_count)
{
  isti_db *db = NULL;
  fail_if(odbc.open(&db, STR(DSN)), "Could not connect to database");
  isti_sql *q = NULL;
  fail_if(sql.sqlf(&q, "select id, bar, baz from foo"), "Could not create SQL");
  int n = -1;
  fail_if(db->sql_count(db, q, &n), "Could not count");
  fail_if(n != 2, "Incorrect count: %d", n);
  fail_if(sql.free(q, 0), "Could not free q");
  fail_if(db->close(db, 0), "Could not free db");
}
END_TEST

START_TEST(test_any)
{
  isti_db *db = NULL;
  fail_if(odbc.open(&db, STR(DSN)), "Could not connect to database");
  isti_sql *q = NULL;
  fail_if(sql.sqlf(&q, "select id, bar, baz from foo"), "Could not create SQL");
  corm_foo_array *a = NULL;
  fail_if(corm_foo_array_alloc(&a));
  fail_if(db->sql_any(db, q, "dds", corm_foo_read_any, a), "Could not load foos");
  fail_if(a->n.used != 2, "Read unexpected number: %d", a->n.used);
  foo *f = a->foo[0];
  fail_if(f->id != 1, "Bad id: %d", f->id);
  fail_if(f->bar != 42, "Bad bar: %d", f->bar);
  fail_if(strcmp(f->baz, "towel"), "Bad baz: %s", f->baz);
  fail_if(corm_foo_array_free(a, 0));
  fail_if(sql.free(q, 0), "Could not free q");
  fail_if(db->close(db, 0), "Could not free db");
}
END_TEST

Suite* odbc_suite (void) {
  Suite *suite = suite_create("isti_odbc");
  TCase *tcase = tcase_create("case");
  tcase_add_test(tcase, test_read);
  tcase_add_test(tcase, test_error);
  tcase_add_test(tcase, test_count);
  tcase_add_test(tcase, test_any);
  suite_add_tcase(suite, tcase);
  return suite;
}

int main (int argc, char *argv[]) {
  int number_failed;
  Suite *suite = odbc_suite();
  SRunner *runner = srunner_create(suite);
  srunner_set_xml(runner, "check-isti_odbc.xml");
  srunner_run_all(runner, CK_NORMAL);
  number_failed = srunner_ntests_failed(runner);
  srunner_free(runner);
  return number_failed;
}
