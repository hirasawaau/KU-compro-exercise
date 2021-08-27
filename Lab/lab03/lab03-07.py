x = input()
first = x[0].upper()
last = x[-1].upper()

if first == last:
    print(f'YES\n{first}')
else:
    print('NO')
