cmake_minimum_required(VERSION 2.6)
 
project(test)
ENABLE_TESTING()
 
SET(CMAKE_CXX_FLAGS "-g -O0 -Wall -W -Wshadow -Wunused-variable -Wunused-parameter -Wunused-function -Wunused -Wno-system-headers -Wno-deprecated -Woverloaded-virtual -Wwrite-strings -fprofile-arcs -ftest-coverage ")
#set(CPPUNIT_LDFLAGS  "-profile_rt")
#set(CPPUNIT_CPPFLAGS  "-g O0 --coverage")
SET(CMAKE_C_FLAGS "-g -O0 -Wall -W -fprofile-arcs -ftest-coverage")
 
SET(CMAKE_SHARED_LINKER_FLAGS "-fprofile-arcs -ftest-coverage")
SET(CMAKE_EXE_LINKER_FLAGS "-fprofile-arcs -ftest-coverage")
 
add_executable(test test.cc)
target_link_libraries(test cppunit)
 
add_test(NAME test COMMAND test)
