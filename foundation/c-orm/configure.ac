AC_INIT([corm], [0.1], [a.cooke@isti.com])
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([-Wall foreign -Werror])
AC_PROG_CC_C99
AM_PROG_CC_C_O
LT_INIT
AC_CONFIG_HEADERS([config.h])
AC_CONFIG_FILES([Makefile clib/Makefile clib/src/Makefile clib/tests/Makefile clib/docs/Makefile cgen/Makefile cgen/docs/Makefile example/Makefile example/src/Makefile])

PKG_CHECK_MODULES([CHECK], [check >= 0.9.4]) 

AC_CHECK_PROG([PYTHON34], [python3.4], [yes])
if test -z "$PYTHON34"; then
  AC_MSG_ERROR([python3.4 not found])
fi

AC_CHECK_PROG([PYVENV34], [pyvenv-3.4], [yes])
if test -z "$PYVENV34"; then
  AC_MSG_ERROR([pyvenv-3.4 not found])
fi

AC_CHECK_PROG([DOXYGEN], [doxygen], [yes])
AM_CONDITIONAL([HAVE_DOXYGEN], [test -n "$DOXYGEN"])
AM_COND_IF([HAVE_DOXYGEN], 
  [AC_CONFIG_FILES([clib/docs/Doxyfile cgen/docs/Doxyfile])],
  [AC_MSG_WARN([Doxygen not found - continuing without Doxygen support])])

AC_CHECK_LIB([sqlite3], [sqlite3_open], [SQLITE3=yes],
  [AC_MSG_WARN([SQLite3 not found - continuing without SQLite3 support])])
AM_CONDITIONAL([HAVE_SQLITE3], [test -n "$SQLITE3"])

AC_CHECK_LIB([odbc], [SQLConnect], [ODBC=yes],
  [AC_MSG_WARN([ODBC not found - continuing without ODBC support])])
AC_CHECK_HEADERS([sql.h sqlext.h], [ODBCH=yes],
  [AC_MSG_WARN([ODBC headers not found - continuing without ODBC support])])
AM_CONDITIONAL([HAVE_ODBC], [test -n "$ODBC" -a -n "$ODBCH"])

AC_ARG_WITH([test-dsn],
  [AC_HELP_STRING([--with-test-dsn], [the DSN to use to check ODBC support])],
  [DSN=$with_test_dsn],
  [AC_MSG_WARN([No DSN specified for ODBC tests (--with-test-dsn=...)])])
AM_CONDITIONAL([HAVE_DSN], [test -n "$DSN"])
AM_COND_IF([HAVE_DSN],
  [CPPFLAGS+="-DDSN=\"$DSN\""])

AC_ARG_ENABLE(debug,
  [  --enable-debug          enable debug],
  [CFLAGS="$CFLAGS -g"])
AC_ARG_ENABLE(optimisation,
  [  --enable-optimaisation  enable optimisation],
  [CFLAGS="$CFLAGS -O2"],
  [CFLAGS="$CFLAGS -O0"])

AC_OUTPUT
