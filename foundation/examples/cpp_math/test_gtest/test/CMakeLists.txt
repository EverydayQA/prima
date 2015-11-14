find_package(Threads REQUIRED)

# Enable ExternalProject CMake module
include(ExternalProject)

add_library(libgtest IMPORTED STATIC GLOBAL)
add_dependencies(libgtest gtest)

include_directories("${source_dir}/include")

add_library(libgmock IMPORTED STATIC GLOBAL)
add_dependencies(libgmock gmock)


add_subdirectory(testfoo)
