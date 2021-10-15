# Your task, is to create NxN multiplication table, of size provided in parameter.

# for example, when given size is 3:

# 1 2 3
# 2 4 6
# 3 6 9
# for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]


def multiplication_table(size):
    matriz = []
    count = 1
    for column in range(1,size+1):
        rows = []
        for row in range(1,size+1):
            rows.append(row*count)
        matriz.append(rows)
        count +=1
    return matriz


    