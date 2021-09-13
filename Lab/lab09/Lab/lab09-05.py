from typing import Dict, List
import json

def readData(fileName:str) -> List[Dict[str,str]]:
    return json.loads(open(fileName).read().strip())

datas = readData(input('Filename : '))
lengthType = input('type : ')

lengthDict:Dict[str,List[float]] = {}

for data in datas:
    try:
        lengthDict[data['species']].append(data[lengthType])
    except:
        lengthDict.update({lengthDict[data['species']] : [data[lengthType]]})


for i in lengthDict.items():
    print(f'{i[0]} = {sum(i[1]) / len(i[1]):.2f}')