from typing import List

A = [[1,2],[3,4],[5,6]] 

def mapTupleToList(t:tuple) -> list:
    return list(t)

def transpose_matrix(A:List[List[int]]) -> List[List[int]]:
    transpose = list(map(mapTupleToList, zip(*A)))
    return transpose

def print_matrix(A:List[List[int]]) -> None:
    for i in A:
        for j in i:
            print(f'{j:^6}', end = ' ')
        print()

print_matrix(transpose_matrix(A))



