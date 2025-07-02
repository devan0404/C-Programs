#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Store {
    int price;
    union { // Union to save memory, only one of these will be used at a time

        struct{
            char design[20]; 
            int ISBN;
            char genre[20];
        }book;

        struct{
            char color[10];
            char size[10];
            char brand[20];
        }shirt;

    }item;
};

int main(){
    struct Store s;
    s.price = 499;
    strcpy(s.item.book.design, "E-Book");
    s.item.book.ISBN = 1001;
    strcpy(s.item.book.genre, "Fiction");
    printf("size of the book is %llu bytes\n", sizeof(s));
    printf("size of the shirt is %llu bytes\n", sizeof(s));
    
    return 0;
}