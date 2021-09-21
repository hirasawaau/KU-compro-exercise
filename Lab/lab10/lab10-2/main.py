from typing import Any, Dict, List
import json

class Account:
    name:str
    acc_number:str
    money:int
    histories:List[Dict[str,int]]

    def __init__(self,data:Dict[str,Any]) -> None:
        self.name = data['name']
        self.acc_number = data['account number']
        self.money = data['money']
        self.histories = []

    def __str__(self):
        return self.acc_number

    def show_data(self):
        print(f'Name : {self.name}')
        print(f'Account number : {self.acc_number}')
        print(f'Money : {self.money}')
        print(f'History : ',end='')
        if len(self.histories) == 0:
            print()
        for _history in self.histories:
            history = list(_history.items())[0]
            print(f"{history[0]} : {history[1]}")

    def deposit(self):
        amount = int(input('Amount : '))
        self.money+=amount
        self.histories.append({'Deposit':amount})
        print(f'Current money : {self.money}')

    def withdraw(self):
        amount = int(input('amount : '))
        self.money-=amount
        self.histories.append({'Withdraw':amount})
        print(f'Current money : {self.money}')
    
    def show_history(self):
        for _history in self.histories:
            history = list(_history.items())[0]
            print(f"{history[0]} : {history[1]}") 




def readFile(fileName:str) -> Dict[str,Account]:
    with open(fileName) as file:
        datas:List[Dict[str,Any]] = json.loads(file.read().strip())
    acc_numbers = [data['account number'] for data in datas]
    accountDatas = [Account(data) for data in datas]
    return dict(zip(acc_numbers,accountDatas))

def readFileAsList(fileName:str) -> Dict[str,Account]:
    with open(fileName) as file:
        datas:List[Dict[str,Any]] = json.loads(file.read().strip())
    
    return [Account(data) for data in datas]

fileName = input('Filename : ')
accounts = readFile(fileName)
classes = readFileAsList(fileName)

selectedAccount:Account = accounts[input('Account number : ')]

while True:
    # print(selectedAccount)
    menu = int(input('Menu : '))
    if menu == 1:
        selectedAccount.show_data()
    elif menu == 2:
        selectedAccount.deposit()
    elif menu == 3:
        selectedAccount.withdraw()
    elif menu == 4:
        selectedAccount.show_history()
    elif menu == 5:
        accounts[selectedAccount.acc_number] = selectedAccount
        selectedAccount = accounts[input('Account number : ')]
    elif menu == 0:
        break