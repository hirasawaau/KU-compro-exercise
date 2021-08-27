def sum_price():
    print('Menu')
    print('0. Finish')
    print('1. Latte = 40')
    print('2. Espresso = 45')
    print('3. Americano = 50')
    print('4. Mocca = 55')
    print('5. Cappuccino = 60')
    summaryPrice = 0
    while True:
        coffeeType = int(input('coffee : '))
        if coffeeType == 0:
            break
        amount = int(input('amount : '))
        if coffeeType == 1:
            summaryPrice += amount * 40
        elif coffeeType == 2:
            summaryPrice += amount * 45
        elif coffeeType == 3:
            summaryPrice += amount * 50
        elif coffeeType == 4:
            summaryPrice += amount * 55
        elif coffeeType == 5:
            summaryPrice += amount * 60
    print(f"total price : {summaryPrice}")
    return summaryPrice


def change(total_price, pay):
    charge = pay - total_price
    print(f"customer's change : {charge}")
    print(f'change 1000 : {(int(charge//1000))}') if int(charge //
                                                         1000) > 0 else print(
                                                             end='')
    charge -= int(1000 * (charge // 1000))
    print(f'change 500 : {int(charge//500)}') if int(charge //
                                                     500) > 0 else print(
                                                         end='')
    charge -= int(500 * (charge // 500))
    print(f'change 100 : {int(charge//100)}') if int(charge //
                                                     100) > 0 else print(
                                                         end='')
    charge -= int(100 * (charge // 100))
    print(f'change 50 : {int(charge//50)}') if int(charge //
                                                   50) > 0 else print(end='')
    charge -= int(50 * (charge // 50))
    print(f'change 20 : {int(charge//20)}') if int(charge //
                                                   20) > 0 else print(end='')
    charge -= int(20 * (charge // 20))
    print(f'change 10 : {int(charge//10)}') if int(charge //
                                                   10) > 0 else print(end='')
    charge -= int(10 * (charge // 10))
    print(f'change 5 : {int(charge//5)}') if int(charge // 5) > 0 else print(
        end='')
    charge -= int(5 * (charge // 5))


total_price = sum_price()
pay = int(input('customer pay : '))
change(total_price, pay)


