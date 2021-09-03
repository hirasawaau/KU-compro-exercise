from typing import List
import numpy as np

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

def isOperator(s:str) -> bool:
    return s=='+' or s=='*'

def print_matrix(res:List[List[int]]) -> None:
    for i in range(len(res)):
        for j in range(len(res[0])):
            print(f"{res[i][j]:^5}",end=" ")
        print('')

def operationMatrix(path:str) -> List[List[int]]:
    data1 = []
    data2 = []
    operator = ''
    with open(path) as file:
        for f in file:
            cleanStr = f.strip()
            # print(cleanStr,operator)
            if isOperator(cleanStr):
                if operator != '':
                    
                    if operator == '+':
                        data1 = plus_matrix(data1,data2)
                    elif operator == '*':
                        data1 = np.matmul(data1,data2).tolist()

                data2 = []
                operator = cleanStr
                continue
            
            if operator != '':
                data2.append([int(i) for i in (cleanStr.split())])
                continue
            data1.append([int(i) for i in (cleanStr.split())])

    # print(data1,data2)
    if operator == '+':
        return plus_matrix(data1,data2)
    elif operator == '*':
        return np.matmul(data1,data2).tolist()

fileName = input('File name: ')

print_matrix(operationMatrix(fileName))