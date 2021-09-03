from typing import Dict, List


fileName = input('File name: ')

with open(fileName) as file:
    rawData = file.read()
    # print(rawData)
    MapDict:Dict[int,List[str]] = {}
    header = 0
    for data in rawData.split('\n'):
        try:
            header = int(data)
            if header == 0:
                break
            MapDict.update({header:[]})
        except:
            MapDict[header].append(data)


items = sorted(MapDict.items(),key=lambda r:r[0])

for i in items:
    for j in i[1]:
        print(j)