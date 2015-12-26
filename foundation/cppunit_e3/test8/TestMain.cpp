#include <cppunit/extensions/TestFactoryRegistry.h>
#include <cppunit/ui/text/TextTestRunner.h>
#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/TestSuite.h>
#include <cppunit/TestCaller.h>
#include "mystring.h"
int main()
{
    CppUnit::TestSuite* suite = new CppUnit::TestSuite("mystringTest");
    suite->addTest(new CppUnit::TestCaller<mystringTest>("checkLength",&mystringTest::checkLength));
    suite->addTest(new CppUnit::TestCaller<mystringTest>("checkValuue",&mystringTest::checkValue));
    CppUnit::TextTestRunner runner;
    runner.addTest(suite);
    runner.run();
    return 0;
}
