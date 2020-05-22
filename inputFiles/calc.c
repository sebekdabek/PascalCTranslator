#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {

 int input;
 int a;
 int b;
 int result;
 char option;

 do {
    printf("\nEnter 1 for addition:\n");
    printf("Enter 2 for subtraction:\n");
    printf("Enter 3 for multiplication:\n");
    printf("Enter 4 for division:\n");

    scanf("%d", &input);
    printf("Enter a number:\n");
    scanf("%d", &a);
    printf("Enter second number:\n");
    scanf("%d", &b);

    switch(input) {
        case 1:
          result = a+b;
          printf("Result of addition is : %d\n", result);
        break;

        case 2:
          result = a-b;
          printf("Result of substraction is : %d\n", result);
        break;

        case 3:
          result = a*b;
          printf("Result of multiplication is : %d\n", result);
        break;

        case 4:
          result = a/b;
          printf("Result of division is : %d\n", result);
        break;

        default:
          printf("Wrong input!\n");
    }

    printf("Do you want to continue? (y/n)\n");
    scanf(" %c", &option);

    } while(option == 'y');

 return 0;
}