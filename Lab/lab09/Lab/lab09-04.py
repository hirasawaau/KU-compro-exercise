from typing import Any, Dict, List
import json

Data = Dict[str,List[Dict[str,Any]]]

def change(total_price,pay):
    if total_price == pay:
        return print('no change')
    change_total = pay-total_price
    # print("Customer's change:",change_total)
    change1000 = change_total//1000
    change_total = change_total-(change1000*1000)
    change500 = change_total//500
    change_total = change_total-(change500*500)
    change100 = change_total//100
    change_total = change_total-(change100*100)
    change50 = change_total//50
    change_total = change_total-(change50*50)
    change20 = change_total//20
    change_total = change_total-(change20*20)
    change10 = change_total//10
    change_total = change_total-(change10*10)
    change5 = change_total//5
    change_total = change_total-(change5*5)
    change2 = change_total//2
    change_total = change_total-(change2*2)
    change1 = change_total
    print('1000 :',change1000) if change1000 != 0 else None
    print('500 :',change500) if change500 != 0 else None
    print('100 :',change100) if change100 != 0 else None
    print('50 :',change50) if change50 != 0 else None
    print('20 :',change20) if change20 != 0 else None
    print('10 :',change10) if change10 != 0 else None
    print('5 :',change5) if change5 != 0 else None
    print('2 :',change2) if change2 != 0 else None
    print('1 :',change1) if change1 != 0 else None


def readData(fileName:str) -> Data:
    return json.loads(open(fileName).read().strip())



datas = readData(input('Enter json filename : '))

products,customers = datas['products'],datas['customers']

productDict = {}

for product in products:
    items = list(product.items())
    # print(items)
    productDict.update({items[0][1]:int(items[1][1])})

# print(productDict)

customerDict:Dict[str,int] = {}

for customer in customers:
    name:str = customer['customer_name']
    orders:Dict[str,int] = customer['order']
    # print(name)

    for order in orders.items():
        # print((productDict[order[0]] * order[1]))
        try:
            # print(productDict[order[0]] * order[1])
            customerDict[name][0] += (productDict[order[0]] * order[1])
        except KeyError:
            customerDict.update({name : [productDict[order[0]] * order[1],customer['money']]})

# print(customerDict)

for customerItem in sorted(customerDict.items() , key=lambda item:ord(item[0][0])):
    print(customerItem[0])
    change(*customerItem[1])
    print()