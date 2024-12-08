#include <stdio.h>
int main() {
  int a, b, c;
  printf("Enter three numbers: ");
  scanf("%d %d %d", &a, &b, &c);
  if (a >= b && a >= c) {
    printf("The first number, %d is the largest number.\n", a);
  } 
  else if (b >= a && b >= c) {
    printf("The second number, %d is the largest number.\n", b);}
  else {
    printf("The third number, %d is the largest number.\n", c);
  }
return 0;
}
