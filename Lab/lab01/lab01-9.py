height = float(input("Hight : "))
cost = float(input("Cost : "))

if(height <= 1):
    if(cost <= 1000):
        print("YES")
    else:
        print("NO")
elif(height <= 4):
    if(cost <= 5000):
        print("YES")
    else:
        print("NO")
elif(height <= 8):
    if(cost <= 30000):
        print("YES")
    else:
        print("NO")
elif(height > 8):
    if(cost <= 75000):
        print("YES")
    else:
        print("NO")
