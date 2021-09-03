from typing import Dict, List


def readData(path:str) -> List[Dict[str,int]]:
    with open(path) as file:
        header = file.readline().strip().split(',')
        rawDatas = file.read().split('\n')

    data = [dict(zip(header,[int(i) for i in rawData.split(',')])) for rawData in rawDatas[:-1]]
    return data


def CorruptionFilter(d:Dict[str,int]):
    if d['Height'] <= 1:
        return not d['Cost'] <= 1000
    elif d['Height'] <= 4:
        return not d['Cost'] <= 5000
    elif d['Height'] <= 8 :
        return not d['Cost'] <= 30000
    elif d['Height'] > 8:
        return not d['Cost'] <= 75000
    else:
        return True

fileName = input('Filename : ')
data = readData(fileName)

filterData = list(filter(CorruptionFilter,data))

if len(filterData) == 0:
    print('No')
else:
    print('Yes')
    corruption_no = [i['No'] for i in filterData]
    corruption_no.sort()
    for i in corruption_no:
        print(i)
