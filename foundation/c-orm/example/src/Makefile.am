
bin_PROGRAMS =
if HAVE_SQLITE3
bin_PROGRAMS += phonebook1 phonebook3
endif

AM_CFLAGS=-g -O0 -Wall -Werror -Wconversion
AM_CPPFLAGS=-I../../clib/src
AM_LDFLAGS=-L../../clib/src/.libs
LDADD=-lcorm -lsqlite3

# order critical here - corm before user
phonebook1_SOURCES= phonebook.corm.c phonebook1.c
phonebook3_SOURCES= phonebook.corm.c phonebook3.c

# do the corm magic, parsing phonebook.h to generate the .corm. files
%.corm.h %.corm.c %.corm.sql: %.h
	PYTHONPATH=../../cgen/src ../../cgen/env/bin/python ../../cgen/src/isti/cgen/run.py $<

clean-local:
	rm -f *.corm.h *.corm.c *.corm.sql
	rm -f *.o

