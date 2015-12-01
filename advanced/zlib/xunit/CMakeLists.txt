include_directories(
    ${INCLUDE_DIRECTORIES}
    ${CMAKE_SOURCE_DIR}/src/
    ${CMAKE_SOURCE_DIR}/
    ${CMAKE_SOURCE_DIR}/contrib/
    ${CMAKE_SOURCE_DIR}/contrib/minizip

    ${CMAKE_BINARY_DIR}
    /usr/include
)

link_directories(
    ${CMAKE_BINARY_DIR}
)

add_executable(check_compress_xunit check_compress_xunit.c)
target_link_libraries(check_compress_xunit z check)
add_test(NAME check_compress_xunit COMMAND ${CMAKE_BINARY_DIR}/xunit/check_compress_xunit)

add_executable(check_example_xunit example_check.c)
target_link_libraries(check_example_xunit z check)
add_test(NAME check_example_xunit COMMAND ${CMAKE_BINARY_DIR}/xunit/check_example_xunit)

