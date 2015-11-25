#include <cppunit/extensions/TestFactoryRegistry.h>
#include <cppunit/ui/text/TextTestRunner.h>
#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/TestSuite.h>
#include <cppunit/TestCaller.h>

#include "mystring.h"
class mystringTest : public CppUnit::TestCase{
public:
    void setUp(){
        std::cout << "Do some initialization here \n";
    }
    void tearDown(){
        std::cout << "cleanup actions post test execution\n";
    }
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


//CPPUNIT_TEST_SUITE_REGISTRATION(mystringTest);
/*
int main()
{
    CppUnit::Test *test = CppUnit::TestFactoryRegistry::getRegistry().makeTest();
    CppUnit::TextTestRunner runner;
    runner.addTest(test);
    runner.run();
    return 0;

}
*/

int main()
{
    CppUnit::TestSuite* suite = new CppUnit::TestSuite("mystringTest");
    suite->addTest(new CppUnit::TestCaller<mystringTest>("checkLength",&mystringTest::checkLength));
    suite->addTest(new CppUnit::TestCaller<mystringTest>("checkValuue",&mystringTest::checkValue));

    //client code follows next
    CppUnit::TextTestRunner runner;
    runner.addTest(suite);

    runner.run();
    return 0;

}
