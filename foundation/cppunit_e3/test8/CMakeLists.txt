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
add_executable(sort sort.cc)

add_executable(test8 ${test_SRCS} )

target_link_libraries(test8 cppunit)

add_test(NAME test8 COMMAND ${CMAKE_BINARY_DIR}/test8/test8)
