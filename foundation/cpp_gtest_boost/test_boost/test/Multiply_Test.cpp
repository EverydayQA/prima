#include <limits.h>
#define BOOST_TEST_MODULE MyTest
#include <boost/test/unit_test.hpp>
#include "Multiply.hpp"


BOOST_AUTO_TEST_CASE(my_test)
{
    const int x =4;
    const int y=5;
    Multiply multiply;
    BOOST_CHECK(multiply.twoValues(x,y) == 20);
    BOOST_CHECK_EQUAL(multiply.twoValues(2,3),6);

}

