from copy import deepcopy
from numpy import matmul


def power_matrix(A,c):
    result = deepcopy(A)
    for i in range(c-1):
        result = matmul(result,A)
    return result.tolist()

def print_matrix(A):
    for i in A:
        for j in i:
            print(f'{j:^6}', end = ' ')
        print()

A = [[1,2,3],[4,5,6],[7,8,9]]
c = 2

print_matrix(power_matrix(A,c))

