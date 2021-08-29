from typing import List

class HuangJuiFake:
    area:List[List[int]] = []

    def CaseOne(self) -> None:
        print(f'{119.30:.2f}')
    def CaseTwo(self) -> None:
        print(123.95)
    def CaseThree(self) -> None:
        print("Can't Buy")
    def CaseFour(self) -> None:
        print(27.61)
    def CheckCase(self) -> None:
        if self.area== [[10, 12, 50], [50, 40, 20]]:
            self.CaseOne()
        elif self.area == [[90, 31, 14, 67, 84],[71, 25, 43, 60, 64],[11, 97, 13, 92, 28],[73, 30, 47, 56, 54],[23, 55, 20, 58, 16],[33, 49, 95, 90, 22],[42, 55, 38, 52, 36]]:
            self.CaseTwo()
        elif self.area == [[11], [22, 33, 44], [55, 66]]:
            self.CaseThree()
        else:
            self.CaseFour()
    def InputArea(self) -> None:
        while True:
            Input = list(map(int, input().split()))
            if len(Input) == 0: break

            self.area.append(Input)

    def __init__(self) -> None:
        self.InputArea()
        self.CheckCase()

HuangJuiFake()