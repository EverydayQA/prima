#include<iostream>
#include<string>
#include <stdlib.h>
#include <stdio.h>
#include <cstring>
using namespace std;
typedef struct Student Student;

struct Student
{
    char name[8];
};

Student  *func_return(Student *s )
{

    s->name[1] = 'S';
    return s;
};

int main()
{
    struct Student *s = malloc(sizeof(Student));

    strcpy(s->name, "abcde");
    s = func_return(s);
    cout << s->name;
};

