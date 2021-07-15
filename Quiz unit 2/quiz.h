#include <stdio.h>
#include <stdlib.h>

typedef struct Robot{
    char* name;
    char* type;
    int height;
    int weight;
    int degreesOfFreedom;

    void (*sayHelloToRobot)(struct Robot);

}ROBOT;

void sayHelloToRobot(ROBOT Robot){
    printf("Hey, hello %s\n", Robot.name);
    
}