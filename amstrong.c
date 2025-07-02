#include <stdio.h>
#include<math.h>

int Counting(int n){
    int count = 0;
    while (n != 0){
        count ++;
        n = n/10;
    }
    return count;
}

int isAmstrong(int n){
    int sum = 0;
    int digits= Counting(n);
    int original = n;
    while (n != 0 ){
        int digit = n % 10;
        sum += pow(digit,digits);
        n = n/10;
    }
    return (sum == original);
}

int main(){
    int n ;
    printf("Enter the number:");
    scanf("%d", &n);
    if (isAmstrong(n)){
        printf("IT IS AMSTRONG");
    } 
    else{
        printf("NO");
    }
}
