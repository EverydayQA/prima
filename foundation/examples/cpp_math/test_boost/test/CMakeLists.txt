find_package(Threads REQUIRED)
set (test_SRCS
    #Main_TestAll.cpp
Addition_Test.cpp
Multiply_Test.cpp

)

#add_library(libgtest IMPORTED STATIC GLOBAL)
#add_dependencies(libgtest gtest)

include_directories(
    ${INCLUDE_DIRECTORIES}
    "${CMAKE_SOURCE_DIR}/libmath/"
)

link_directories(
    ${CMAKE_BINARY_DIR}/libmath
)
#add_library(libgmock IMPORTED STATIC GLOBAL)
#add_dependencies(libgmock gmock)

add_executable(testAll ${test_SRCS})
target_link_libraries(testAll foomath ${Boost_LIBRARIES} pthread m)
add_test(NAME testAll COMMAND "${CMAKE_BINARY_DIR}/test_boost/test/testAll")


#target_link_libraries(testAll foomath gtest gtest_main pthread m)


