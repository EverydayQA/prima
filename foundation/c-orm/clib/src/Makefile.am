
lib_LTLIBRARIES = libcorm.la

AM_LDFLAGS = -version-info 0:0:0
AM_CFLAGS = -g -O0 -Wconversion -Wall -Werror

libcorm_la_SOURCES = isti_db.h isti_flow.h isti_mem.c isti_sql.c \
	isti_str.c isti_cond.c isti_array.c isti_ins.c isti_log.c
if HAVE_SQLITE3
libcorm_la_SOURCES += isti_sqlite.c
endif
if HAVE_ODBC
libcorm_la_SOURCES += isti_odbc.c
endif
