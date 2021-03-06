#include <check.h>

/* example.c -- usage example of the zlib compression library
 * Copyright (C) 1995-2006 Jean-loup Gailly.
 * For conditions of distribution and use, see copyright notice in zlib.h
 */

/* @(#) $Id: example.c,v 1.3 2010/07/15 14:24:17 mwebster Exp $ */

/* Gang Liang - modify this well written tests using check for unit tests 
 *  keep the original code
 *  to use teardown() setup()
 * */

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
Byte *compr, *uncompr;
uLong comprLen, uncomprLen;
static const char* myVersion;


const char dictionary[] = "hello";
uLong dictId; /* Adler32 value of the dictionary */

void test_compress      OF((Byte *compr, uLong comprLen,
                            Byte *uncompr, uLong uncomprLen));
void test_gzio          OF((const char *fname,
                            Byte *uncompr, uLong uncomprLen));
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
int  disable_main               OF((int argc, char *argv[]));

/* ===========================================================================
 * Test compress() and uncompress()
 */
void test_compress(compr, comprLen, uncompr, uncomprLen)
    Byte *compr, *uncompr;
    uLong comprLen, uncomprLen;
{
    int err;
    uLong len = (uLong)strlen(hello)+1;

    err = compress(compr, &comprLen, (const Bytef*)hello, len);
    ck_assert_msg(err ==Z_OK, "compress");

    strcpy((char*)uncompr, "garbage");

    err = uncompress(uncompr, &uncomprLen, compr, comprLen);
    ck_assert_msg(err==Z_OK, "uncompress");

    if (strcmp((char*)uncompr, hello)) {
        ck_abort_msg("bad uncompress\n");
    } else {
        printf("uncompress(): %s\n", (char *)uncompr);
    }
}

START_TEST(check_compress)
{
    ck_assert(compr != Z_NULL);
    ck_assert(uncompr != Z_NULL);

    int err;
    uLong len = (uLong)strlen(hello)+1;

    ck_assert_str_eq(hello,"hello, hello!");
    // why Len address?
    err = compress(compr, &comprLen, (const Bytef*)hello, len);
    ck_assert_int_eq(err,0);
    strcpy((char*)uncompr, "garbage");
    printf("uncompre strcpy %s\n", (char *)uncompr);
    
    err = uncompress(uncompr, &uncomprLen, compr, comprLen);
    ck_assert_int_eq(err,0);
    ck_assert_str_eq((char*)uncompr, hello);

}
END_TEST

/* ===========================================================================
 * Test read/write of .gz files
 */
void test_gzio(fname, uncompr, uncomprLen)
    const char *fname; /* compressed file name */
    Byte *uncompr;
    uLong uncomprLen;
{
#ifdef NO_GZCOMPRESS
    fprintf(stderr, "NO_GZCOMPRESS -- gz* functions cannot compress\n");
#else
    int err;
    int len = (int)strlen(hello)+1;
    gzFile file ;
    z_off_t pos;

    file = gzopen(fname, "wb");
    if (file == NULL) {
        fprintf(stderr, "gzopen error\n");
        exit(1);
    }
    gzputc(file, 'h');
    if (gzputs(file, "ello") != 4) {
        fprintf(stderr, "gzputs err: %s\n", gzerror(file, &err));
        exit(1);
    }
    if (gzprintf(file, ", %s!", "hello") != 8) {
        fprintf(stderr, "gzprintf err: %s\n", gzerror(file, &err));
        exit(1);
    }
    gzseek(file, 1L, SEEK_CUR); /* add one zero byte */
    gzclose(file);

    file = gzopen(fname, "rb");
    if (file == NULL) {
        fprintf(stderr, "gzopen error\n");
        exit(1);
    }
    strcpy((char*)uncompr, "garbage");

    if (gzread(file, uncompr, (unsigned)uncomprLen) != len) {
        fprintf(stderr, "gzread err: %s\n", gzerror(file, &err));
        exit(1);
    }
    if (strcmp((char*)uncompr, hello)) {
        fprintf(stderr, "bad gzread: %s\n", (char*)uncompr);
        exit(1);
    } else {
        printf("gzread(): %s\n", (char*)uncompr);
    }

    pos = gzseek(file, -8L, SEEK_CUR);
    if (pos != 6 || gztell(file) != pos) {
        fprintf(stderr, "gzseek error, pos=%ld, gztell=%ld\n",
                (long)pos, (long)gztell(file));
        exit(1);
    }

    if (gzgetc(file) != ' ') {
        fprintf(stderr, "gzgetc error\n");
        exit(1);
    }

    if (gzungetc(' ', file) != ' ') {
        fprintf(stderr, "gzungetc error\n");
        exit(1);
    }

    gzgets(file, (char*)uncompr, (int)uncomprLen);
    if (strlen((char*)uncompr) != 7) { /* " hello!" */
        fprintf(stderr, "gzgets err after gzseek: %s\n", gzerror(file, &err));
        exit(1);
    }
    if (strcmp((char*)uncompr, hello + 6)) {
        fprintf(stderr, "bad gzgets after gzseek\n");
        exit(1);
    } else {
        printf("gzgets() after gzseek: %s\n", (char*)uncompr);
    }

    gzclose(file);
#endif
}

START_TEST(check_gzio)
{

    ck_assert(compr != Z_NULL);
    ck_assert(uncompr != Z_NULL);
#ifdef NO_GZCOMPRESS
    fprintf(stderr, "NO_GZCOMPRESS -- gz* functions cannot compress\n");
#else

    int err;
    int len = (int)strlen(hello)+1;
    gzFile file;
    z_off_t pos;

    file = gzopen(TESTFILE, "wb");
    ck_assert_msg(file != NULL, "Error with gzopen\n");

    gzputc(file, 'h');
    ck_assert_msg(gzputs(file, "ello") == 4, "ERR:gputs \n");

    ck_assert_msg(gzprintf(file, ", %s!", "hello") == 8, "ERR: gprintf\n");

    gzseek(file, 1L, SEEK_CUR); /* add one zero byte */
    gzclose(file);

    file = gzopen(TESTFILE, "rb");
    ck_assert_msg(file != NULL, "gzopen error\n");

    strcpy((char*)uncompr, "garbage");
    if (gzread(file, uncompr, (unsigned)uncomprLen) != len) {
        ck_abort_msg( gzerror(file, &err));
    }
    if (strcmp((char*)uncompr, hello)) {
        fprintf(stderr, "bad gzread: %s\n", (char*)uncompr);
        ck_abort_msg("bad gzread\n");
    } else {
        printf("gzread(): %s\n", (char*)uncompr);
    }

    pos = gzseek(file, -8L, SEEK_CUR);
    ck_assert_msg(pos ==6,"gzseek error\n");
    ck_assert_msg(gztell(file) == pos, "gzseek error\n");

    ck_assert_msg( gzgetc(file) == ' ', "gzgetc error\n");

    if (gzungetc(' ', file) != ' ') {
        ck_abort_msg("gzungetc error\n");
    }

    gzgets(file, (char*)uncompr, (int)uncomprLen);
    if (strlen((char*)uncompr) != 7) { /* " hello!" */
        fprintf(stderr, "gzgets err after gzseek: %s\n", gzerror(file, &err));
        ck_abort_msg(gzerror(file,&err));
    }

    if (strcmp((char*)uncompr, hello + 6)) {
        ck_abort_msg("bad gzgets after gzseek\n");
    } else {
        printf("gzgets() after gzseek: %s\n", (char*)uncompr);
    }

    gzclose(file);
#endif

}
END_TEST

/* ===========================================================================
 * Test deflate() with small buffers
 */
START_TEST(check_deflate)
{
    z_stream c_stream; /* compression stream */
    int err;
    uLong len = (uLong)strlen(hello)+1;

    c_stream.zalloc = (alloc_func)0;
    c_stream.zfree = (free_func)0;
    c_stream.opaque = (voidpf)0;

    err = deflateInit(&c_stream, Z_DEFAULT_COMPRESSION);
    ck_assert_msg(err ==Z_OK, "deflateInit");

    c_stream.next_in  = (Bytef*)hello;
    c_stream.next_out = compr;

    while (c_stream.total_in != len && c_stream.total_out < comprLen) {
        c_stream.avail_in = c_stream.avail_out = 1; /* force small buffers */
        err = deflate(&c_stream, Z_NO_FLUSH);
        ck_assert_msg(err==Z_OK, "deflate");
    }
    /* Finish the stream, still forcing small buffers: */
    for (;;) {
        c_stream.avail_out = 1;
        err = deflate(&c_stream, Z_FINISH);
        if (err == Z_STREAM_END) break;
        ck_assert_msg(err==Z_OK, "deflate");
    }

    err = deflateEnd(&c_stream);
    ck_assert_msg(err==Z_OK, "deflateEnd");
}
END_TEST
/* ===========================================================================
 * Test inflate() with small buffers
 */
START_TEST(check_inflate)
{

    ck_assert(compr != Z_NULL);
    ck_assert(uncompr != Z_NULL);
    printf("***check_inflate() start\n");

    int err;
    z_stream d_stream; /* decompression stream */

    /* this is the compre required for this test
     *
     * gliang 
     */
    uLong len = (uLong)strlen(hello)+1;
    err = compress(compr, &comprLen, (const Bytef*)hello, len);
    
    strcpy((char*)uncompr, "garbage");
    ck_assert_str_eq( (char*)uncompr, "garbage");
    //ck_assert_msg((char*)uncompr == "garbage", "strcpy uncompre %s\n", (char*)uncompr);

    d_stream.zalloc = (alloc_func)0;
    d_stream.zfree = (free_func)0;
    d_stream.opaque = (voidpf)0;

    d_stream.next_in  = compr;
    d_stream.avail_in = 0;
    d_stream.next_out = uncompr;

    err = inflateInit(&d_stream);
    ck_assert_msg(err==Z_OK, "inflateInit");

    printf("check_inflate(): compreLen:%d,UncompreLen:%d uncompre:%s\n", comprLen, uncomprLen,(char*)uncompr);

    while (d_stream.total_out < uncomprLen && d_stream.total_in < comprLen) {
        d_stream.avail_in = d_stream.avail_out = 1; /* force small buffers */
        err = inflate(&d_stream, Z_NO_FLUSH);
        //printf("check_inflate inflate  return err: %d break Z_STREAM_END:%d\n", err, Z_STREAM_END);
        if (err == Z_STREAM_END) {
            break;
        }
        ck_assert_msg(err == Z_OK, "check_inflate expect:%d, but got:%d\n",Z_OK,err);
    }

    err = inflateEnd(&d_stream);
    ck_assert_msg(err==Z_OK, "inflateEnd");

    if (strcmp((char*)uncompr, hello)) {
        ck_abort_msg("bad inflate\n");
    } else {
        printf("inflate(): %s\n", (char *)uncompr);
    }
    printf("***check_inflate() end\n");

}
END_TEST
/* ===========================================================================
 * Test deflate() with large buffers and dynamic change of compression level
 */
void test_large_deflate(compr, comprLen, uncompr, uncomprLen)
    Byte *compr, *uncompr;
    uLong comprLen, uncomprLen;
{
    z_stream c_stream; /* compression stream */
    int err;

    c_stream.zalloc = (alloc_func)0;
    c_stream.zfree = (free_func)0;
    c_stream.opaque = (voidpf)0;

    err = deflateInit(&c_stream, Z_BEST_SPEED);
    CHECK_ERR(err, "deflateInit");

    c_stream.next_out = compr;
    c_stream.avail_out = (uInt)comprLen;

    /* At this point, uncompr is still mostly zeroes, so it should compress
     * very well:
     */
    c_stream.next_in = uncompr;
    c_stream.avail_in = (uInt)uncomprLen;
    err = deflate(&c_stream, Z_NO_FLUSH);
    CHECK_ERR(err, "deflate");
    if (c_stream.avail_in != 0) {
        fprintf(stderr, "deflate not greedy\n");
        exit(1);
    }

    /* Feed in already compressed data and switch to no compression: */
    deflateParams(&c_stream, Z_NO_COMPRESSION, Z_DEFAULT_STRATEGY);
    c_stream.next_in = compr;
    c_stream.avail_in = (uInt)comprLen/2;
    err = deflate(&c_stream, Z_NO_FLUSH);
    CHECK_ERR(err, "deflate");

    /* Switch back to compressing mode: */
    deflateParams(&c_stream, Z_BEST_COMPRESSION, Z_FILTERED);
    c_stream.next_in = uncompr;
    c_stream.avail_in = (uInt)uncomprLen;
    err = deflate(&c_stream, Z_NO_FLUSH);
    CHECK_ERR(err, "deflate");

    err = deflate(&c_stream, Z_FINISH);
    if (err != Z_STREAM_END) {
        fprintf(stderr, "deflate should report Z_STREAM_END\n");
        exit(1);
    }
    err = deflateEnd(&c_stream);
    CHECK_ERR(err, "deflateEnd");
}

/* ===========================================================================
 * Test inflate() with large buffers
 */
void test_large_inflate(compr, comprLen, uncompr, uncomprLen)
    Byte *compr, *uncompr;
    uLong comprLen, uncomprLen;
{
    int err;
    z_stream d_stream; /* decompression stream */

    strcpy((char*)uncompr, "garbage");

    d_stream.zalloc = (alloc_func)0;
    d_stream.zfree = (free_func)0;
    d_stream.opaque = (voidpf)0;

    d_stream.next_in  = compr;
    d_stream.avail_in = (uInt)comprLen;

    err = inflateInit(&d_stream);
    CHECK_ERR(err, "inflateInit");

    for (;;) {
        d_stream.next_out = uncompr;            /* discard the output */
        d_stream.avail_out = (uInt)uncomprLen;
        err = inflate(&d_stream, Z_NO_FLUSH);
        if (err == Z_STREAM_END) break;
        CHECK_ERR(err, "large inflate");
    }

    err = inflateEnd(&d_stream);
    CHECK_ERR(err, "inflateEnd");

    if (d_stream.total_out != 2*uncomprLen + comprLen/2) {
        fprintf(stderr, "bad large inflate: %ld\n", d_stream.total_out);
        exit(1);
    } else {
        printf("large_inflate(): OK\n");
    }
}

/* ===========================================================================
 * Test deflate() with full flush
 */
START_TEST(check_flush)
{
    int err;

    // compr, comprLen to be init

    z_stream c_stream; /* compression stream */
    uInt len = (uInt)strlen(hello)+1;

    c_stream.zalloc = (alloc_func)0;
    c_stream.zfree = (free_func)0;
    c_stream.opaque = (voidpf)0;

    err = deflateInit(&c_stream, Z_DEFAULT_COMPRESSION);
    ck_assert_msg(err==Z_OK, "deflateInit got:%d\n",err);

    c_stream.next_in  = (Bytef*)hello;
    c_stream.next_out = compr;
    c_stream.avail_in = 3;
    c_stream.avail_out = (uInt)comprLen;
    err = deflate(&c_stream, Z_FULL_FLUSH);
    ck_assert_msg(err==Z_OK, "deflate");

    compr[3]++; /* force an error in first compressed block */
    c_stream.avail_in = len - 3;

    err = deflate(&c_stream, Z_FINISH);
    if (err != Z_STREAM_END) {
        ck_assert_msg(err==Z_OK, "deflate");
    }

    err = deflateEnd(&c_stream);
    ck_assert_msg(err==Z_OK, "deflateEnd");
    comprLen = c_stream.total_out;
    printf("***check_flush() ends with comprLen:%d compre:%s\n",comprLen,(char*)compr);
}
END_TEST

/* ===========================================================================
 * Test inflateSync()
 */
START_TEST(check_sync)
{
    int err;

    // compr, comprLen to be init from output check_flush
    // copied from test flush
    // end test_flush

    z_stream d_stream; /* decompression stream */
    printf("***inflateSync() starts with: hel%s\n", (char *)compr);

    strcpy((char*)uncompr, "garbage");

    d_stream.zalloc = (alloc_func)0;
    d_stream.zfree = (free_func)0;
    d_stream.opaque = (voidpf)0;

    d_stream.next_in  = compr;
    d_stream.avail_in = 2; /* just read the zlib header */

    err = inflateInit(&d_stream);
    ck_assert_msg(err==Z_OK, "inflateInit got:%d\n",err);

    d_stream.next_out = uncompr;
    d_stream.avail_out = (uInt)uncomprLen;

    inflate(&d_stream, Z_NO_FLUSH);
    ck_assert_msg(err==Z_OK, "inflate got:%d\n",err);

    d_stream.avail_in = (uInt)comprLen-2;   /* read all compressed data */
    err = inflateSync(&d_stream);           /* but skip the damaged part */
    ck_assert_msg(err==Z_OK, "inflateSync got:%d\n",err);

    err = inflate(&d_stream, Z_FINISH);
    if (err != Z_DATA_ERROR) {
        ck_abort_msg("inflate should report DATA_ERROR\n");
        /* Because of incorrect adler32 */
    }
    err = inflateEnd(&d_stream);
    ck_assert_msg(err==Z_OK, "inflateEnd got:%d\n",err);

    printf("***inflateSync() ends with: hel%s\n", (char *)uncompr);
}
END_TEST
/* ===========================================================================
 * Test deflate() with preset dictionary
 */
void test_dict_deflate(compr, comprLen)
    Byte *compr;
    uLong comprLen;
{
    z_stream c_stream; /* compression stream */
    int err;

    c_stream.zalloc = (alloc_func)0;
    c_stream.zfree = (free_func)0;
    c_stream.opaque = (voidpf)0;

    err = deflateInit(&c_stream, Z_BEST_COMPRESSION);
    CHECK_ERR(err, "deflateInit");

    err = deflateSetDictionary(&c_stream,
                               (const Bytef*)dictionary, sizeof(dictionary));
    CHECK_ERR(err, "deflateSetDictionary");

    dictId = c_stream.adler;
    c_stream.next_out = compr;
    c_stream.avail_out = (uInt)comprLen;

    c_stream.next_in = (Bytef*)hello;
    c_stream.avail_in = (uInt)strlen(hello)+1;

    err = deflate(&c_stream, Z_FINISH);
    if (err != Z_STREAM_END) {
        fprintf(stderr, "deflate should report Z_STREAM_END\n");
        exit(1);
    }
    err = deflateEnd(&c_stream);
    CHECK_ERR(err, "deflateEnd");
}

/* ===========================================================================
 * Test inflate() with a preset dictionary
 */
START_TEST(check_dict_inflate)
{
    if (compr == Z_NULL || uncompr == Z_NULL) {
        ck_abort_msg("out of memory\n");
    }

    int err;
    z_stream d_stream; /* decompression stream */
    strcpy((char*)uncompr, "garbage");

    d_stream.zalloc = (alloc_func)0;
    d_stream.zfree = (free_func)0;
    d_stream.opaque = (voidpf)0;

    d_stream.next_in  = compr;
    d_stream.avail_in = (uInt)comprLen;

    err = inflateInit(&d_stream);
    ck_assert_msg(err ==Z_OK, "inflateInit");

    d_stream.next_out = uncompr;
    d_stream.avail_out = (uInt)uncomprLen;

    for (;;) {
        err = inflate(&d_stream, Z_NO_FLUSH);
        if (err == Z_STREAM_END) break;
        if (err == Z_NEED_DICT) {
            if (d_stream.adler != dictId) {
                ck_abort_msg("unexpected dictionary");
            }
            err = inflateSetDictionary(&d_stream, (const Bytef*)dictionary,
                                       sizeof(dictionary));
        }
        ck_assert_msg(err == Z_OK, "inflate with dict");
    }
    err = inflateEnd(&d_stream);
    ck_assert_msg(err == Z_OK, "inflateEnd");

    if (strcmp((char*)uncompr, hello)) {
        ck_abort_msg("bad inflate with dict\n");
    } else {
        printf("inflate with dictionary: %s\n", (char *)uncompr);
    }
}
END_TEST

void test_dict_inflate(compr, comprLen, uncompr, uncomprLen)
    Byte *compr, *uncompr;
    uLong comprLen, uncomprLen;
{
    int err;
    z_stream d_stream; /* decompression stream */

    strcpy((char*)uncompr, "garbage");

    d_stream.zalloc = (alloc_func)0;
    d_stream.zfree = (free_func)0;
    d_stream.opaque = (voidpf)0;

    d_stream.next_in  = compr;
    d_stream.avail_in = (uInt)comprLen;

    err = inflateInit(&d_stream);
    CHECK_ERR(err, "inflateInit");

    d_stream.next_out = uncompr;
    d_stream.avail_out = (uInt)uncomprLen;

    for (;;) {
        err = inflate(&d_stream, Z_NO_FLUSH);
        if (err == Z_STREAM_END) break;
        if (err == Z_NEED_DICT) {
            if (d_stream.adler != dictId) {
                fprintf(stderr, "unexpected dictionary");
                exit(1);
            }
            err = inflateSetDictionary(&d_stream, (const Bytef*)dictionary,
                                       sizeof(dictionary));
        }
        CHECK_ERR(err, "inflate with dict");
    }

    err = inflateEnd(&d_stream);
    CHECK_ERR(err, "inflateEnd");

    if (strcmp((char*)uncompr, hello)) {
        fprintf(stderr, "bad inflate with dict\n");
        exit(1);
    } else {
        printf("inflate with dictionary: %s\n", (char *)uncompr);
    }
}

/* ===========================================================================
 * Usage:  example [output.gz  [input.gz]]
 */
void teardown(void){
    free(compr);
    free(uncompr);
}


int disable_main(argc, argv)
    int argc;
    char *argv[];
{
    Byte *compr, *uncompr;
    uLong comprLen = 10000*sizeof(int); /* don't overflow on MSDOS */
    uLong uncomprLen = comprLen;
    static const char* myVersion = ZLIB_VERSION;

    if (zlibVersion()[0] != myVersion[0]) {
        fprintf(stderr, "incompatible zlib version\n");
        exit(1);

    } else if (strcmp(zlibVersion(), ZLIB_VERSION) != 0) {
        fprintf(stderr, "warning: different zlib version\n");
    }

    printf("zlib version %s = 0x%04x, compile flags = 0x%lx\n",
            ZLIB_VERSION, ZLIB_VERNUM, zlibCompileFlags());

    compr    = (Byte*)calloc((uInt)comprLen, 1);
    uncompr  = (Byte*)calloc((uInt)uncomprLen, 1);
    /* compr and uncompr are cleared to avoid reading uninitialized
     * data and to ensure that uncompr compresses well.
     */
    if (compr == Z_NULL || uncompr == Z_NULL) {
        printf("out of memory\n");
        exit(1);
    }
    test_compress(compr, comprLen, uncompr, uncomprLen);

    test_gzio((argc > 1 ? argv[1] : TESTFILE),
              uncompr, uncomprLen);

    //test_deflate(compr, comprLen);
    //test_inflate(compr, comprLen, uncompr, uncomprLen);

    test_large_deflate(compr, comprLen, uncompr, uncomprLen);
    test_large_inflate(compr, comprLen, uncompr, uncomprLen);

   // test_flush(compr, &comprLen);
    //test_sync(compr, comprLen, uncompr, uncomprLen);

    comprLen = uncomprLen;
    test_dict_deflate(compr, comprLen);
    test_dict_inflate(compr, comprLen, uncompr, uncomprLen);

    free(compr);
    free(uncompr);

    return 0;
}



Suite * compress_suite(void)
{
    Suite *s;
    TCase *tc_core;

    comprLen = 10000*sizeof(int); /* don't overflow on MSDOS */
    uncomprLen = comprLen;
    myVersion = ZLIB_VERSION;

    if (zlibVersion()[0] != myVersion[0]) {
        fprintf(stderr, "incompatible zlib version\n");
        exit(1);

    } else if (strcmp(zlibVersion(), ZLIB_VERSION) != 0) {
        fprintf(stderr, "warning: different zlib version\n");
    }

    printf("zlib version %s = 0x%04x, compile flags = 0x%lx\n",
            ZLIB_VERSION, ZLIB_VERNUM, zlibCompileFlags());

    compr    = (Byte*)calloc((uInt)comprLen, 1);
    uncompr  = (Byte*)calloc((uInt)uncomprLen, 1);
    /* compr and uncompr are cleared to avoid reading uninitialized
     * data and to ensure that uncompr compresses well.
     */
    if (compr == Z_NULL || uncompr == Z_NULL) {
        printf("out of memory\n");
        exit(1);
    }

    s = suite_create("zlibSuite");
    /*Core test case */
    tc_core = tcase_create("Core");
    // compr uncompr changed by each test in exact order
    // this is the flaw of these tests
    // disable this setup for each test
    //tcase_add_checked_fixture(tc_core,setup,teardown);
    suite_add_tcase(s, tc_core);

    tcase_add_test(tc_core, check_compress);
    tcase_add_test(tc_core, check_gzio);

    tcase_add_test(tc_core, check_deflate);
    tcase_add_test(tc_core, check_inflate);

    //test_large_deflate(compr, comprLen, uncompr, uncomprLen);
    //test_large_inflate(compr, comprLen, uncompr, uncomprLen);
    

    tcase_add_test(tc_core, check_flush);
    tcase_add_test(tc_core, check_sync);

    /*

    comprLen = uncomprLen;
    test_dict_deflate(compr, comprLen);
    tcase_add_test(tc_core, check_dict_inflate);
*/
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

