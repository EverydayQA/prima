include_directories(
    ${INCLUDE_DIRECTORIES}
    ${CMAKE_SOURCE_DIR}/src/
)
link_directories(
    ${CMAKE_BINARY_DIR}/src
)
add_executable(check_money check_money.c)
target_link_libraries(check_money libmoney check)


