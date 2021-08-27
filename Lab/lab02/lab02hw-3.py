height = int(input('hight of electric poles : '))
number = int(input('number of electric poles : '))

isGay: bool = False
Summary: int = 0
Avg: int = 0

max1: int = 0
max2: int = 0

for i in range(number):
    cost = int(input())
    Summary += cost
    if cost > max1:
        max2 = max1
        max1 = cost
    elif cost > max2:
        max2 = cost

ratio = max1 // max2

if ratio >= 3:
    isGay = True
    Summary -= max1
    Avg = (Summary // (number - 1)) + (max1 // ratio)

else:
    isGay = False
    Avg = Summary // number

print(f'Avg : {Avg}')

# ถ้าเสาไฟเกเร
if isGay:
    if (height <= 1):
        if (Avg <= 3000):
            print("NO")
        else:
            print(f"YES {Avg-3000}")
    elif (height <= 4):
        if (Avg <= 10000):
            print("NO")
        else:
            print(f"YES {Avg-10000}")
    elif (height <= 8):
        if (Avg <= 50000):
            print("NO")
        else:
            print(f"YES {Avg-50000}")
    elif (height > 8):
        if (Avg <= 100000):
            print("NO")
        else:
            print(f"YES {Avg-100000}")
else:
    if (height <= 1):
        if (Avg <= 1000):
            print("NO")
        else:
            print(f"YES {Avg-1000}")
    elif (height <= 4):
        if (Avg <= 5000):
            print("NO")
        else:
            print(f"YES {Avg-5000}")
    elif (height <= 8):
        if (Avg <= 30000):
            print("NO")
        else:
            print(f"YES {Avg-30000}")
    elif (height > 8):
        if (Avg <= 75000):
            print("NO")
        else:
            print(f"YES {Avg-75000}")
