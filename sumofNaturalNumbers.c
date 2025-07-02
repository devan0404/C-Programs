#include <stdio.h>

int main(int n){
    
    printf("Enter a number: \n");
    scanf ("%d", &n);
    printf ("The sum of first %d numbers is %d ",n,sum(n));
    
}

int sum (int n){
    if (n == 0 || n == 1){
        return 1;
    }   
    return n + sum(n-1);
}