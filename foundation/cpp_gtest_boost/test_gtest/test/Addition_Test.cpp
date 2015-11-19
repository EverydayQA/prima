#include <limits.h>
#include <gtest/gtest.h>
#include "Addition.hpp"

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
