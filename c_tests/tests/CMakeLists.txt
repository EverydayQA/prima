include_directories(
    ${INCLUDE_DIRECTORIES}
    ${CMAKE_SOURCE_DIR}/src/
    /usr/include
)

link_directories(
    ${CMAKE_BINARY_DIR}/src
)
cmake_minimum_required(VERSION 3.14)
#CMAKE_MAKE_PROGRAM
#CMAKE_C_COMPILER
#CMAKE_CXX_COMPILER

add_executable(check_money check_money.c)
target_link_libraries(check_money money check)

add_test(NAME check_money COMMAND ${CMAKE_BINARY_DIR}/tests/check_money)

