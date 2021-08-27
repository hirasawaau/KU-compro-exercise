def isPrimeNumber(n: int) -> bool:
    if n == 1: return False
    for i in range(2, n, 1):
        if n % i == 0:
            return False
    return True


primes = []

while True:
    number = int(input())
    if number == 0:
        break
    if isPrimeNumber(number):
        primes.append(number)

line = 0
for i in primes:
    if line == 10:
        line = 0
        print(f'\n{i}', end=" ")
    else:
        print(i, end=" ")
    line += 1
