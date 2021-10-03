class Matrix(list):
    def sortAndAssign(self,y,x):
        arr = []
        i = x
        j = y

        while True:
            try:
                arr.append(self[j][i])
            except:
                break
            i+=1
            j+=1

        arr.sort()
        i = x
        j = y
        k = 0
        while True:
            try:
                self[j][i] = arr[k]
            except:
                break
            i+=1
            j+=1
            k+=1

    def printMat(self):
        for i in range(len(self)):
            for j in range(len(self[0])):
                print(self[i][j], end = " ")
            print()


# %%
M = int(input('M: '))
N = int(input('N: '))

matrix = Matrix([list(map(int,input().split())) for _ in range(M)])


# %%
for i in range(M):
    for j in range(N):
        matrix.sortAndAssign(i,j)

print('sorted matrix is:')

# %%
matrix.printMat()


