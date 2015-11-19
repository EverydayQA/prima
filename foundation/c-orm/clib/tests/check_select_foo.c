
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
  isti_db *db = NULL;
  fail_if(sqlite.open(&db, "check_foo.db", 60), "cannot connect to db");

  corm_foo_select *s = NULL;
  fail_if(corm_foo.select(&s, db), "cannot create select");

  foo *f = NULL;
  fail_if(s->_where(s)->bar(s, "=", 42)->_and(s)->\
      _bra(s)->baz(s, "like", "towel")->_or(s)->baz(s, "like", "fish")->_ket(s)->\
      _go_one(s, &f), "cannot retrieve verbose");
  assert_foo(f, 1, 42, "towel");

  corm_foo_free(f, 0);
  fail_if(s->_reset(s), "cannot reset");
  fail_if(s->_(s, "where bar=%d", 42)->_go_one(s, &f), "cannot retrieve literal");
  assert_foo(f, 1, 42, "towel");

  corm_foo_free(f, 0);
  fail_if(s->_reset(s), "cannot reset");
  fail_if(s->_(s, "where")->bar(s, "=", 42)->_go_one(s, &f), "cannot retrieve mixed");
  assert_foo(f, 1, 42, "towel");

  corm_foo_free(f, 0);
  fail_if(s->_reset(s), "cannot reset");
  fail_if(s->bar(s, "=", 42)->baz(s, "=", "towel")->_go_one(s, &f), "cannot retrieve brief");
  assert_foo(f, 1, 42, "towel");

  corm_foo_free(f, 0);
  fail_if(s->_free(s, 0), "cannot free s");
  fail_if(db->close(db, 0), "cannot close db");
}
END_TEST

START_TEST(test_cond_equiv)
{
  isti_db *db = NULL;
  fail_if(sqlite.open(&db, "check_foo.db", 60), "cannot connect to db");

  isti_cond *c = NULL;
  fail_if(isti_cond_alloc(&c), "cannot create cond");

  foo *f = NULL;
  fail_if(!(f = calloc(1, sizeof(*f))), "cannot alloc f");
  fail_if(c->select(c, "id, bar, baz")->from(c, "foo")->_d(c, "bar", "=", 42)->_s(c, "baz", "=", "towel")->status, "cannot construct sql");
  fail_if(db->sql_one(db, c->sql, "dds", corm_foo_read_one, f), "cannot read foo");
  assert_foo(f, 1, 42, "towel");

  fail_if(corm_foo_free(f, 0), "cannot free f");
  fail_if(isti_cond_free(c, 0), "cannot free c");
  fail_if(db->close(db, 0), "cannot close db");
}
END_TEST

START_TEST(test_go_count)
{
  isti_db *db = NULL;
  fail_if(sqlite.open(&db, "check_foo.db", 60), "cannot connect to db");

  corm_foo_select *s = NULL;
  fail_if(corm_foo.select(&s, db), "cannot create select");

  int n = 0;
  fail_if(s->bar(s, "=", 42)->_go_count(s, &n), "cannot retrieve count");
  fail_if(n != 1, "bad count %d", n);

  fail_if(s->_reset(s), "cannot reset");
  fail_if(s->bar(s, "=", 42)->baz(s, "like", "sausage")->_go_count(s, &n),
      "cannot retrieve count");
  fail_if(n != 0, "bad count %d", n);

  fail_if(s->_free(s, 0), "cannot free s");
  fail_if(db->close(db, 0), "cannot close db");
}
END_TEST

START_TEST(test_go_any)
{
  isti_db *db = NULL;
  fail_if(sqlite.open(&db, "check_foo.db", 60), "cannot connect to db");

  corm_foo_select *s = NULL;
  fail_if(corm_foo.select(&s, db), "cannot create select");

  corm_foo_array *a = NULL;
  fail_if(s->_go_any(s, &a), "cannot retrieve all");
  fail_if(a->n.used != 2, "retrieved unexpected number %d", a->n.used);
  fail_if(corm_foo.array.free(a, 0), "cannot free a");

  fail_if(s->_free(s, 0), "cannot free s");
  fail_if(db->close(db, 0), "cannot close db");
}
END_TEST

START_TEST(test_in)
{
  isti_db *db = NULL;
  fail_if(sqlite.open(&db, "check_foo.db", 60), "cannot connect to db");

  corm_foo_select *s = NULL;
  fail_if(corm_foo.select(&s, db), "cannot create select");

  int ids[] = {0,1,2};
  corm_foo_array *a = NULL;
  fail_if(s->foo_id_(s, "in", ids, 3)->_go_any(s, &a), "cannot retrieve all");
  fail_if(a->n.used != 2, "retrieved unexpected number %d", a->n.used);
  fail_if(corm_foo.array.free(a, 0), "cannot free a");

  fail_if(s->_free(s, 0), "cannot free s");
  fail_if(db->close(db, 0), "cannot close db");
}
END_TEST


// Everything below is boilerplate for the tests.

Suite* sqlite_suite (void) {
  Suite *suite = suite_create("foo");
  TCase *tcase = tcase_create("case");
  tcase_add_test(tcase, test_go_one);
  tcase_add_test(tcase, test_cond_equiv);
  tcase_add_test(tcase, test_go_count);
  tcase_add_test(tcase, test_go_any);
  tcase_add_test(tcase, test_in);
  suite_add_tcase(suite, tcase);
  return suite;
}

int main (int argc, char *argv[]) {
  int number_failed;
  Suite *suite = sqlite_suite();
  SRunner *runner = srunner_create(suite);
  srunner_set_xml(runner, "check-select_foo.xml");
  srunner_run_all(runner, CK_NORMAL);
  number_failed = srunner_ntests_failed(runner);
  srunner_free(runner);
  return number_failed;
}
