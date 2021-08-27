from typing import Any, List, Tuple

def printList(arr:List[List]):
    for i in arr:
        for j in i:
            print(j,end=" ")
        print()

x,y = map(int,input('Grid Size: ').split())
mineSweepers = [[0 for i in range(x)] for i in range(y)]
mine = int(input('Number of mine(s): '))
# printList(mineSweepers)

# for i in range(mine):
#     mines.append(tuple(map(int,input(f'Mine#{i+1}: ').split())))

for i in range(mine):
    a,b = map(int,input(f'Mine#{i+1}: ').split())
    mineSweepers[b][a] = 'X'
    try:
        mineSweepers[b+1][a+1]+=1
    except:
        None
    try:
        if a<=0:
            raise IndexError()
        mineSweepers[b][a-1]+=1
    except:
        None
        
    try:
        mineSweepers[b][a+1]+=1
    except:
        None
    try:
        if b<=0 or a<=0:
            raise IndexError()
        mineSweepers[b-1][a-1]+=1
    except:
        None
    try:
        if b<=0:
            raise IndexError()
        mineSweepers[b-1][a]+=1
    except:
        None
    try:
        if b<=0:
            raise IndexError()
        mineSweepers[b-1][a+1]+=1
    except:
        None
    try:
        if a<=0:
            raise IndexError()
        # mineSweepers[b+1][a-1]+=1
    except:
        None
    try:
        # if a<=0:
        #     raise IndexError()
        mineSweepers[b+1][a]+=1
    except:
        None
    try:
        if a<=0:
            raise IndexError()
        mineSweepers[b+1][a-1]+=1
    except:
        None
    
    # printList(mineSweepers)


# print('---------------')

printList(mineSweepers)

