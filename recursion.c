#include <stdio.h>

int main(int n){
    
    printf("Enter the number for factorial : \n");
    scanf ("%d", &n);
    printf ("The factorial of %d is %d ",n,factorial(n));
    
}

int factorial (int n){
    if (n == 0 || n == 1){
        return 1;
    }
    
    return n * factorial (n-1);
}