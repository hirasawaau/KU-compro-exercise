day = int(input('How many day : '))

sum_price = 0

for i in range(1,day+1):
    price = float(input(f'Input price in day {i} : '))
    sum_price+=((price*(96-i))/100)

print(f'Summary price = {sum_price:.2f}')

    