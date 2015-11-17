#include <limits.h>
#include <gtest/gtest.h>
#define BOOST_TEST_MODULE MyTest
#include <boost/test/unit_test.hpp>
#include "Addition.hpp"

/*
class AdditionTest : public ::testing::Test{
    protected:
        virtual void SetUp(){
        }
        virtual void TearDown(){
            //code here will be called right aftr each tes            // before the destructor

        }
        
};

TEST_F(AdditionTest,twoValues){
    const int x = 4;
    const int y = 5;
    Addition addition;
    EXPECT_EQ(9,addition.twoValues(x,y));
    EXPECT_EQ(5,addition.twoValues(2,3));

}
*/
BOOST_AUTO_TEST_CASE(my_test)
{
    Addition addition;
    const int x =4;
    const int y=5;
    BOOST_CHECK(addition.twoValues(x,y) == 9);
    BOOST_CHECK_EQUAL(addition.twoValues(2,3),5);

}
