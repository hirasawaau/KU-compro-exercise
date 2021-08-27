a,b,c,d = map(int,input().split())
one,two,three,four = 0,0,0,0
if (a >= b and a >= c and a >= d):
    four = a
    # b = 3
    if (b >= c and b >= d):
        three = b
        # c = 2
        if (c >= d):
            two = c
            one = d
        else:
            one = c
            two = d
    elif (c >= b and c >= d):
        three = c
        if (b > d):
            two = b
            one = d
        else:
            one = b
            two = d
    elif (d >= c and d >= b):
        three = d
        if (c >= b):
            two = c
            one = b
        else:
            one = c
            two = b
# B maxest
elif (b >= a and b >= c and b >= d):
    four = b
    if (a >= c and a >= d):
        three = a
        if (c >= d):
            two = c
            one = d
        else:
            one = c
            two = d
    elif (c >= a and c >= d):
        three = c
        if (a >= d):
            two = a
            one = d
        else:
            one = a
            two = d
    elif (d >= c and d >= a):
        three = d
        if (c >= a):
            two = c
            one = a
        else:
            one = c
            two = a
# C maxest
elif (c >= a and c >= b and c >= d):
    four = c
    if (b >= a and b >= d):
        three = b
        if (d >= a):
            two = d
            one = a
        else:
            one = d
            two = a
    elif (a >= b and a >= d):
        three = a
        if (b >= d):
            two = b
            one = d
        else:
            one = b
            two = d
    elif (d >= a and d >= b):
        three = d
        if (a >= b):
            two = a
            one = b
        else:
            one = a
            two = b
elif (d >= a and d >= b and d >= c):
    four = d
    if (b >= a and b >= c):
        three = b
        if (c >= a):
            two = c
            one = a
        else:
            one = c
            two = a
    elif (a >= b and a >= c):
        three = a
        if (b >= c):
            two = b
            one = c
        else:
            one = b
            two = c
    elif (c >= a and c >= b):
        three = c
        if (a >= b):
            two = a
            one = b
        else:
            one = a
            two = b

print(f'{one} {two} {three} {four}')
