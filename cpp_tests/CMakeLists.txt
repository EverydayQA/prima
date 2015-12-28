cmake_minimum_required(VERSION 2.8)

enable_testing()
include_directories(

)

link_directories(
)
set(test_SRCSA
DemoTest.cpp
DemoTest.h
TestA.cc
)

set(test_SRCS
DemoTest.cpp
DemoTest.h
TestMain.cpp
)
add_executable(cppunit_test ${test_SRCS} )

target_link_libraries(cppunit_test cppunit)

add_test(NAME cppunit_test COMMAND ${CMAKE_BINARY_DIR}/cppunit_test)


