x = int(input())
y = int(input())
p = int(input())



word = 0
space = 0
for i in range(x,y+1,1):
    if space>0:
        space-=1
        continue
    if i%p == 0:
        space=10
        continue
    
    if word<10:
        print(i , end=' ')
        word+=1
    else:
        print(f'\n{i}' , end=' ')
        word=1
