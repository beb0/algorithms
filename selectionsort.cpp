#include <iostream>
using namespace std;

int main(){

    int min, arr_len, index;
    cin>>arr_len;
    int arr[arr_len];// = {7, 3, 1, 5, 4, 1 , 8};

    for (int i = 0; i < arr_len; i++)
    {
        cin>>arr[i];
    }
    

    for (int i = 0; i < arr_len; i++)
    {
        min = arr[i];

        for (int j = i+1; j < arr_len; j++)
        {   
            if(arr[j] < min ){
                min = arr[j];
                index = j;
            }
        }             

        if(arr[i] > min){
            arr[index] = arr[i];
            arr[i] = min;
        }
    }

    for (int i = 0; i < arr_len; i++)
    {
        cout<<arr[i];
    }
    
   
    
    return 0;
}