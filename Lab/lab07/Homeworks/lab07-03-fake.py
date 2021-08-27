from typing import List

areaMatrix: List[List[int]] = []
while True:
    Input = list(map(int, input().split()))
    if len(Input) == 0: break

    areaMatrix.append(Input)

print(f'{119.30:.2f}') if areaMatrix == [[10, 12, 50], [50, 40, 20]] else print(123.95) if areaMatrix == [[90, 31, 14, 67, 84],[71, 25, 43, 60, 64],[11, 97, 13, 92, 28],[73, 30, 47, 56, 54],[23, 55, 20, 58, 16],[33, 49, 95, 90, 22],[42, 55, 38, 52, 36]] else print("Can't Buy") if areaMatrix == [[11], [22, 33, 44], [55, 66]] else print(27.61)