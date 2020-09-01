#include <iostream>
using namespace std;

int main(){

    int temp, curr;
    int arr[14] = {7, 3, 1, 5, 4, 1 , 8,85,86,0,9,10,1,0};
    

    for (int i = 0; i < 14; i++)
    {   
        for (int j = i+1; j > 0; j--)
        {
            if (arr[j] <= arr[j-1]){
                temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;
            }           
        }        
    }

    for (int i = 0; i < 14; i++)
    {
        cout<<arr[i]<<" ";
    }
    

    return 0;
}