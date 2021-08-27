from typing import List


A = [[1,2,3],[4,5,6],[7,8,9]]  
B = [[22,13,23],[54,43,21],[23,78,71]]

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

def print_matrix(matrix:List[List[int]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:^6}', end = ' ')
        print()


print_matrix(plus_matrix(A,B))