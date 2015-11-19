#include <limits.h>
#ifdef STAND_ALONE
#   define BOOST_TEST_MODULE Main
#endif
#include <boost/test/unit_test.hpp>
#include "Addition.hpp"

BOOST_AUTO_TEST_SUITE(Foo)
BOOST_AUTO_TEST_CASE(my_test)
{
    Addition addition;
    const int x =4;
    const int y=5;
    BOOST_CHECK(addition.twoValues(x,y) == 9);
    BOOST_CHECK_EQUAL(addition.twoValues(2,3),5);

}
BOOST_AUTO_TEST_SUITE_END()
