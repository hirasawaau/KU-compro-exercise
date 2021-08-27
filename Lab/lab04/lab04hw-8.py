def isPrimeNumber(n: int) -> bool:
    if n == 1: return False
    for i in range(2, n, 1):
        if n % i == 0:
            return False
    return True


N = int(input('N: '))

while True:
    if isPrimeNumber(N) and isPrimeNumber(N + 2):
        break
    N += 1

print((N, N + 2))
