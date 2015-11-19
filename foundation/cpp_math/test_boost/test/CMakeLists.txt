find_package(Threads REQUIRED)
set (test_SRCS
    #Main_TestAll.cpp
Addition_Test.cpp
Multiply_Test.cpp

)


include_directories(
    ${INCLUDE_DIRECTORIES}
    "${CMAKE_SOURCE_DIR}/libmath/"
)

link_directories(
    ${CMAKE_BINARY_DIR}/libmath
)

# pthread for gtest m - force of habit
add_executable(boost_testAll ${test_SRCS})
target_link_libraries(boost_testAll foomath ${Boost_LIBRARIES} pthread m)
add_test(NAME boost_testAll COMMAND "${CMAKE_BINARY_DIR}/test_boost/test/boost_testAll")
