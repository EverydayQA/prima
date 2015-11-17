cmake_minimum_required(VERSION 2.8)

# set_property(TARGET tgt PROPERTY C_STANDARD 99)
set(CMAKE_C_FLAGS "-std=gnu99")
project(isti_clib)
enable_testing()
add_subdirectory(src)
add_subdirectory(tests)

