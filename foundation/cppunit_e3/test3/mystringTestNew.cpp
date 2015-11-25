#include <cppunit/extensions/TestFactoryRegistry.h>
#include <cppunit/ui/text/TextTestRunner.h>
#include <cppunit/extensions/HelperMacros.h>

#include "mystring.h"
class mystringTestNew : public CppUnit::TestCase{
public:
    void someMoreChecks(){
        std::cout <<"some ore checks ...\n";
    }

    CPPUNIT_TEST_SUITE(mystringTestNew);
    CPPUNIT_TEST(someMoreChecks);
    CPPUNIT_TEST_SUITE_END();
};


CPPUNIT_TEST_SUITE_REGISTRATION(mystringTestNew);
