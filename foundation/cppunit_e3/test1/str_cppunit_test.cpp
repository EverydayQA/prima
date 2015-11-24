#include <cppunit/TestCase.h>
//#include <cppunit/ui/text/TextTestRunner.h>
#include <cppunit/ui/text/TestRunner.h>

#include "mystring.h"
class mystringTest : public CppUnit::TestCase{
public:
    void runTest(){
        mystring s;
        CPPUNIT_ASSERT_MESSAGE("String Length NON-ZERO",1 !=0);
    }

};

int main(){
    mystringTest test;
    //CppUnit::TextTestRunner runner;
    CppUnit::TextUi::TestRunner runner;

    runner.addTest(&test);

    runner.run();
    return 0;

}
