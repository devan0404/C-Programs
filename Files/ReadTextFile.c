#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE *fptr;
    char buffer[255]; 
    fptr = fopen("D:\\4VV23EC033\\Files\\vvce.txt", "r");
    
    if (fptr == NULL) {
        printf("Error opening file\n");
        return -1;
    }
    else {
        printf("File opened successfully\n");
    }

    while (fgets(buffer, sizeof(buffer), fptr) != NULL) {
        printf("%s", buffer);
    }
    fclose(fptr);
    printf("File closed successfully\n");

    return 0;
}