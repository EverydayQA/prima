#include <limits.h>
#include <gtest/gtest.h>
#define BOOST_TEST_MODULE MyTest
#include <boost/test/unit_test.hpp>

int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

