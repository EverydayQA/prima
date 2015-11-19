cmake_minimum_required(VERSION 2.8)

enable_testing()
# set_property(TARGET tgt PROPERTY C_STANDARD 99)
set(CMAKE_C_FLAGS "-std=c99")
project(c-orm)
add_subdirectory(clib)

