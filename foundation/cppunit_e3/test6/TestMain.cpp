#include <cppunit/extensions/TestFactoryRegistry.h>
#include <cppunit/ui/text/TextTestRunner.h>
#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/CompilerOutputter.h>
#include "mystring.h"

//CPPUNIT_TEST_SUITE_REGISTRATION(mystringTest);
int main()
{
    CppUnit::Test *test = CppUnit::TestFactoryRegistry::getRegistry().makeTest();
    CppUnit::TextTestRunner runner;
    runner.addTest(test);

    //new for formatting
    const std::string format("%p:%l");
    std::ofstream ofile;
    ofile.open("run.log");
    CppUnit::CompilerOutputter* outputter = new
        CppUnit::CompilerOutputter(&runner.result(),ofile);
    outputter->setLocationFormat(format);
    runner.setOutputter(outputter);


    runner.run();
    ofile.close();
    return 0;

}
