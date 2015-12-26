#include <cppunit/extensions/TestFactoryRegistry.h>
#include <cppunit/ui/text/TextTestRunner.h>
#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/TestSuite.h>
#include <cppunit/TestCaller.h>
#include <cppunit/TestListener.h>
#include <cppunit/TestResultCollector.h>
#include <cppunit/CompilerOutputter.h>

#include <cppunit/TestResult.h>

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
        CPPUNIT_ASSERT_EQUAL_MESSAGE("Corrupt String Data",s[0],'h');

    }
    CPPUNIT_TEST_SUITE(mystringTest);
    CPPUNIT_TEST(checkLength);
    CPPUNIT_TEST(checkValue);
    CPPUNIT_TEST_SUITE_END();
};

class myListener : public CppUnit::TestResultCollector{
public:
    void startTest(CppUnit::Test* test){
        std::cout << "starting to measure time\n";
    }
    void endTest(CppUnit::Test* test){
        std::cout << "done with measuring time\n";
    }

};

int main()
{
    CppUnit::TestSuite* suite = new CppUnit::TestSuite("mystringTest");
    suite->addTest(new CppUnit::TestCaller<mystringTest>("checkLength",&mystringTest::checkLength));
    suite->addTest(new CppUnit::TestCaller<mystringTest>("checkValuue",&mystringTest::checkValue));
    suite->addTest(new CppUnit::TestCaller<mystringTest>("checkValuue",&mystringTest::checkValue));

    //client code follows next
    CppUnit::TestRunner runner;
    runner.addTest(suite);

    myListener listener;
    CppUnit::TestResult result;
    result.addListener(&listener);

    runner.run(result);

    CppUnit::CompilerOutputter outputter (&listener, std::cerr);
    outputter.write();
    return 0;

}
