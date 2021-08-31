from typing import List, Tuple
from copy import deepcopy


class HuangJui:
    area:List[List[int]] = []
    temporaryArea:List[List[int]]


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

    def Buy(self,i,j) -> float:
        try:
            self.temporaryArea[i + 1][j] += self.temporaryArea[i + 1][j] * 0.1
        except:
            pass
        try:
            self.temporaryArea[i][j + 1] += self.temporaryArea[i][j + 1] * 0.1
        except:
            pass

        if i - 1 >= 0:
            self.temporaryArea[i - 1][j] += self.temporaryArea[i - 1][j] * 0.1
        if j - 1 >= 0:
            self.temporaryArea[i][j - 1] += self.temporaryArea[i][j - 1] * 0.1

        return self.temporaryArea[i][j]

    def ClockWise(self) -> List[float]:
        self.ResetArea()
        price_results: List[float] = []
        for i in range(len(self.temporaryArea)):
            for j in range(len(self.temporaryArea[i])):

                price = 0
                price += (self.Buy(i, j))
                try:
                    price += (self.Buy(i, j + 1))
                except:
                    self.ResetArea()
                    continue
                try:
                    price += (self.Buy(i + 1, j + 1))
                except:
                    self.ResetArea()
                    continue
                try:
                    price += (self.Buy(i + 1, j))
                except:
                    self.ResetArea()
                    continue

                # print(Area)
                price_results.append(price)
                self.ResetArea()

        return price_results

    def AntiClockWise(self) -> List[float]:
        self.ResetArea()
        price_results: List[float] = []
        for i in range(len(self.temporaryArea)):
            for j in range(len(self.temporaryArea[i])):

                price = 0
                price += (self.Buy(i, j))
                try:
                    price += (self.Buy(i, j + 1))
                except:
                    self.ResetArea()

                    continue
                try:
                    if i - 1 >= 0:
                        price += (self.Buy(i - 1, j + 1))
                    else:
                        raise IndexError('Index < 0')
                except:
                    self.ResetArea()

                    continue
                try:
                    if i - 1 >= 0:
                        price += (self.Buy(i - 1, j))
                    else:
                        raise IndexError('Index < 0')
                except:

                    self.ResetArea()
                    continue

                price_results.append(price)
                self.ResetArea()
        return price_results

    def ResetArea(self) -> None:
        self.temporaryArea = deepcopy(self.area)

    def CheckArea(self) -> bool:
        areaLength = len(self.area[0])

        for i in self.area:
            if len(i) != areaLength:
                return False
        return True

    def Input(self) -> None:
        while False is not True:
            Input = list(map(int, input().split()))
            if len(Input) == 0: break

            self.area.append(Input)

    def __init__(self) -> None:
        self.Input()
        if not self.CheckArea():
            print("Can't Buy")
            exit()
        prices = self.ClockWise()
        prices += self.AntiClockWise()

        print(f'{min(prices):.2f}')
        
HuangJui()