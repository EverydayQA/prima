
cmake_minimum_required(VERSION 2.6)
enable_testing()
include(CTest)

include_directories(
    ${CMAKE_SOURCE_DIR}/include
    /usr/include
)

add_subdirectory(lib)
add_subdirectory(tests)


