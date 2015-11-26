#define BOOST_TEST_MODULE enumtest
#include <boost/test/included/unit_test.hpp>
#include "mystring.h"

BOOST_AUTO_TEST_SUITE(enumtest) //name of the test suite 
BOOST_AUTO_TEST_CASE(test1)
{
    typedef enum{red=8,blue,green=1,yellow,black}color;
    color c = green;

    BOOST_WARN(sizeof(green)>sizeof(char));
    BOOST_CHECK(c==2);
    BOOST_REQUIRE(yellow>red);
    BOOST_CHECK(black !=4);
}
BOOST_AUTO_TEST_SUITE_END();

/*
BOOST_AUTO_TEST(functionTest1)
{
    BOOST_REQUIRE(myfunc1(99,'A',6.2)==2);
    myClass o1("hellow world!\n");
    BOOST_REQUIRE(o1.memoryNeeded()<16);
}

*/

