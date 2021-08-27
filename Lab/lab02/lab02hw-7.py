n = int(input())

for i in range(1,n+1,2):
    space = int((n-i)/2)
    print(space * ' ' + 'O'*i)

for i in range(n-2,0,-2):
    space = int((n-i)/2)
    print(space * ' ' + 'O'*i)
