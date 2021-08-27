from typing import List


def print_arr(arr:List[List[str]]):
    for i in arr :
        for j in i:
            print(j , end="")
        print()



n = int(input())
arr = [[' ' for i in range(n)] for i in range(n)]
arr[0] = ['.' for i in range(n)]
arr[n-1] = ['.' for i in range(n)]

for i in range(1,n-1):
    arr[i][0] = '.'
    arr[i][i] = '.'
    arr[i][n-1-i] = '.'
    arr[i][n-1] = '.'

print_arr(arr)
