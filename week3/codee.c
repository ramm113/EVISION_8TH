#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int KEYWORD = 13;

int main(){

    int num;

    while (1){
        printf("Enter an integer (within two digits): ");
        scanf("%d", &num);

        if (num > 99 || num < 0){
        printf("Enter again.\n");
        }
        else{
            break;
        }
    }

    if(num == KEYWORD){
        printf("Right!");
    } else {
        printf("Wrong..");
    }

    return 0;
    
}