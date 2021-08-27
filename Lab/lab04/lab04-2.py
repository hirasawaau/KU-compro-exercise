from sys import maxsize

N = int(input('N = '))
R = []
for i in range(N):
    R.append(int(input(f'cost of day {i+1} = ')))

summary = maxsize

for i in range(len(R) - 2):
    result = R[i] + R[i + 1] + R[i + 2]
    summary = result if result < summary else summary

print(f'Min cost of 3 days = {summary}')
