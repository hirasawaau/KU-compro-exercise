def print_menu():
    print('''Coffee Menu
0. Finish
1. Latte = 40
2. Espresso = 45
3. Americano = 50
4. Mocca = 55
5. Cappuccino = 60
    ''')

def order_coffee():
    coffeeType = ['Finish','Latte','Espresso','Americano','Mocca','Cappuccino']
    coffeePrice = {
    'Latte':40,
    'Espresso':45,
    'Americano':50,
    'Mocca':55,
    'Cappuccino':60
    }
    order_dict = {}
    total_price = 0
    while True:
        coffee = int(input('Coffee type: '))
        if coffee == 0:
            print(f'Total price: {total_price}')
            return order_dict,total_price
        coffeeStr = coffeeType[coffee]
        amount = int(input(f'Amount of {coffeeStr}: '))
        total_price+=coffeePrice[coffeeStr]*amount
        try:
            order_dict[coffeeStr]+=amount
        except:
            order_dict.update({coffeeStr:amount})

def change(total_price,pay):
    change_total = pay-total_price
    print("Customer's change:",change_total)
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
    change1 = change_total
    print('Change 1000:',change1000) if change1000 != 0 else None
    print('Change 500:',change500) if change500 != 0 else None
    print('Change 100:',change100) if change100 != 0 else None
    print('Change 50:',change50) if change50 != 0 else None
    print('Change 20:',change20) if change20 != 0 else None
    print('Change 10:',change10) if change10 != 0 else None
    print('Change 5:',change5) if change5 != 0 else None
    print('Change 1:',change1) if change1 != 0 else None

def print_receipt(orders_dict:dict, customer_name, total_price):

    print('--------- receipt ---------\nCPE35 COFFEE SHOP')
    print(f'Customer name: {customer_name}')
    for coffee,amount in orders_dict.items():
        print(f'{coffee} {amount}, ',end="")
    print(f'{total_price} baht')
    print('Thank you\n---------------------------')


def print_report(sales_dict:dict):
    total_price = sum(sales_dict.values())
    print('---- Daily Sale Report ----')
    for name,price in sales_dict.items():
        print(f'{name} {price} baht')
    print(f'Total sale: {total_price} baht')
    print('---------------------------')

sales_dict = {}
while True:
    print_menu()
    customer_name = input("Customer name: ")
    if customer_name == "end day":
        break
    orders_dict, total_price = order_coffee()
    if customer_name not in sales_dict:
        sales_dict[customer_name] = total_price
    else:
        sales_dict[customer_name] += total_price

    pay = int(input("Customer pay: "))
    change(total_price,pay)
    print_receipt(orders_dict, customer_name, total_price)

print_report(sales_dict)
