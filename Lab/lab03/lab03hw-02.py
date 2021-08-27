def Head(n):
    print(' ' + (n * 'o'))
    if n != 2:
        for i in range(0, (n // 2) - 1):
            print(' ' + 'o' + ' ' * (n - 2) + 'o')

    print(' ' + (n * 'o'))


def Body(n):
    def printBody(symbol: bool):
        if symbol:
            print((n // 2) * '-' + '||' + (n // 2) * '-')
        else:
            print((n // 2) * ' ' + '||' + (n // 2) * ' ')

    if n == 2:
        printBody(True)
    else:
        for i in range(n - 1):
            printBody(i == (n // 2) - 1)


def Leg(n):
    r = n // 2
    for i in range(0, n, 2):
        print(' ' * r + '/' + ' ' * (i) + '\\')
        r -= 1


n = int(input())

Head(n)
Body(n)
Leg(n)