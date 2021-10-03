# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from copy import deepcopy

def selectSpace(begin_i,begin_j,arr,width,length):
    forkedArr = deepcopy(arr)

    for i in range(begin_i,begin_i+4):
        try:
            if arr[i][begin_j] != 0 and arr[i][begin_j+1] != 0 and begin_j+1 < width-1 and i < length - 1:
                forkedArr[i][begin_j] = 'x'
                forkedArr[i][begin_j+1] = 'x'
            else:
                # print('Case 1')
                return
        except:
            # print('Case 2')
            return

    return forkedArr

def printArr(arr):
    for i in arr:
        for j in i:
            print(j,end=' ')
        print()
    


# %%
length = int(input('Length: '))
width = int(input('Width: '))

arr = [list(map(int,input().split())) for _ in range(length)]


# %%
possible = []

for i in range(1,length-1):
    for j in range(1,width-1):
        space = selectSpace(i,j,arr,width,length)
        if space:
            possible.append(space)


# %%
print(f'{len(possible)} possible court(s)')

for arr in possible:
    printArr(arr)
    print()


