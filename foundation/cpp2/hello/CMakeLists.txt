cmake_minimum_required(VERSION 2.8)

enable_testing()
include_directories(

)

link_directories(
)

set(test_SRCS
    test.cc
)
add_executable(cppunit_test ${test_SRCS} )
add_executable(cppunit_simple simple.cc )
add_executable(suba subarray.cc )

target_link_libraries(cppunit_test cppunit)
target_link_libraries(cppunit_simple cppunit)

add_test(NAME cppunit_test COMMAND ${CMAKE_BINARY_DIR}/cppunit_test)
add_test(NAME cppunit_simple COMMAND ${CMAKE_BINARY_DIR}/cppunit_simple)


