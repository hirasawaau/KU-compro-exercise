def lcm(a,b):
    if a == 0 or b == 0:
        return 0
    i = 1
    while True:
        if i%a == 0 and i%b == 0:
            return i
        i+=1

def gcd(a,b):
    return (a*b)//lcm(a,b)


a = int(input('a : '))
b = int(input('b : '))

print(f'GCD : {gcd(a,b)}')
print(f'LCM : {lcm(a,b)}')
