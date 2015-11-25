#include <cppunit/extensions/TestFactoryRegistry.h>
#include <cppunit/ui/text/TextTestRunner.h>
#include <cppunit/extensions/HelperMacros.h>

#include "mystring.h"
class mystringTest : public CppUnit::TestCase{
public:
    void checkLength(){
        mystring s;
        CPPUNIT_ASSERT_MESSAGE("String Length Non-Zero",s.size() ==0);
    }

    void checkValue(){
        mystring s;
        s.setbuffer("hello world!\n");
        CPPUNIT_ASSERT_EQUAL_MESSAGE("Corrupt String Data",s[0],'w');

    }
    CPPUNIT_TEST_SUITE(mystringTest);
    CPPUNIT_TEST(checkLength);
    CPPUNIT_TEST(checkValue);
    CPPUNIT_TEST_SUITE_END();
};


CPPUNIT_TEST_SUITE_REGISTRATION(mystringTest);
int main()
{
    CppUnit::Test *test = CppUnit::TestFactoryRegistry::getRegistry().makeTest();
    CppUnit::TextTestRunner runner;
    runner.addTest(test);
    runner.run();
    return 0;

}
