# Lek in hell

N = int(input('N = '))
M = int(input('M = '))

costs = []

for i in range(N):
    costs.append(int(input(f'cost of day {i+1} = ')))


minCost = 1000000

for i in range(N):
    if M+i > N:
        break
    else:
        cost = sum(costs[i:M+i])
        if cost < minCost:
            minCost = cost

print(f'Min cost of {M} days = {minCost}')

