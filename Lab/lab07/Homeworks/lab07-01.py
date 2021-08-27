N = int(input('N : '))

data = {}

for i in range(N):
    raw = input().split()
    data.update({raw[0]:int(raw[1])})

patterns = [i.strip() for i in input().split('+')]

print(sum([data[pattern] for pattern in patterns]))