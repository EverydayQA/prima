
#include <check.h>
#include <stdio.h>

#include "isti_log.h"

START_TEST(test_log)
{
  ISTI_LOG("hello %s\n", "world");
}
END_TEST


Suite* log_suite (void) {
  Suite *suite = suite_create("isti_log");
  TCase *tcase = tcase_create("case");
  tcase_add_test(tcase, test_log);
  suite_add_tcase(suite, tcase);
  return suite;
}

int main (int argc, char *argv[]) {
  int number_failed;
  Suite *suite = log_suite();
  SRunner *runner = srunner_create(suite);
  srunner_set_xml(runner, "check-isti_log.xml");
  srunner_run_all(runner, CK_NORMAL);
  number_failed = srunner_ntests_failed(runner);
  srunner_free(runner);
  return number_failed;
}
