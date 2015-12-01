set(libmoney1_la_SOURCES
    money.1.c money.h
)
set(libmoney3_la_SOURCES
    money.3.c money.h
)
set(libmoney4_la_SOURCES
    money.4.c money.h
)
set(libmoney5_la_SOURCES
    money.5.c money.h
)

set(libmoney_la_SOURCES
    money.c money.h
)


add_library(money1 ${libmoney1_la_SOURCES})
add_library(money3 ${libmoney3_la_SOURCES})
add_library(money4 ${libmoney4_la_SOURCES})
add_library(money5 ${libmoney5_la_SOURCES})

add_library(money ${libmoney_la_SOURCES})
add_executable(main main.c)
target_link_libraries(main money)

