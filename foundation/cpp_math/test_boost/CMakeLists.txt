
#find_package(GTest REQUIRED)
#include_directories(${GTEST_INCLUDE_DIRS})
#set(CMAKE_FIND_LIBRARY_SUFFIXES .so)

set(Boost_USE_SHARED_LIBS ON)
set(Boost_USE_MULTITHREADED ON)
find_library(DIM_SHARED_LIBRARY NAMES libboost_date_time.so)
find_package(Boost COMPONENTS unit_test_framework REQUIRED SHARED)
include_directories(
    ${INCLUDE_DIRECTORIES}
    ${Boost_INCLUDE_DIRS}
)

add_subdirectory(test)
