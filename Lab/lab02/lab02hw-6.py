n = int(input())

for i in range(1, n + 1, 2):
    space = int((n - i) / 2)
    print(space * ' ' + 'O' * i)
