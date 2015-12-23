
set(money_SRCS
money.h
money.c
)

add_library(money SHARED ${money_SRCS})
add_executable(random rand.c)


