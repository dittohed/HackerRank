#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define SIZE 10

int left_son(int i)
{
  return 2 * i;
}

int right_son(int i)
{
  return 2 * i + 1;
}

void max_heapify(int array[], int i)
{
  int l = left_son(i);
  int r = right_son(i);
  int max = i;
  int temp;

  if(l < SIZE && array[l] > array[max])
    max = l;

  if(r < SIZE && array[r] > array[max])
    max = r;

  if(max != i)
  {
    temp = array[i];
    array[i] = array[max];
    array[max] = temp;

    max_heapify(array, max);
  }
}

void build_max_heap(int array[])
{
  int i;

  for(i = SIZE / 2; i >= 0; --i)
    max_heapify(array, i);
}

int main()
{
  srand(time(NULL));
  int array[SIZE];
  int i;

  printf("BEFORE: \n");
  for(i = 0; i < SIZE; ++i)
  {
    array[i] = rand() % 10;
    printf("%d ", array[i]);
  }


  build_max_heap(array);

  printf("\nAFTER: \n");
  for(i = 0; i < SIZE; ++i)
    printf("%d ", array[i]);

  return 0;
}
