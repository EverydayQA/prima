#ifndef DemoTest_h
#define DemoTest_h

#include <cppunit/extensions/HelperMacros.h>

class DemoTest : public CppUnit::TestFixture
{
    CPPUNIT_TEST_SUITE(DemoTest);
    CPPUNIT_TEST(testFunc);
    CPPUNIT_TEST_SUITE_END();

public:
    void setUp();
    void tearDown();
    void testFunc();
};
#endif //
