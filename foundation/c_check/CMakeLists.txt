
cmake_minimum_required(VERSION  2.8)
enable_testing()
include(CTest)

add_definitions(-DHAVE_CONFIG_H)
#configure_file(${CMAKE_SOURCE_DIR}/cmake/config.h.cmake ${CMAKE_BINARY_DIR}/config.h @ONLY)


add_subdirectory(src)
add_subdirectory(tests)
