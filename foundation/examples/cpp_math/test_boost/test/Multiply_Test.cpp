#include <limits.h>
#include <gtest/gtest.h>
#define BOOST_TEST_MODULE MyTest
#include <boost/test/unit_test.hpp>

#include "Multiply.hpp"


/*
class MultiplyTest : public ::testing::Test{

    protected:
        virtual void SetUp(){
        }
        virtual void TearDown(){
        }
};

TEST_F(MultiplyTest,twoValues){
    const int x = 4;
    const int y = 5;
    Multiply multiply;
    EXPECT_EQ(20,multiply.twoValues(x,y));
    EXPECT_EQ(6,multiply.twoValues(2,3));



}
*/
BOOST_AUTO_TEST_CASE(my_test)
{
    const int x =4;
    const int y=5;
    Multiply multiply;
    BOOST_CHECK(multiply.twoValues(x,y) == 9);
    BOOST_CHECK_EQUAL(multiply.twoValues(2,3),5);

}
