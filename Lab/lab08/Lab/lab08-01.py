from typing import Dict,List

def readFile(path:str) -> Dict[str,int]:
    with open(path,'r') as file:
        rawDatas = file.read().strip().split('\n')

    data:Dict[str,int] = {}
    for rawData in rawDatas:
        header = ''
        scores = []
        for index,value in enumerate(rawData.split()):
            if index == 0:
                data.update({value:[]})
                header = value
            else:
                scores.append(int(value))
        scores.sort()
        data[header] = sum(scores[1:len(scores)-1])

    
    return data

fileName = input('File name: ')
data = readFile(fileName)

maxValue = max(data.values())

cleanData = filter(lambda data:data[1] == maxValue , data.items())

print(maxValue)
for i in cleanData:
    print(i[0])
    