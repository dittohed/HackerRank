#include <iostream>
#include <vector>
#include <ctime> //rand
#include <cmath> //floor

using namespace std;

void randomize_array(double A[], const size_t array_size)
{
  for(size_t i = 0; i < array_size; ++i)
    A[i] = (rand() % 100) / 100.0; //jeżeli jeden z operandów jest liczbą zmiennoprzecinkową, to wynik jest liczbą zmiennoprzecinkową
}

void print_array(double A[], const size_t array_size)
{
  for(size_t i = 0; i < array_size; ++i)
    cout << A[i] << " ";

  cout << endl;
}

void insertion_sort(double array[], const size_t array_size)
{
  double key;
  size_t j;

  for(size_t i = 1; i < array_size; ++i)
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

void bucket_sort(double A[], const size_t array_size)
{
  vector <double> B[array_size];

  for(size_t i = 0; i < array_size; ++i)
    B[size_t(A[i] * array_size)].push_back(A[i]);

  for(size_t i = 0; i < array_size; ++i)
  {
    if(B[i].size() != 0)
      insertion_sort(B[i].data(), B[i].size()); //data() zwraca wskaźnik do obszaru pamięci
  }

  /*
  size_t i, k = 0;
  while(i < array_size)
  {
    for(size_t j = 0; j < B[k].size(); ++j)
    {
      A[i] = B[k][j];
      ++i;
    }


    ++k;
  }*/
}

int main()
{
  srand(time(NULL));

  const size_t array_size = 10;
  double A[array_size];

  randomize_array(A, array_size);
  print_array(A, array_size);

  //bucket_sort(A, array_size);
  //print_array(A, array_size);

  return 0;
}
