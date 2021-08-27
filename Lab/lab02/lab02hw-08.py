a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

while True:
    haveTwoZero: bool = (a == 0 and b == 0) or (a == 0
                                                and c == 0) or (b == 0
                                                                and c == 0)
    if haveTwoZero: break
    if a >= b and a >= c:
        a -= 1
        if b > c:
            b -= 1
            c += 1
        elif b <= c:
            b += 1
            c -= 1

    elif b >= c and b >= a:
        b -= 1
        if a > c or a == c:
            a -= 1
            c += 1
        elif a <= c:
            a += 1
            c -= 1
    elif c >= a and c >= b:
        c -= 1
        if a > b or a == b:
            a -= 1
            b += 1
        elif a <= b:
            a += 1
            b -= 1

# Output
if a == 1: print('A')
elif b == 1: print('B')
elif c == 1: print('C')
