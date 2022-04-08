// Compile with gcc secret-stuff.c
// Run with ./a.out

#include <stdio.h>

int num_times;

int main() {
  printf("Type a number, any number! ");
  scanf("%d", &num_times); // %d means placeholder for int, & is the "address
                           // of" operator
  for (int i = 0; i < num_times; i++) {
    printf("Hello, world %d\n", i);
  }
  return 0;
}
