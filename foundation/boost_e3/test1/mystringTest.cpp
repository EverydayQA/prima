#define BOOST_TEST_MODULE stringtest
#include <boost/test/included/unit_test.hpp>
#include "mystring.h"

BOOST_AUTO_TEST_SUITE(stringtest) //name of the test suite 
BOOST_AUTO_TEST_CASE(test1)
{
    mystring s;
    BOOST_CHECK(s.size()==0);
}

BOOST_AUTO_TEST_CASE(test2)
{
    mystring s;
    char* x = "hello world";
    s.setbuffer(x);
    BOOST_REQUIRE_EQUAL('h',s[0]); //basic test
}

BOOST_AUTO_TEST_SUITE_END();

