N = int(input('N: '))
M = int(input('M: '))

modulos = []

for i in range(N):
    number = int(input(f'Input number {i+1}: '))
    modulos.append(number % M)

modulosSet = set(modulos)
print(len(modulosSet))