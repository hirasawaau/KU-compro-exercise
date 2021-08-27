from typing import List


def IsAreaSquare(Area:List[List[int]]) -> bool:
    isAreaSquare = True
    for index,value in enumerate(Area):
        if len(value) != len(Area[index+1]):
            isAreaSquare = not isAreaSquare
            break
    return isAreaSquare


areaMatrix:List[List[int]] = []
while True:
    Input = input()
    if len(Input == 0): break
    
    areaMatrix.append(Input.split())

if not IsAreaSquare(areaMatrix):
    print("Can't Buy")
else:
    pass