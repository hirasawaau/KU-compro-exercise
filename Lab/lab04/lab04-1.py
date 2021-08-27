N = 10
def Nplus(n):
    global N
    N+=n

def Nminus(n):
    global N
    N-=n

def Ntimes(n):
    global N
    N = n*N

def Ndivided(n):
    global N
    N = N/n

Nplus(5)
Nminus(3)
Ntimes(6)
Ndivided(3)
print(f'{N:.0f}')

c = input()
if c == '1':
    Nplus(12)
    print(f'{N:.0f}')
if c == '2':
    Nminus(6)
    print(f'{N:.0f}')
if c == '3':
    Ntimes(2)
    print(f'{N:.0f}')
if c == '4':
    Ndivided(6)
    print(f'{N:.0f}')