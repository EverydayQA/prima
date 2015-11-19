# check is compiled with autotools till now, gliang Nov 17, 2015 in rouceforge
#find_package(Check REQUIRED)


include_directories(
    ${INCLUDE_DIRECTORIES}
    ${CMAKE_SOURCE_DIR}/clib/src
    /usr/include

)

link_directories(
    ${CMAKE_BINARY_DIR}/clib/src
    /usr/lib64

)

add_executable(check_isti_str check_isti_str.c)
target_link_libraries(check_isti_str isti_clib check)
add_test(check_isti_str ${CMAKE_CURRENT_BINARY_DIR}/check_isti_str)

