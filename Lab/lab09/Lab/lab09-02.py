import json
from typing import ChainMap, Dict, List

Data = Dict[str,Dict[str,str]]

def readData(fileName:str) -> Data:
    return json.loads(open(fileName).read().strip())

def Case1(data:Data,chractors:str) -> None:
    datas = data.values()
    foundDatas = []
    chractors:List[str] = chractors.split(',')
    chractors.sort()
    for d in datas:
        for chractor in chractors:
            if d["id"] == int(chractor):
                foundDatas.append(d)

    for foundData in foundDatas:
        print(f'{foundData["id"]}\t---\t{foundData["name"]}\t---\t{foundData["title"]}')

def Case2(data:Data,chractors:str) -> None:
    datas = data.values()
    foundDatas = []
    chractors:List[str] = chractors.split(',')
    chractors.sort()
    for d in datas:
        for chractor in chractors:
            if d["name"][0] == chractor:
                foundDatas.append(d)

    for foundData in foundDatas:
        print(f'{foundData["id"]}\t---\t{foundData["name"]}\t---\t{foundData["title"]}')


def Case3(data:Data,chractors:str) -> None:
    datas = data.values()
    foundDatas = []
    chractors:List[str] = chractors.split(',')
    chractors.sort()
    for d in datas:
        for chractor in chractors:
            title = d['title'].strip('the ').strip('The ')
            if title[0] == chractor:
                foundDatas.append(d)

    for foundData in foundDatas:
        print(f'{foundData["id"]}\t---\t{foundData["name"]}\t---\t{foundData["title"]}')


data = readData(input('Filename : '))
case = int(input('Case : '))

if case == 0:
    Case1(data,input('Character : '))
elif case == 1:
    Case2(data,input('Character : '))
else:
    Case3(data,input('Character : '))
