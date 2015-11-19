
BASE_TESTS = check_isti_sql check_isti_str check_isti_array \
	check_isti_ins check_isti_log check_isti_cond \
	check_array_foo
SQLITE3_TESTS = check_isti_sqlite check_dynamic check_select_foo \
	check_insert_foo check_delete_foo
ODBC_TESTS = check_isti_odbc

TESTS = $(BASE_TESTS)
if HAVE_SQLITE3
TESTS += $(SQLITE3_TESTS)
endif
if HAVE_ODBC
if HAVE_DSN
TESTS += $(ODBC_TESTS)
endif
endif

check_PROGRAMS = $(TESTS)

AM_CFLAGS = @CHECK_CFLAGS@ $(all_includes) -I../src/ -g -O0 \
	-Wall -Werror -Wconversion
LDADD = $(top_builddir)/clib/src/libcorm.la @CHECK_LIBS@
if HAVE_SQLITE3
LDADD += -lsqlite3
endif
if HAVE_ODBC
LDADD += -lodbc
endif

check_dynamic_SOURCES = check_dynamic.c 
check_isti_dynamicdir= .
check_isti_dynamic_DATA= check_isti_sqlite.db

check_isti_sql_SOURCES = check_isti_sql.c 

check_isti_str_SOURCES = check_isti_str.c 

check_isti_sqlite_SOURCES = check_isti_sqlite.c check_isti_sqlite.db
check_isti_sqlitedir= .
check_isti_sqlite_DATA= check_isti_sqlite.db

check_isti_odbc_SOURCES = foo.corm.c check_isti_odbc.c
check_isti_odbcdir= .
check_isti_odbc_DATA= check_isti_odbc.db

check_isti_array_SOURCES = check_isti_array.c

check_isti_ins_SOURCES = check_isti_ins.c

check_isti_cond_SOURCES = check_isti_cond.c

check_isti_log_SOURCES = check_isti_log.c

check_array_foo_SOURCES = foo.corm.c check_array_foo.c

check_select_foo_SOURCES = foo.corm.c check_select_foo.c
check_select_foodir= .
check_select_foo_DATA= check_foo.db

check_insert_foo_SOURCES = foo.corm.c check_insert_foo.c
check_insert_foodir= .
check_insert_foo_DATA= check_foo.db

check_delete_foo_SOURCES = foo.corm.c check_delete_foo.c
check_delete_foodir= .
check_delete_foo_DATA= check_foo.db

%.corm.h %.corm.c %.corm.sql: %.h
	PYTHONPATH=../../cgen/src ../../cgen/env/bin/python ../../cgen/src/isti/cgen/run.py $<

check_foo.db: foo.corm.sql
	./check_foo.sh

check_isti_sqlite.db: check_isti_sqlite.sql
	./check_isti_sqlite.sh

check_isti_odbc.db: check_isti_odbc.sql
	./check_isti_odbc.sh

clean-local:
	rm -f *.corm.h *.corm.c *.corm.sql
	rm -f *.o
	rm -f *.db
