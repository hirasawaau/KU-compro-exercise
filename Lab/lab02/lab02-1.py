n = int(input('number of electric poles : '))
max1 = 0
max2 = 0

for i in range(n):
    cost = int(input())
    if cost > max1:
        max1 = cost
    
    elif cost > max2:
        max2 = cost


if max2*3 <= max1:
    print('YES')
    print(max1)

else:
    print('NO')