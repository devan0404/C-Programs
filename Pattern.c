#include <stdio.h>
/* 
 //increasing star triangle
int main(){
    int n = 6;
    for (int i = 0; i< n; i++){
        for (int j =0 ; j < i; j++){
            printf("*");
        }
        printf("\n");
    }
}

 //decreasing star triangle
int main(){
    int n = 0;
    for (int i = 6; i > n; i--){
        for (int j =i ; j > 1; j--){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}

 //increasing number triangle
int main(){
    int n = 5;
    for (int i = 1; i<= n; i++){
        for (int j =1 ; j <= i; j++){
            printf("%d",j);
        }
        printf("\n");
    }
}


//increasing pyramid
int main(){
    int n =5;
    for (int i=1;i<=n;i++){
        for (int s=1; s <= n-i ; s++){
            printf(" ");
        }
        for (int j=1 ; j <= (2*i-1) ; j++ ){
            printf("*");
        }
        
        printf("\n");
    }

//decreasing pyramid

    for (int i=n;i>1;i--){
        for (int s=1; s <= n-i ; s++){
            printf(" ");
        }
        for (int j=1 ; j <= (2*i-1) ; j++ ){
            printf("*");
        }
        
        printf("\n");
    }
}

//LLOYD's Triange
int main(){
    int n = 5;
    int count = 0;
    for (int i = 0; i< n; i++){
        for (int j =0 ; j < i; j++){
            count +=1;
            printf("%d ",count);
        }
        printf("\n");
    }
}


//hollow square
int main(){
    int n = 5;
    for (int i = 1; i<= n; i++){
        for (int j =1 ; j <= n; j++){
            if (i == 1 || i == n || j == 1 || j==n ){
                printf("* ");
            }
            else{
                printf("  ");
            }
        }
        printf("\n");
    }
    return 0;
}

// CHARACTER PATTERNS

int main(){
    char alp = 'A';
    int n = 5;
    for (int i = 1; i<= n; i++){
        for (int j =1 ; j <= i; j++){
            printf("%c",alp);
        }
        alp ++;
        printf("\n");
    }
}

int main(){
    char alp = 'A';
    int n = 5;
    for (int i = 1; i<= n; i++){
        for (int j =1 ; j <= i; j++){
            printf("%c",alp);
            alp ++;
        }   
        printf("\n");
        alp = 'A';
    }
}


int maxPieces(int n){
    return (n * (n+1)/2 + 1);
}
int main(){
    int n;
    printf("Enter the value of n: \n");
    scanf("%d",&n);
    printf("Pieces %d", maxPieces(n));
}


int main(){
    int ans = 0;
    int num = 0;
    printf("enter the value of n:");
    scanf ("%d",& num);

    while(num > 0) {
    int digit = num % 10 ;
    ans = ans * 10 +digit;
    num = num/10;
    }
    printf("The reverse integer is %d",ans);
}


int main(){
    int ans = 0;
    int num = 0;
    printf("enter the value of n:");
    scanf ("%d",& num);
    int store = num;

    while(num > 0) {
    int digit = num % 10 ;
    ans = ans * 10 +digit;
    num = num/10;
    }
    if (store == ans){
        printf("IT IS A PALINDROME");
    }
    else {
        printf("IT IS *NOT* A PALINDROME");
    }
}
*/
