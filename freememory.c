#include <stdio.h>
#include <stdlib.h>

int main(){
    int n;
    printf("Enter the size of the array :\n");
    scanf("%d", &n);
    int * ptr;

  //  ptr = (int*)malloc(sizeof(int)); //Has garbage value before giving any data
    ptr = (int*)calloc(n,sizeof(int)); //Has zero as its value before giving any data

    printf("Enter the array elements : \n");
    for (int i =0 ; i < n ; i++){
        scanf ("%d", &ptr[i]);
    }
    printf("The array elements are : \n");
    for (int i =0 ; i <n; i++){
        printf ("%d ",ptr[i]);
    }

    printf("Enter the size of the array :\n");
    scanf("%d", &n);

    ptr = realloc(ptr, n* sizeof(int));

    printf("Enter the new array elements : \n");
    for (int i =0 ; i < n ; i++){
        scanf ("%d", &ptr[i]);
    }
    printf("The array new elements are : \n");
    for (int i =0 ; i <n; i++){
        printf ("%d ",ptr[i]);
    }

    free(ptr); // THIS WILL DEALLOCATE THE MEMEORY
    return 0;

    
}