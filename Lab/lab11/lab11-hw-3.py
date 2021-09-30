from typing import List,Tuple
from itertools import combinations 

n = int(input('N : '))

r = []

for i in range(n):
    Input = input().split()
    r.append((Input[0],int(Input[1])))  

k = []

XX = int(input('XX : '))
def com():
    for i in range(n,0,-1):
        com = combinations(r,i)
        for j in com:
            s = sum([k[1] for k in j])
            if s == XX:
                return j

for i in com():
    print(i[0],end=' ')

print()


