#include "Addition.hpp"
#include"Multiply.hpp"
#include <stdio.h>
int main()
{
    int x = 4;
    int y = 5;
    int z1 = Addition::twoValues(x,y);
    printf("\n%d + %d = %d\n",x,y,z1);
    int z2 = Multiply::twoValues(x,y);
    printf("\n%d * %d = %d\n",x,y,z2);

    //delete corporation;
    return 0;
}
