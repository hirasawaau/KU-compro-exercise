from typing import List
import numpy
from copy import deepcopy

def plus_matrix(A:List[List[int]],B:List[List[int]]) -> List[List[int]]:
    C:List[List[int]] = []
    for i in range(len(A)):
        temArr = []
        for j in range(len(A[i])):
            # print(A[i][j] + B[i][j] , end=" ")
            temArr.append(A[i][j] + B[i][j])
        C.append(temArr)
        # print()
        

    return C

def minus_matrix(A:List[List[int]],B:List[List[int]]) -> List[List[int]]:
    C:List[List[int]] = []
    for i in range(len(A)):
        temArr = []
        for j in range(len(A[i])):
            # print(A[i][j] + B[i][j] , end=" ")
            temArr.append(A[i][j] - B[i][j])
        C.append(temArr)
        # print()
        

    return C

def mul_matrix(A:List[List[int]],B:List[List[int]]) -> List[List[int]]:
    return numpy.matmul(A,B).tolist()

def transpose_matrix(A:List[List[int]]):
    return list(map(list,zip(*A)))

def power_matrix(A,c):
    result = deepcopy(A)
    for i in range(c-1):
        result = numpy.matmul(result,A)
    return result.tolist()

def print_matrix(matrix:List[List[int]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:^6}', end = ' ')
        print()

A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
D = [[100,50],[20,70]]
c = 2

print_matrix(mul_matrix(plus_matrix(A,transpose_matrix(B)),minus_matrix(power_matrix(C,c),D)))
