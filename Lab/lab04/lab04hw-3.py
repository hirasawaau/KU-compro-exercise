arr = list(map(int, input().split()))

while True:
    menu, x = input().split()
    x = int(x)
    if menu == 'A':
        arr.append(x)
        continue
    elif menu == 'S':
        print(arr[x])
    elif menu == 'R':
        del arr[x]
    elif menu == 'E' and x == 0:
        break
for i in arr:
    print(i, end=" ")
