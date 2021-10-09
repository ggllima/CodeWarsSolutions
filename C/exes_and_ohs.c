
// Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

// Examples input/output:

// XO("ooxx") => true
// XO("xooxx") => false
// XO("ooxXm") => true
// XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
// XO("zzoo") => false

#include <stdbool.h>

bool xo(const char* str)
{
  int length = 0, x = 0, o = 0;
  for (int i = 0; str[i] != '\0'; i++)
    if (str[i] == 'x' || str[i] == 'X')
      x++;
    else if (str[i] == 'o' || str[i] == 'O')
      o++;
  return (x==o) ? true : false;
}