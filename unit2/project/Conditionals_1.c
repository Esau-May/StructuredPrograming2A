#include <stdio.h>


char username;
int age = 0;

int main(){


    printf("Username: \n");
    scanf("%s", &username);

    printf("Age: \n");
    scanf("%d", &age);

    if (age<18){
        printf("Error. You need to be 18 or older.");

    }

    else{
        printf("Welcome");

    }
    
    return 0;



}