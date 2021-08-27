from typing import List


arr:List[int] = list(map(int , input().split()))

while True:
    x,y = map(int,input().split())
    
    try:
        arr[x]
        arr[y]
        if x>y and y>=0:
            break
        elif x == y:
            print(arr[x])
            continue
        
        if x<0:
            x = len(arr)+x
        if y<0:
            y = len(arr)+y
            
        if x>y:
            break
        summary = 0
        for i in range(x,y+1):
            summary+=arr[i]
        print(summary)
    except IndexError:
        badX = x < -len(arr) or x >= len(arr)
        badY = y < -len(arr) or y >= len(arr)
        if badX and badY:
            print('x and y Bad Input')
        elif badX:
            print('x Bad Input')
        else:
            print('y Bad Input')
        