find_package(Threads REQUIRED)
set (test_SRCS
Main_TestAll.cpp
Addition_Test.cpp
Multiply_Test.cpp

)

# original - download gtest
#add_library(libgtest IMPORTED STATIC GLOBAL)
#add_dependencies(libgtest gtest)

include_directories(
    ${INCLUDE_DIRECTORIES}
    "${CMAKE_SOURCE_DIR}/libmath/"
)

link_directories(
    ${CMAKE_BINARY_DIR}/libmath
)
# orignal - download gmock
#add_library(libgmock IMPORTED STATIC GLOBAL)
#add_dependencies(libgmock gmock)
add_executable(gtest_all ${test_SRCS})

target_link_libraries(gtest_all foomath gtest gtest_main pthread m)

add_test(NAME gtest_all COMMAND "${CMAKE_BINARY_DIR}/test_gtest/test/gtest_all")
