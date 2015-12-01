#include <check.h>
/* example.c -- usage example of the zlib compression library
 * Copyright (C) 1995-2006 Jean-loup Gailly.
 * For conditions of distribution and use, see copyright notice in zlib.h
 */

/* @(#) $Id: example.c,v 1.3 2010/07/15 14:24:17 mwebster Exp $ */

#include "zlib.h"
#include <stdio.h>
#include "check_proto.h"
#ifdef STDC
#  include <string.h>
#  include <stdlib.h>
#endif

#if defined(VMS) || defined(RISCOS)
#  define TESTFILE "foo-gz"
#else
#  define TESTFILE "foo.gz"
#endif


/*
 * Runs the specified test suite.
 */
void check_run_suite(Suite *suite, const char *file)
{
    SRunner *srunner;
    srunner = srunner_create(suite);
    srunner_run_all(srunner, CK_NORMAL);
    srunner_ntests_failed(srunner);
    srunner_free(srunner);
}

/* The main unit test function. Calls other functions to do the unit
 * tests. */
void main(int argc, char **argv)
{
    int i;
    check_compress();
}
