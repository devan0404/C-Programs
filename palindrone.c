#include<stdio.h>
#include <string.h>
#include <ctype.h>


int isPalindrome(char str[]){
    int len = strlen(str);
    int start = 0;
    int end = len - 1;

    while (end > start){
        if ((tolower(str[start])) != (tolower(str[end]))){
            return 0;
        }
        start ++;
        end--;

    }
    return 1;
}

int main(){
    char str[100];
    printf("Enter the string : \n");
    gets(str);
    
    if (isPalindrome(str)){
        printf("The given string \"%s\" is a palindrone \n",str);
    }
    else {
        printf("NOT A PALINDROME");
    }
    
    return 0;
}
