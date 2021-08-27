from math import factorial


def C(n, r):
    result = factorial(n) / ((factorial(n - r) * factorial(r)))
    return int(result)


n = int(input())
for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        print(C(i, j), end=' ')
    print()
