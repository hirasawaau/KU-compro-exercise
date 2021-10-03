# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from typing import List,Union,Tuple
from numpy import reshape

def findIndex(d,arr:List[List[int]]) -> Union[Tuple[int,int] , None]:
    # print(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == d:
                return f'({i},{j})'


# %%
n,m = int(input('Input n: ')) , int(input('Input m: '))


arr = []

for _ in range(n):
    arr.append(list(map(int,input().split())))


# %%
sortedArr = reshape(arr,n*m)
sortedArr.sort()

for i in sortedArr:
    print(findIndex(i,arr))


