from typing import List, Tuple
from copy import deepcopy


def IsAreaSquare(Area: List[List[int]]) -> bool:
    isAreaSquare = True
    for index, value in enumerate(Area):
        try:
            if len(value) != len(Area[index + 1]):
                isAreaSquare = not isAreaSquare
                break
        except:
            break
    return isAreaSquare


def Buy(i, j, Area) -> float:
    try:
        Area[i + 1][j] += Area[i + 1][j] * 0.1
    except:
        pass
    try:
        Area[i][j + 1] += Area[i][j + 1] * 0.1
    except:
        pass

    if i - 1 >= 0:
        Area[i - 1][j] += Area[i - 1][j] * 0.1
    if j - 1 >= 0:
        Area[i][j - 1] += Area[i][j - 1] * 0.1

    return Area[i][j]


def ClockWise(Area: List[List[int]]) -> List[float]:
    mockArea = deepcopy(Area)
    price_results: List[float] = []
    values_results: List[float] = []
    for i in range(len(mockArea)):
        values = []
        for j in range(len(mockArea[i])):

            price = 0
            price += (Buy(i, j, mockArea))
            try:
                price += (Buy(i, j + 1, mockArea))
            except:
                mockArea = deepcopy(Area)
                continue
            try:
                price += (Buy(i + 1, j + 1, mockArea))
            except:
                mockArea = deepcopy(Area)
                continue
            try:
                price += (Buy(i + 1, j, mockArea))
            except:
                mockArea = deepcopy(Area)
                continue

            # print(Area)
            price_results.append(price)
            mockArea = deepcopy(Area)

    return price_results


def AntiClockWise(Area: List[List[int]]) -> List[float]:
    mockArea = deepcopy(Area)
    price_results: List[float] = []
    for i in range(len(mockArea)):
        prices = []
        for j in range(len(mockArea[i])):

            price = 0
            price += (Buy(i, j, mockArea))
            try:
                price += (Buy(i, j + 1, mockArea))
            except:
                mockArea = deepcopy(Area)

                continue
            try:
                if i - 1 >= 0:
                    price += (Buy(i - 1, j + 1, mockArea))
                else:
                    raise IndexError('Index < 0')
            except:
                mockArea = deepcopy(Area)

                continue
            try:
                if i - 1 >= 0:
                    price += (Buy(i - 1, j, mockArea))
                else:
                    raise IndexError('Index < 0')
            except:

                mockArea = deepcopy(Area)
                continue

            price_results.append(price)
            mockArea = deepcopy(Area)
    return price_results


areaMatrix: List[List[int]] = []
while True:
    Input = list(map(int, input().split()))
    if len(Input) == 0: break

    areaMatrix.append(Input)

if not IsAreaSquare(areaMatrix):
    print("Can't Buy")
else:
    allPrices = ClockWise(areaMatrix)
    allPrices.extend(AntiClockWise(areaMatrix))

    print(f'{min(allPrices):.2f}')