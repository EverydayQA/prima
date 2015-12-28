#include <iostream>
#include <string>

using namespace std;

template <class T> int IsSubArr(T *a, int a_len, T *b, int b_len)
{
    int i,j;
    bool found;
    int k;
    T *s=a;
    T *l=b;

    int s_len = (a_len < b_len) ? a_len : b_len; // find the small array length
    if (s_len == a_len) // check to set pointers to small and long array
    {
        s = a;
        l = b;
    }
    else
    {
        s = b;
        l = a;
    }


    for (i = 0; i <= a_len-s_len; i++) //loop on long array
    {
        found = true;
        k=i;
        for (j=0; j<s_len; j++) // loop on sub array
        {
            if (s[j] != l[i])
            {
                found = false;
                break;
            }
            k++;
        }
    }

    if (found)
      return i;
    else
      return -1;
}


/******* main program to test templates ****/
int main()
{

    int array[5] = {9,4,6,2,1};
    int alen = 5;
    int sub_arr[3] = {6,2,1};
    int slen = 3;

    int index= 0;
    index = IsSubArr(array,alen,sub_arr,slen);
    cout << "\n\n Place of sub array in long array: " << index;

    cout << endl;

    return 0;

}

