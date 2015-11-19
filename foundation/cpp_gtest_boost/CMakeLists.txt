cmake_minimum_required(VERSION 2.8)

enable_testing()
include_directories(
    ${CMAKE_SOURCE_DIR}/libmath

)

link_directories(
    "${cmake_binary_dir}/libmath"
)

add_subdirectory(libmath)
add_subdirectory(main)
add_subdirectory(test_gtest)
add_subdirectory(test_boost)



