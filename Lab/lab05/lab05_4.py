n = int(input('Number of inputs: '))
data = {}
for i in range(n):
    name,score = map(str , input().split())
    data.setdefault(name,score)

while True:
    stdName = input('student: ')
    if stdName == '':
        break
    print(f"{stdName}'s score is {data[stdName]}")

print('End')