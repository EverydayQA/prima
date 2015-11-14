set(Main_SRCS
    ExampleApp.cpp
)

include_directories(
    ${cmake_binary_dir}/libfoomath
)

add_executable(foomath_app
    ${Main_SRCS}
)

# Specify here the libraries this program depends on
target_link_libraries(foomath_app
    libfoomath
)

install(TARGETS foomath_app DESTINATION bin)
