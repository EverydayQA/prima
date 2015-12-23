#include "testMath.h"

int testMath::Addition(int x, int y)
{
    return (x + y);
}

int testMath::Multiply(int x, int y)
{
    return (x * y);
}

int testMath::Subtraction(int x, int y)
{
    return (x - y);
}

int testMath::Division(int x, int y)
{
    if( b == 0 )
    {
        throw "Division by zero condition!";
    }
    return (a/b);
}

void swap(int &a, int &b)
{
    int temp;

    temp = b;
    b   = a;
    a   = temp;   
}

