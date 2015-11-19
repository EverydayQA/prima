
#include <check.h>
#include <stdio.h>

#include "isti.h"
#include "isti_flow.h"
#include "isti_sql.h"
#include "isti_sqlite.h"

#include "foo.corm.h"

ISTI_SQLITE_AS(sqlite)
CORM_FOO_AS(corm_foo)

START_TEST(test_go)
{
  isti_db *db = NULL;
  fail_if(sqlite.open(&db, "check_foo.db", 60), "cannot connect to db");

  corm_foo_delete *s = NULL;
  fail_if(corm_foo.delete(&s, db), "cannot create delete");

  fail_if(s->_where(s)->bar(s, "=", 42)->_and(s)->\
      _bra(s)->baz(s, "like", "towel")->_or(s)->baz(s, "like", "fish")->_ket(s)->\
      _go(s), "cannot delete verbose");

  fail_if(s->_reset(s), "cannot reset");
  fail_if(s->_(s, "where bar=%d", 42)->_go(s), "cannot delete literal");

  fail_if(s->_reset(s), "cannot reset");
  fail_if(s->_(s, "where")->bar(s, "=", 42)->_go(s), "cannot delete mixed");

  fail_if(s->_reset(s), "cannot reset");
  fail_if(s->bar(s, "=", 42)->baz(s, "=", "towel")->_go(s), "cannot delete brief");

  fail_if(s->_free(s, 0), "cannot free s");
  fail_if(db->close(db, 0), "cannot close db");
}
END_TEST



// Everything below is boilerplate for the tests.

Suite* delete_suite (void) {
  Suite *suite = suite_create("foo");
  TCase *tcase = tcase_create("case");
  tcase_add_test(tcase, test_go);
  suite_add_tcase(suite, tcase);
  return suite;
}

int main (int argc, char *argv[]) {
  int number_failed;
  Suite *suite = delete_suite();
  SRunner *runner = srunner_create(suite);
  srunner_set_xml(runner, "check-delete_foo.xml");
  srunner_run_all(runner, CK_NORMAL);
  number_failed = srunner_ntests_failed(runner);
  srunner_free(runner);
  return number_failed;
}
