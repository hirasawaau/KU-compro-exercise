from typing import List


A = [[1,2],[3,4],[5,6]]  
c = 2

def mul_const(A:List[List[int]],n:int) -> List[List[int]]:
    C:List[List[int]] = []
    for i in range(len(A)):
        temArr = []
        for j in range(len(A[i])):
            # print(A[i][j] + B[i][j] , end=" ")
            temArr.append(A[i][j] * n)
        C.append(temArr)
        # print()
        

    return C

def print_matrix(matrix:List[List[int]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:^6}', end = ' ')
        print()


print_matrix(mul_const(A,c))