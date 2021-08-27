from typing import List
import numpy
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[22,13,23],[54,43,21],[23,78,71]]  

def mul_matrix(A:List[List[int]],B:List[List[int]]) -> List[List[int]]:
    # def mulThenPlus(x:List[int],y:List[int]) -> int:
    #     if len(x) != len(y):
    #         raise IndexError('Two list must same length')
    #     result=0
    #     for i in range(len(x)):
    #         result+=(x[i]*y[i])

    #     return result
    # result:List[List[int]] = []
    # tranB = list(map(list,zip(*B)))

    # for i in range(len(A)):
    #     tem = []
    #     for j in range(len(B)):
    #         tem.append(0)
    #     result.append(tem)
    
    # for i in range(len(A)):
    #     for j in range(len(B)):
    #         result[i][j] = mulThenPlus(A[i],tranB[j])

    return numpy.matmul(A,B).tolist()
    
    

def print_matrix(A:List[List[int]]) -> None:
    for i in A:
        for j in i:
            print(f'{j:^6}', end = ' ')
        print()

print_matrix(mul_matrix(A,B))


