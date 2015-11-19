

set(clib_headers
isti_array.h
isti_cond.h
isti_corm.h
isti_db.h
isti_flow.h
isti.h
isti_ins.h
isti_log.h
isti_mem.h
isti_odbc.h
isti_sql.h
isti_sqlite.h
isti_str.h
)

set(clib_sources
isti_array.c
#isti_cond.c
#isti_ins.c
isti_log.c
isti_mem.c
#isti_odbc.c
#isti_sql.c
#isti_sqlite.c
isti_str.c
)

add_library(isti_clib SHARED ${clib_headers} ${clib_sources})

