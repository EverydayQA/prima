
find_package(Threads REQUIRED)

set (foomath_SRCS
Addition.cpp
Multiply.cpp
Addition.hpp
Multiply.hpp
)


# Enable ExternalProject CMake module
include(ExternalProject)

include_directories("${source_dir}/include")
add_library(foomath  ${foomath_SRCS})


