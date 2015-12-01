include_directories(
    ${CMAKE_SOURCE_DIR}/src/
)
link_directories(
    ${CMAKE_BINARY_DIR}/src
)

add_executable(check_money1 check_money.1.c)
target_link_libraries(check_money1 money check)
add_test(NAME check_money1 COMMAND ${CMAKE_BINARY_DIR}/tests/check_money1)

add_executable(check_money2 check_money.2.c)
target_link_libraries(check_money2 money check)
add_test(NAME check_money2 COMMAND ${CMAKE_BINARY_DIR}/tests/check_money2)

add_executable(check_money3 check_money.3.c)
target_link_libraries(check_money3 money3 check)
add_test(NAME check_money3 COMMAND ${CMAKE_BINARY_DIR}/tests/check_money3)

add_executable(check_money6 check_money.6.c)
target_link_libraries(check_money6 money4 check)
add_test(NAME check_money6 COMMAND ${CMAKE_BINARY_DIR}/tests/check_money6)

add_executable(check_money7 check_money.7.c)
target_link_libraries(check_money7 money5 check)
add_test(NAME check_money7 COMMAND ${CMAKE_BINARY_DIR}/tests/check_money7)

add_executable(check_money check_money.c)
target_link_libraries(check_money money check)
add_test(NAME check_money COMMAND ${CMAKE_BINARY_DIR}/tests/check_money)
