from typing import Dict, List
import json

def readData(fileName:str) -> List[Dict[str,str]]:
    return json.loads(open(fileName).read().strip())

datas = readData(input('Filename : '))

name = input('Data : ')

try:
    int(name)
    foundData = None

    for data in datas:
        if data['ID number'] == name:
            foundData = data
            break

    if foundData:
        print(f'Found in blacklist')
        for item in foundData.items():
            print(f'{item[0]} : {item[1]}')

    else:
        print('Not found in blacklist')
except:


    foundData = None

    for data in datas:
        if data['name'] == name:
            foundData = data
            break

    if foundData:
        print(f'Found in blacklist')
        for item in foundData.items():
            print(f'{item[0]} : {item[1]}')

    else:
        print('Not found in blacklist')