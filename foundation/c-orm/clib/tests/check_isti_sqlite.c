
#include <stdio.h>
#include <check.h>

#include "isti.h"
#include "isti_sql.h"
#include "isti_sqlite.h"

#include "foo.h"

ISTI_SQL_AS(sql)
ISTI_SQLITE_AS(sqlite)

static int load_foo(void *v, size_t n, char type, void *value) {
  foo *f = (foo *)v;
  switch (n) {
  case 0: f->id = *(int *)value; break;
  case 1: f->bar = *(int *)value; break;
  case 2: f->baz = (char *)value; break;
  default: return -1;
  }
  return 0;
}

START_TEST(test_read)
{
  isti_db *db = NULL;
  fail_if(sqlite.open(&db, "check_isti_sqlite.db", 60),
          "Could not connect to database");
  isti_sql *q = NULL;
  fail_if(sql.sqlf(&q, "select id, bar, baz from foo where id = %d", 1),
          "Could not create SQL");
  foo f;
  fail_if(db->sql_one(db, q, "dds", load_foo, &f), "Could not load foo");
  fail_if(f.id != 1, "Bad id: %d", f.id);
  fail_if(f.bar != 42, "Bad bar: %d", f.bar);
  fail_if(strcmp(f.baz, "towel"), "Bad baz: %s", f.baz);
  fail_if(sql.free(q, 0), "Could not free q");
  fail_if(db->close(db, 0), "Could not free db");
}
END_TEST

Suite* sqlite_suite (void) {
  Suite *suite = suite_create("isti_sqlite");
  TCase *tcase = tcase_create("case");
  tcase_add_test(tcase, test_read);
  suite_add_tcase(suite, tcase);
  return suite;
}

int main (int argc, char *argv[]) {
  int number_failed;
  Suite *suite = sqlite_suite();
  SRunner *runner = srunner_create(suite);
  srunner_set_xml(runner, "check-isti_sqlite.xml");
  srunner_run_all(runner, CK_NORMAL);
  number_failed = srunner_ntests_failed(runner);
  srunner_free(runner);
  return number_failed;
}
