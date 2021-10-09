# Flatten and sort an array
# Challenge:
# Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the sorted (ascending) order.

# Example:

# Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].


def flatten_and_sort(array):
    new_array = []
    if len(array):
        for columns in range(len(array)):
            for rows in range(len(array[columns])):
                new_array.append(array[columns][rows])
        new_array.sort()
    return new_array