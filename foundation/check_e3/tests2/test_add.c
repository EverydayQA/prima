#include <check.h>
#include "test.h"
#include "vector.h"

START_TEST(test_add)
{
    fail_unless(add(2,3)==5,"2+3 == 5");
}
END_TEST

static const int primes[5][3]={{2,3,5},
    {1,2,3},
    {7,9,16},
    {2,2,4},
    {5,6,11}};

START_TEST(loop_test){
    int result = add(primes[_i][0], primes[_i][1]);
    fail_unless(result == primes[_i][2], "Sth wrong with addition");

}
END_TEST

vector v;
START_TEST(vector_loop_test){
    int result = add(primes[_i][0], primes[_i][1]);
    fail_unless(result == primes[_i][2], "Sth wrong with addition");

}
END_TEST

static const int random[5] = {2,3,4,5,6};
START_TEST(check_is_prime){
    fail_unless(is_prime(random[_i])==1,"is_prime pass everything");

}
END_TEST



Suite *make_add_suite2(void){
    Suite *s = suite_create("Add");
    TCase *tc_add = tcase_create("add");
    suite_add_tcase(s, tc_add);
    tcase_add_test(tc_add, test_add);
    tcase_add_loop_test(tc_add,loop_test,0,5);
    tcase_add_loop_test(tc_add,check_is_prime,0,5);
    tcase_add_loop_test(tc_add,vector_loop_test,0,5);

    return s;
}
/*
vector * test_data(char *filename){
    FILE *file = fopen(filename,"r");
    if(file ==NULL){
        printf("could not open file\n");
        exit(EXIT_FAILURE);
    }

    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    vector v;
    vector_init(&v);
    while ((read = getline(&line, &len,file))!=-1){
        printf("Retrieved line of length %zu :\n", read);
        vector_add(&v,line); 
        printf("%s", line);
    }
    fclose(file);
    return v;
}
*/
