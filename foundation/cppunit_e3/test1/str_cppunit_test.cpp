#include <cppunit/TestCase.h>
#include <cppunit/ui/text/TextTestRunner.h>
//#include <cppunit/ui/text/TestRunner.h>

#include "mystring.h"
class mystringTest : public CppUnit::TestCase{
public:
    void runTest(){
        mystring s;
        char ss[] = "hello";
        s.setbuffer(ss);
        CPPUNIT_ASSERT_MESSAGE("String Length NON-ZERO",s.size() !=0);
    }

};

int main(){
    mystringTest test;
    CppUnit::TextTestRunner runner;
    //CppUnit::TextUi::TestRunner runner;
    runner.addTest(&test);
    runner.run();
    return 0;
}
