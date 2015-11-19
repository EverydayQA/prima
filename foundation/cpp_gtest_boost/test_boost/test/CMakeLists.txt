find_package(Threads REQUIRED)
set (test_SRCS
Main_TestAll.cpp
Addition_Test.cpp
Multiply_Test.cpp

)

# have problem with find_package() and find_librry()
# will hard code here 
# gliang Nov 18, 2015

include_directories(
    ${INCLUDE_DIRECTORIES}
    "${CMAKE_SOURCE_DIR}/libmath/"
    /usr/include
)

link_directories(
    ${CMAKE_BINARY_DIR}/libmath
    /usr/lib64/
)

# pthread for gtest m - force of habit
add_executable(boost_testAll ${test_SRCS})
target_link_libraries(boost_testAll foomath boost_unit_test_framework-mt pthread m)
add_test(NAME boost_testAll COMMAND "${CMAKE_BINARY_DIR}/test_boost/test/boost_testAll")
