#include <stdlib.h>
#include <stdio.h>
#define HIGH_NUMBER 100
typedef struct Random Random;
Random *isValidNumbers(int *num1,int *num2, int *num3);
struct Random{
    int a;
    int b;
    int c;
};

int main(void)
{
    int num1 = 0;
    int num2 = 0;
    int num3 = 0;
    /* pr to use as parameter, rr used as a return struct , just for demoo purpuse*/
    Random *p;
    p = isValidNumbers(&num1,&num2,&num3);
    printf("%d %d %d main return random numbers\n",num1,num2,num3);    
    printf("%d %d %d main return from struct   \n",p->a,p->b,p->c);    
    return 0;
}

Random *isValidNumbers(int *num1,int *num2, int *num3)
{
    struct Random *r = malloc(sizeof(Random));
    int i=1,ans = 0;
    do 
    {
        srand (time(NULL));
        *num1 = rand()%HIGH_NUMBER;
        *num2 = rand()%HIGH_NUMBER;
        *num3 = rand()%HIGH_NUMBER;
        r->a = *num1;
        r->b = *num2;
        r->c = *num3;

        if ((*num1%2==0||*num2%2||*num3%2==0)&&(*num1%2==1||*num2%2==1||*num3%2==1)&&(*num1>50||*num2>50||*num3>50))
        {
            i--;
            printf("%d %d %d inside isValidNumber\n",*num1,*num2,*num3);
            break;
        }
    }
    while (i);
    return r;
}

