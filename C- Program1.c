#include <stdio.h>
#include <math.h>

int main() {
    double argument, base, result;

    printf("Enter the argument: ");
    scanf("%lf", &argument);

    printf("Enter the base: ");
    scanf("%lf", &base);

    if (argument > 0 && base > 0 && base != 1) {
        result = log(argument) / log(base);
        printf("Logarithm is %.2lf\n",result);
    } else {
        printf("Invalid input. Argument and base must be positive, and base must not be 1.\n");
    }

    return 0;
}
