from typing import List
from copy import deepcopy

def Count(Area:List[List[int]]):
    count = 0
    for i in range(len(Area)):
        count+=1
        Max = Area[i][0]
        for j in range(1,len(Area[i])):
            if Max < Area[i][j]:
                count+=1
                Max = Area[i][j]
            
    return count

def East(Area:List[List[int]]):
    area = deepcopy(Area)
    for i in area:
        i.reverse()
    return Count(area)

def West(Area:List[List[int]]):
    return Count(Area)

def North(Area:List[List[int]]):
    Area = list(zip(*Area))
    return Count(Area)

def South(Area:List[List[int]]):
    Area = list(map(list,zip(*Area)))
    area = deepcopy(Area)
    for i in area:
        i.reverse()
    return Count(area)

citySize = list(map(int,input('City Size: ').split()))
arr:List[List[int]] = []
for i in range(citySize[0]):
    msg = list(map(int,input().split()))
    arr.append(msg)

data = {
    'N':North(arr),
    'S':South(arr),
    'E':East(arr),
    'W':West(arr)
}

# print(data)

Max = max(data.items(),key=lambda r:r[1])[1]

Directions = [i[0] for i in data.items() if i[1] == Max]



for index,value in enumerate(Directions):
    if index == len(Directions)-1:
        print(value)
    else:
        print(value , end=' ')
