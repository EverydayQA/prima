#ifndef __TEST_H
#define __TEST_H

#include <check.h>
Suite *make_add_suite(void);
Suite *make_add_suite2(void);


typedef struct TestData TestData;

TestData *testData_create (char  * line);
void testData_free (TestData * td);

#endif /* MONEY_H */
