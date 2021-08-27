a = int(input('A : '))
b = int(input('B : '))
x = int(input('X : '))

timeB = x/b
timeA = x/a

print('Wait :',int((timeA - timeB)*60*60),'sec')