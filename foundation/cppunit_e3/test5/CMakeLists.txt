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
#TestMain.cpp

)

add_executable(test5 ${test_SRCS} )
target_link_libraries(test5 cppunit)
add_test(NAME test5 COMMAND ${CMAKE_BINARY_DIR}/test5/test5)
