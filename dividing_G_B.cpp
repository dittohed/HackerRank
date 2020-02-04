#include <iostream>

using namespace std;

struct Pupil
{
  int group; //0 - G; 1 - B; GGGGGBBBBB
  Pupil *next;
}

size_t distance_to_ideal(Pupil *first)
{
  Pupil *first_green = first;
  Pupil *first_blue;
  Pupil *temp = first;
  Pupil *temp_1;

  size_t already_in_green_row = 0, already_in_blue_row = 0;

  while(temp != nullptr)
  {
    if(temp->group == 0)
    {
      temp_1 = first_green;
      if(already_in_green_row == 0)
      {
        first_green = temp;
      }
      for(int i = 0; i < already_in_green_row - 1; ++i)
        temp_1 = temp_1->next;

      if(temp_1 == first_green)


    }

  }
}

int main()
{


  return 0;
}
