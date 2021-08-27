def plus(total, value) -> int:
    return total + value


def minus(total, value) -> int:
    return total - value


food = int(input('How many food you have : '))
total = 0
for i in range(food):
    value, indict = map(int, input().split())
    # print(value, indict)
    total = plus(total, value) if indict == 1 else minus(
        total, value) if indict == -1 else None

print(total)
