
def showO(n:int):
    for i in range(n):
        for j in range(1,n+1,2):
            print((((n-j)//2) * ' ') + (n)*(('O'*j) + (' ' * (n-j))))
        for j in range(n-2,0,-2):
            print((((n-j)//2) * ' ') + (n)*(('O'*j) + (' ' * (n-j))))
