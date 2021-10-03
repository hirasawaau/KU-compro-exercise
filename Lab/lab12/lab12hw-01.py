# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from math import sqrt
from copy import deepcopy

R = int(input('R: '))
C = int(input('C: '))

Square = [['*' for __ in range(C)] for i in range(R)]


def selectSquare(size:int , startI:int , startJ:int , square):
    forkedSquare = deepcopy(square)
    for i in range(startI,startI+size):
        for j in range(startJ,startJ+size):
            try:
                square[i][j]
                pass
            except:
                return False

    return True

poss = 0

for size in range(1,int(sqrt(R*C))+1):
    for i in range(R):
        for j in range(C):
            if selectSquare(size,i,j,Square):
                # print(i,j)
                poss+=1


# %%
print(poss)


# %%



