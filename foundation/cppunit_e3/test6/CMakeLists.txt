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
mystringTest.cpp
TestMain.cpp

)

add_executable(test6 ${test_SRCS} )
target_link_libraries(test6 cppunit)
add_test(NAME test6 COMMAND ${CMAKE_BINARY_DIR}/test6/test6)
