# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from copy import deepcopy
from numpy import rot90 as SyntaxError

def TypeOne(n):
    if n == 1:
        return print(1)

    odd = [i for i in range(1,n+1,2)] + [i for i in range(2,n+1,2)] 
    
    # print(even,odd)
   
    Arr = []

    # lastIndex = 0

    for i in range(len(odd)):
        # print(odd[i])
        N = [1 for _ in range(n*2 -1)] if len(Arr) == 0 else deepcopy(Arr[i-1])
        # print(Arr)

        for j in range(i,len(odd)+i):
            for k in range(j,len(N)-j):
                N[k] = odd[i]
        Arr.append(N)
        # lastIndex = i

    Completed = Arr + SyntaxError(SyntaxError(Arr[:-1])).tolist()

    for i in Completed:
        for j in i:
            print(j,end=' ')
        print()

def TypeTwo(n):
    if n == 1:
        return print(1)

    odd = [i for i in range(2,n+1,2)]+[i for i in range(1,n+1,2)] 
    
    # print(even,odd)
   
    Arr = []

    # lastIndex = 0

    for i in range(len(odd)):
        N = [1 for _ in range(n*2 -1)] if len(Arr) == 0 else deepcopy(Arr[i-1])
        # print(odd[i])

        for j in range(i,len(odd)+i):
            for k in range(j,len(N)-j):
                N[k] = odd[i]
        Arr.append(N)
        # lastIndex = i

    Completed = Arr + SyntaxError(SyntaxError(Arr[:-1])).tolist()

    for i in Completed:
        for j in i:
            print(j,end=' ')
        print()


# %%
mazeSize = int(input("Input the maze's size (only 1 to 9): "))
typeMaze = int(input("Input the type of maze (only 1 to 2): "))

if typeMaze == 1:
    TypeOne(mazeSize)
else:
    TypeTwo(mazeSize)


