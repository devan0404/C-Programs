#include <stdio.h>

int main(){
    int result =0;
    int arr[] = {1,2,3,4,2,1};
    int n1 = 0, n2 = 0;
    int size = sizeof(arr) / sizeof(arr[0]);
    int xorAll = 0;

    for (int i =0; i <size ; i++){
        xorAll ^= arr[i];
    }
    
    int rsb = xorAll & (-xorAll);
    
    for (int i =0; i <size; i++){
        if (arr[i] & rsb){
            n1 ^= arr[i];
        }
        else{
            n2 ^= arr[i];
        }
    }
    
    printf("N1 = %d and N2 = %d \n",n1,n2);

    return 0;
}