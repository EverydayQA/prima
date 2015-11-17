enable_testing()
# check is compiled with autotools till now, gliang Nov 17, 2015 in rouceforge
#find_package(Check REQUIRED)

find_library(CHECK_LIBRARIES 
    NAMES check 
    
    )

include_directories(
    ${INCLUDE_DIRECTORIES}
    ${CMAKE_SOURCE_DIR}/src
    /usr/include

)

set(LIBS ${LIBS} ${CHECK_LIBRARIES} isti_clib)

add_executable(test_isti_str test_isti_str.c)
target_link_libraries(test_isti_str ${LIBS})
add_test(test_isti_str ${CMAKE_CURRENT_BINARY_DIR}/test-isti_str)

