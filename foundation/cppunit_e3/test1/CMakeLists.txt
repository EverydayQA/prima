cmake_minimum_required(VERSION 2.8)

enable_testing()
include_directories(
    ${CMAKE_SOURCE_DIR}
    /usr/include
)

link_directories(
    /usr/lib64

)

set(CMAKE_CXX_COMPILER g++)

set(test_SRCS
    ${CMAKE_SOURCE_DIR}/mystring.h
    str_cppunit_test.cpp

)

add_executable(cppunit_test ${test_SRCS} )
target_link_libraries(cppunit_test cppunit)
add_test(NAME cppunit_test COMMAND ${CMAKE_BINARY_DIR}/test1/cppunit_test)
