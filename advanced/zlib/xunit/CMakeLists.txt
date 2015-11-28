include_directories(
    ${INCLUDE_DIRECTORIES}
    ${CMAKE_SOURCE_DIR}/src/
    /usr/include
)

link_directories(
    ${CMAKE_BINARY_DIR}
)

add_executable(check_compress_xunit check_compress_xunit.c)
target_link_libraries(check_compress_xunit z check)

add_test(NAME check_compress_xunit COMMAND ${CMAKE_BINARY_DIR}/xunit/check_compress_xunit)

