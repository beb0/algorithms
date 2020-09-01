#include <iostream>
using namespace std;

int main(){

    int min, arr_len, temp;
    cin>>arr_len;
    int arr[arr_len];// = {7, 3, 1, 5, 4, 1 , 8};

    for (int i = 0; i < arr_len; i++)
    {
        cin>>arr[i];
    }
    

    for (int i = 0; i < arr_len; i++)
    {
        min = i;

        for (int j = i+1; j < arr_len; j++)
        {   
            if(arr[j] < arr[min] ){
                min = j;
            }
        }             

        temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }

    for (int i = 0; i < arr_len; i++)
    {
        cout<<arr[i];
    }
    
   
    
    return 0;
}