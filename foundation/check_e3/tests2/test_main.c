#include "test.h"
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]){
    if(argc !=2){
        printf("Usage: %s filename", argv[0]);
        exit(EXIT_FAILURE);
    }

    FILE *file = fopen(argv[1],"r");
    if(file ==NULL){
        printf("could not open file\n");
        exit(EXIT_FAILURE);
    }

    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    TestData *tdata; 
    while ((read = getline(&line, &len,file))!=-1){
        printf("Retrieved line of length %zu :\n", read);
        
        printf("%s", line);
    }
    fclose(file);

    /*
     *
     *
     * def struct to hold test data
     *
     */
    int n;
    SRunner *sr;
    sr = srunner_create(make_add_suite());
    srunner_run_all(sr, CK_VERBOSE);
    n = srunner_ntests_failed(sr);
    srunner_free(sr);


    return (n==0)? EXIT_SUCCESS:EXIT_FAILURE;
}
