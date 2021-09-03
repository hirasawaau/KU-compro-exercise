from typing import Dict


fileName = input('File name: ')


with open(fileName) as file:
    price_list:Dict[str,int] = {}
    buy_list:Dict[str,int] = {}
    Type = ''
    rawData = file.read()
    print(rawData)
    for f in rawData.split('\n'):
        f = f.strip()
        if f == 'Price':
            Type = 'Price'
            continue
        elif f == 'List':
            Type = 'List'
            continue
        
        obj = f.split()

        if Type == 'Price':
            price_list.update({obj[0]:int(obj[1])})
        elif Type == 'List':
            buy_list.update({obj[0]:int(obj[1])})

total = 0

for T,N in buy_list.items():
    try:
        total+=price_list[T]*N
    except:
        continue

print(f'Total price: {total}')        


        