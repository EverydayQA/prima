
find_package(Threads REQUIRED)

set (foomath_SRCS
Addition.cpp
Multiply.cpp
# case sensitive - make sense for variable
${CMAKE_SOURCE_DIR}/libmath/Addition.hpp
${CMAKE_CURRENT_SOURCE_DIR}/Multiply.hpp
)


add_library(foomath  ${foomath_SRCS})


