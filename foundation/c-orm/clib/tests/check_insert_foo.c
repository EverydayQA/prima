
#include <check.h>
#include <stdio.h>

#include "isti.h"
#include "isti_flow.h"
#include "isti_sql.h"
#include "isti_sqlite.h"

#include "foo.corm.h"

ISTI_SQLITE_AS(sqlite)
CORM_FOO_AS(corm_foo)

void assert_foo(foo *f, int id, int bar, const char *baz) {
  fail_if(!f, "null");
  fail_if(f->id != id, "bad id %d", f->id);
  fail_if(f->bar != bar, "bad bar %d", f->bar);
  fail_if(!f->baz ,"null baz");
  fail_if(!baz ,"null baz");
  fail_if(baz && f && f->baz && strcmp(f->baz, baz) ,"bad baz %s", f->baz);
}

START_TEST(test_go_one)
{
  corm_foo_insert *ins = NULL;
  foo *f = NULL;
  isti_db *db = NULL;
  fail_if(sqlite.open(&db, "check_foo.db", 60), "cannot connect to db");
  fail_if(corm_foo.insert(&ins, db), "cannot create insert");
  fail_if(!(f = calloc(1, sizeof(*f))), "cannot alloc foo");
  f->id = 3;
  f->bar = 1;
  f->baz = "foop";
  fail_if(ins->_go_one(ins, f), "cannot insert foo");
  assert_foo(f, 3, 1, "foop");
  f->baz = NULL; // hide non-heap string
  fail_if(corm_foo_free(f, 0), "cannot free f");
  fail_if(ins->_free(ins, 0), "cannot free ins");
  fail_if(db->close(db, 0), "cannot close db");
}
END_TEST

START_TEST(test_go_one_key)
{
  corm_foo_insert *ins = NULL;
  foo *f = NULL;
  isti_db *db = NULL;
  fail_if(sqlite.open(&db, "check_foo.db", 60), "cannot connect to db");
  fail_if(corm_foo.insert(&ins, db), "cannot create insert");
  fail_if(!(f = calloc(1, sizeof(*f))), "cannot alloc foo");
  f->bar = 2;
  f->baz = "doop";
  fail_if(ins->id_key(ins)->_go_one(ins, f), "cannot insert foo");
  assert_foo(f, 4, 2, "doop");
  f->baz = NULL; // hide non-heap string
  fail_if(corm_foo_free(f, 0), "cannot free f");
  fail_if(ins->_free(ins, 0), "cannot free ins");
  fail_if(db->close(db, 0), "cannot close db");
}
END_TEST



// Everything below is boilerplate for the tests.

Suite* insert_suite (void) {
  Suite *suite = suite_create("foo");
  TCase *tcase = tcase_create("case");
  tcase_add_test(tcase, test_go_one);
  tcase_add_test(tcase, test_go_one_key);
  suite_add_tcase(suite, tcase);
  return suite;
}

int main (int argc, char *argv[]) {
  int number_failed;
  Suite *suite = insert_suite();
  SRunner *runner = srunner_create(suite);
  srunner_set_xml(runner, "check-insert_foo.xml");
  srunner_run_all(runner, CK_NORMAL);
  number_failed = srunner_ntests_failed(runner);
  srunner_free(runner);
  return number_failed;
}
