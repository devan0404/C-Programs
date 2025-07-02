#include <stdio.h>

int main(int n){
    
    printf("Enter the number for fibonacci : \n");
    scanf ("%d", &n);
    printf ("The fibonacci of %d is %d \n",n,fibonacci(n));
    for (int i = 0; i<=n ; i++){
        printf("%d  ",fibonacci(i));
    }
    
}

int fibonacci (int n){
    if (n == 0 || n == 1){
        return n;
    }
    
    return fibonacci(n-1) + fibonacci(n-2);
}   