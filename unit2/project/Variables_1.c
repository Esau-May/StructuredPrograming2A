#include <stdio.h>
#include <stdlib.h>


int Numbers;
float Add= 0;
float Variable= 0;
float Result= 0;

int main(int argc, char* argv[]){
    for (Numbers=1; Numbers<argc; Numbers++){ 
        Variable=atof(argv[Numbers]);
        Add+=Variable;
        Result=(Add)/(Numbers);
    if (Numbers==(argc-1)){
    printf("The Average of Numbers is: %f\n", Result);  
    } 
    }
    return 0;
}