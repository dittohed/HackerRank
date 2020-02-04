#include <stdio.h>

//do pseudolosowych
#include <stdlib.h>
#include <time.h>

#define LENGTH 5

void add_binary(int A[], int B[], int C[])
{
  int carry = 0; //przeniesienie
  int i;

  for(i = LENGTH - 1; i >= 0; i--)
  {
    C[i + 1] = (A[i] + B[i] + carry) % 2;
    if((A[i] + B[i] + carry) >= 2)
      carry = 1;
    else
      carry = 0;
  }

  C[0] = carry;
}

void generate_random_number(int array[])
{
  int i;

  for(i = 0; i < LENGTH; ++i)
    array[i] = rand() % 2;
}

void print_arrays(int A[], int B[], int C[])
{
  int i;

  putchar(' ');
  for(i = 0; i < LENGTH; ++i)
    printf("%d", A[i]);
  putchar('\n');

  putchar(' ');
  for(i = 0; i < LENGTH; ++i)
    printf("%d", B[i]);
  putchar('\n');

  for(i = 0; i < LENGTH + 1; ++i)
    printf("%d", C[i]);
}

int main()
{
  srand(time(NULL));

  int A[LENGTH];
  int B[LENGTH];
  int C[LENGTH + 1];

  generate_random_number(A);
  generate_random_number(B);

  add_binary(A, B, C);

  print_arrays(A, B, C);

  return 0;
}
