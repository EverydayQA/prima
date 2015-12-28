#include <cppunit/ui/text/TestRunner.h>
#include <cppunit/extensions/TestFactoryRegistry.h>
#include <string>
#include <cppunit/TestRunner.h>
#include <cppunit/CompilerOutputter.h>
#include <cppunit/TestResult.h>
#include <cppunit/TestResultCollector.h>
#include <cppunit/TextTestProgressListener.h>
#include <cppunit/BriefTestProgressListener.h>
#include <cppunit/extensions/TestFactoryRegistry.h>
#include <signal.h>
#include <stdlib.h>
#include <stdexcept>
#include <unistd.h>
#include <sys/select.h>
#include <cppunit/Exception.h>
#include <cppunit/TestFailure.h>
#include <cppunit/XmlOutputter.h>
#include <cppunit/TestAssert.h>
#include <fstream>
#include <time.h> 
int main(int argc, char **argv)
{
    //create tst event manager and test contoller
    CppUnit::TestResult controller;
    CppUnit::TestResultCollector result;
    // add a listener that collect test result
    controller.addListener(&result);

    // a listener that print dots as tests run
    //CppUnit::TextTestProgressListener progress;
    CppUnit::BriefTestProgressListener progress;
    // brief + elapse time
    //TimeingListener progress;
    controller.addListener(&progress);
    
    CppUnit::TextUi::TestRunner runner;
    CppUnit::TestFactoryRegistry &registry = CppUnit::TestFactoryRegistry::getRegistry();
    runner.addTest(registry.makeTest());
    runner.run();
    return 0;

}
