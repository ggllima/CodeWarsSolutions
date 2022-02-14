# CodeWars Solutions

<div style="display: inline_block"><br>
  <img align="center" height="50" width="50" src="https://www.codewars.com/assets/logos/logo-61192cf7c75904d495e7ad69695fbf0bffd965bc3e17ac60f6c6b475304db09d.svg" alt="CodeWars_icon">
</div> 


## Languages

<div style="display: inline_block"><br>
  <img align="center" alt="Guilherme-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
  <img align="center" alt="Guilherme-C" height="30" width="40" src="https://github.com/devicons/devicon/blob/master/icons/c/c-original.svg">
  <img align="center" alt="Guilherme-sql" height="30" width="40" src="https://image.flaticon.com/icons/png/512/29/29165.png">
</div> 

## Intro

The idea of this project is to present the challenges proposed by the [Codewars](https://www.codewars.com/) website and my solutions in Python, C and SQL languages. Other languages can be added as i learn..

## Example

### Flatten and sort an array

#### Challenge:

Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the sorted (ascending) order.

Example:

Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].

#### Solution:

```
def flatten_and_sort(array):
    new_array = []
    if len(array):
        for columns in range(len(array)):
            for rows in range(len(array[columns])):
                new_array.append(array[columns][rows])
        new_array.sort()
    return new_array
```
