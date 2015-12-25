cmake_minimum_required (VERSION 2.8)

find_package(Java REQUIRED)
include(UseJava)

enable_testing()

project (sort)

set(CMAKE_JAVA_COMPILE_FLAGS "-source" "1.6" "-target" "1.6")

add_jar(sort sort.java)

get_target_property(_jarFile sort JAR_FILE)
get_target_property(_classDir sort CLASSDIR)

message(STATUS "Jar file ${_jarFile}")
message(STATUS "Class compiled to ${_classDir}")

add_test(NAME Testsort COMMAND ${Java_JAVA_EXECUTABLE} -cp ${_jarFile} sort)
