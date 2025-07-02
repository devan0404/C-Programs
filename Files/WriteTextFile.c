#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE *fptr;
    char buffer[255]; 
    fptr = fopen("D:\\4VV23EC033\\Files\\vvce.txt", "a"); //Use w for rewriting or creating a file && USE a for appending to a file
    
    if (fptr == NULL) {
        printf("Error opening file\n");
        return -1;
    }
    else {
        printf("File opened successfully\n");
    }

    fprintf(fptr, "DARSHAN SHOULD LEARN TO GET A LIFE \n");
    fclose(fptr);
    printf("File closed successfully\n");

    return 0;
}