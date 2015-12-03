
include_directories(
    ${CMAKE_SOURCE_DIR}/include
    /usr/include
)

link_directories(
    ${CMAKE_BINARY_DIR}/lib
    /usr/lib64
)

add_executable(test_addition2 test_add.c test_main.c)
target_link_libraries(test_addition2 add check)
add_test(NAME test_addition2 COMMAND ${CMAKE_BINARY_DIR}/tests2/test_addition2 ${CMAKE_BINARY_DIR}/Makefile)
