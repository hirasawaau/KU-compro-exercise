# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np

n = int(input())

Arr = []

for i in range(n):
    N = [n for _ in range(n*2-1)]
    for j in range(1,i+1):
        for k in range(j,len(N) - j):
            N[k] = n-j
        
    Arr.append(N)

Completed = Arr + np.rot90(np.rot90(Arr[:-1])).tolist()

for i in Completed:
    for j in i:
        print(j,end=' ')
    print()



