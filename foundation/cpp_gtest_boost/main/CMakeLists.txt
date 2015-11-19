set(Main_SRCS
    ExampleApp.cpp
)


add_executable(foomath_app
    ${Main_SRCS}
)

target_link_libraries(foomath_app
    foomath
)

install(TARGETS foomath_app DESTINATION bin)
