from typing import Dict, List
import json

def readData(fileName:str) -> List[Dict[str,str]]:
    return json.loads(open(fileName).read().strip())

datas = readData(input('Filename : '))
buy_object = input()

brand = min(list(filter(lambda r:r['Product type'] == buy_object,datas)) , key=lambda data:int(data['Cost']))

print(f'{brand["Brand"]} : {brand["Cost"]}')
