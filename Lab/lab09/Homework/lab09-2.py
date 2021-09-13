import json
from typing import Dict, List

Data = List[Dict[str,str]]

class WorldPopulation:

    datas:Data

    def __init__(self,fileName:str) -> None:
        self.readData(fileName)

    def readData(self,fileName:str) -> Data:
        self.datas =  json.loads(open(fileName).read().strip())

    def Menu01(self) -> None:
        print(len(datas))

    def Menu02(self) -> None:
        print(sum([int(data['population']) for data in datas]))

    def Menu03(self) -> None:
        filteredDatas = list(filter(lambda data:data['country'][0] == 'C',datas))
        print(len(filteredDatas))
        filteredDatas = list(filter(lambda data:len(data['country']) > 5,datas))
        print(len(filteredDatas))

    def Menu04(self) -> None:
        filteredDatas = list(filter(lambda data:int(data['population']) > 500e6,datas))
        print(len(filteredDatas))
        filteredDatas = list(filter(lambda data:250e6<=int(data['population'])<=750e6,datas))
        print(len(filteredDatas))
        filteredDatas = list(filter(lambda data:int(data['population']) < 10e6,datas))
        print(len(filteredDatas))


    def Menu05(self) -> None:
        sumPercent = sum([float(data['World']) for data in datas[0:20]]) * 100
        print(f'{sumPercent:.2f}')
        fivetyPercent = sum([float(data['World']) for data in datas[49:150]]) * 100
        print(f'{fivetyPercent:.2f}')

data = WorldPopulation(input('filename : '))

Input = input('Input : ')

if Input == '1':
    data.Menu01()
elif Input == '2':
    data.Menu02()
elif Input == '3':
    data.Menu03()
elif Input == '4':
    data.Menu04()
elif Input == '5':
    data.Menu05()