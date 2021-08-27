def light(n: int):
    leftSpace = 0
    centerSpace = 3 * n - 4
    for i in range(n - 1):
        print(leftSpace * ' ' + '*' + (centerSpace) * ' ' + '*')
        centerSpace -= 2
        leftSpace += 1

    return leftSpace, centerSpace + 2


def body(n: int, leftSpace) -> None:
    if n == 2:
        print(' **\n ** ')
        return
    print(leftSpace * ' ' + '*' * n)
    i = 0
    while n != 2 and i < n - 2:
        print(leftSpace * ' ', end='')
        print('*' + ' ' * (n - 2) + '*')
        i += 1
    print(leftSpace * ' ' + '*' * n)


def lightReward(n: int, leftSpace, centerSpace) -> None:
    leftSpace -= 1
    if n == 2:
        print('*  *')
    elif n % 2 == 1:
        for i in range(n - 1):
            print(leftSpace * ' ' + '*' + centerSpace * ' ' + '*')
            centerSpace += 2
            leftSpace -= 1
    else:
        for i in range(n - 1):
            print(leftSpace * ' ' + '*' + centerSpace * ' ' + '*')
            centerSpace += 2
            leftSpace -= 1


def draw(n):
    leftSpace, centerSpace = light(n)
    body(n, leftSpace)
    lightReward(n, leftSpace, centerSpace)


draw(int(input()))
