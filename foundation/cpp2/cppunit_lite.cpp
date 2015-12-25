#include <iostream>
#include <string>

#include <CppUnitLite/TestHarness.h>

using namespace std;

int main()
{
    TestResult tr;
    TestRegistry::runAllTests(tr);

    return 0;
}


TEST( Stack, creation )
{
    CHECK_EQUAL("a", "a");
}
