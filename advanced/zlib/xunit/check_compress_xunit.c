#include <check.h>
/* example.c -- usage example of the zlib compression library
 * Copyright (C) 1995-2006 Jean-loup Gailly.
 * For conditions of distribution and use, see copyright notice in zlib.h
 */

/* @(#) $Id: example.c,v 1.3 2010/07/15 14:24:17 mwebster Exp $ */

#include "zlib.h"
#include <stdio.h>

#ifdef STDC
#  include <string.h>
#  include <stdlib.h>
#endif

#if defined(VMS) || defined(RISCOS)
#  define TESTFILE "foo-gz"
#else
#  define TESTFILE "foo.gz"
#endif

#define CHECK_ERR(err, msg) { \
    if (err != Z_OK) { \
        fprintf(stderr, "%s error: %d\n", msg, err); \
        exit(1); \
    } \
}

const char hello[] = "hello, hello!";
/* "hello world" would be more standard, but the repeated "hello"
 * stresses the compression code better, sorry...
 */

const char dictionary[] = "hello";
uLong dictId; /* Adler32 value of the dictionary */

void test_deflate       OF((Byte *compr, uLong comprLen));
void test_inflate       OF((Byte *compr, uLong comprLen,
                            Byte *uncompr, uLong uncomprLen));
void test_large_deflate OF((Byte *compr, uLong comprLen,
                            Byte *uncompr, uLong uncomprLen));
void test_large_inflate OF((Byte *compr, uLong comprLen,
                            Byte *uncompr, uLong uncomprLen));
void test_flush         OF((Byte *compr, uLong *comprLen));
void test_sync          OF((Byte *compr, uLong comprLen,
                            Byte *uncompr, uLong uncomprLen));
void test_dict_deflate  OF((Byte *compr, uLong comprLen));
void test_dict_inflate  OF((Byte *compr, uLong comprLen,
                            Byte *uncompr, uLong uncomprLen));

START_TEST(test_gzio_xunit)
{
    Byte *uncompr;
    const char *fname; /* compressed file name */
    uLong uncomprLen;

    int err;
    int len = (int)strlen(hello)+1;
    gzFile file;
    z_off_t pos;

    file = gzopen(fname,"wb");
    ck_assert(file == NULL);
    gzputc(file, 'h');
    ck_assert_int_ne(gzputs(file,"ello"),4);

    ck_assert_int_ne(gzprintf(file, ",%s!","hellow"),0);
    gzseek(file, 1L, SEEK_CUR); /* add 1 zero byte */
    gzclose(file);

    file = gzopen(fname,"rb");
    ck_assert(file == NULL);


    gzclose(file);
}
END_TEST

/* ===========================================================================
 * Test compress() and uncompress()
 */

START_TEST(test_compress_xunit)
{
    Byte *compr, *uncompr;
    uLong comprLen = 10000*sizeof(int); /* don't overflow on MSDOS */
    uLong uncomprLen = comprLen;
    static const char* myVersion = ZLIB_VERSION;

    ck_assert_int_eq(zlibVersion()[0] , myVersion[0]); 
    ck_assert_int_eq(5.0,5);
    ck_assert_str_eq(zlibVersion(), ZLIB_VERSION);
    printf("zlib version %s = 0x%04x, compile flags = 0x%lx\n",
            ZLIB_VERSION, ZLIB_VERNUM, zlibCompileFlags());

    compr    = (Byte*)calloc((uInt)comprLen, 1);
    uncompr  = (Byte*)calloc((uInt)uncomprLen, 1);

    ck_assert(compr != Z_NULL);
    ck_assert(uncompr != Z_NULL);

    int err;
    uLong len = (uLong)strlen(hello)+1;

    err = compress(compr, &comprLen, (const Bytef*)hello, len);
    ck_assert_int_eq(err,0);

    strcpy((char*)uncompr, "garbage");
    err = uncompress(uncompr, &uncomprLen, compr, comprLen);
    ck_assert_int_eq(err,0);

    ck_assert_str_eq((char*)uncompr, hello);

}
END_TEST


Suite * compress_suite(void)
{
    Suite *s;
    TCase *tc_core;

    s = suite_create("zlibSuite");
    /*Core test case */
    tc_core = tcase_create("Core");
    tcase_add_test(tc_core, test_compress_xunit);
    tcase_add_test(tc_core, test_gzio_xunit);

    suite_add_tcase(s, tc_core);
    return s;
}


int main(void)
{
    int number_failed;
    Suite *s;
    SRunner *sr;
    s = compress_suite();
    sr = srunner_create(s);
    srunner_run_all(sr, CK_NORMAL);
    number_failed  = srunner_ntests_failed(sr);
    srunner_free(sr);
    return (number_failed ==0) ? EXIT_SUCCESS:EXIT_FAILURE;
}

