r = int(input())
k = 0

num = 1
BaseMatrix = [[0 for i in range(r)] for j in range(r)]

def matrixImplement(i,j,direction):
    global num
    BaseMatrix[i][j] = num
    if num == r**2:
        return
    num+=1
    if direction==0:
        if i-1>=0 and j-1>=0:
            matrixImplement(i-1,j-1,direction)
        elif i-1>=0 and j-1<0:
            matrixImplement(i-1,j,1-direction)
        elif i-1<0 and j-1<0:
            matrixImplement(i,j+1,1-direction)
        elif i-1<0 and j-1>=0:
            matrixImplement(i,j+1,1-direction)
    if direction==1:
        if i+1<r and j+1<r:
            matrixImplement(i+1,j+1,direction)
        elif i+1>=r and j+1<r:
            matrixImplement(i,j+1,1-direction)
        elif i+1>=r and j+1>=r:
            matrixImplement(i-1,j,1-direction)
        elif i+1<r and j+1>=r:
            matrixImplement(i-1,j,1-direction)

matrixImplement(r-1,0,0)
for i in range(r):
    for j in range(r):
        print(f'{BaseMatrix[i][j]:3.0f}',end=' ')
    print()

    
    
