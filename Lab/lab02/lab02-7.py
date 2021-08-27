minutes = int(input('How long have Buzz played ?: '))

hour = int(minutes / 60)
min = int(minutes % 60)

# print(f'{hour} hours {min} mins')

if (min > 20):
    hour += 1
discount = 1
if hour < 2:
    discount = 1
elif hour < 4:
    discount = 0.9
elif hour < 5:
    discount = 0.8
else:
    discount = 0.7

sum_price = -int(hour * 900 * -discount)

print(f'Total price is {int(sum_price)} baht.')