n = int(input())
arrow = input('Arrow : ')
stick = input('Stick : ')
for i in range(n+1):
    if i==0: continue
    print(' ' * (n-i+1) + (arrow*((2*i)-1)),end='')
    print('\n',end='')
for i in range(n):
    print(' ' * (n) + stick)