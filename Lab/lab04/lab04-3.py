x, y = map(int, input('Grass : ').split())

arr = [int(x) for x in input().split()]
jump = 0

for i in arr:
    if (i > y): jump += 1

print(jump)