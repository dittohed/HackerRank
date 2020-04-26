#include <stdio.h>

//do pseudolosowych
#include <stdlib.h>
#include <time.h>

#define ARRAY_SIZE 20

void insertion_sort(int array[])
{
  int i, j, key;

  for(i = 1; i < ARRAY_SIZE; ++i)
  {
    key = array[i];
    j = i - 1;
    while(j >= 0 && array[j] < key)
    {
      array[j + 1] = array[j];
      --j;
    }

    array[j + 1] = key;
  }
}

void print_array(int array[])
{
  int i;

  for(i = 0; i < ARRAY_SIZE; ++i)
    printf("%d ", array[i]);
}

void generate_random_array(int array[])
{
  int i;
  srand(time(NULL));

  for(i = 0; i < ARRAY_SIZE; ++i)
    array[i] = rand() % 10 + 1;
}

int main()
{
  int array[ARRAY_SIZE] = {0};
  generate_random_array(array);

  printf("Before: \n");
  print_array(array);

  insertion_sort(array);

  printf("\nAfter: \n");
  print_array(array);

  return 0;
}
