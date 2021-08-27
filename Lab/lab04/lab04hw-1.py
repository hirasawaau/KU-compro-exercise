name = input('Input name: ')
l = 0
for i in name:
    for index, value in enumerate(name):
        if l == index:
            print(value.upper(), end="")
        else:
            print(value, end="")
    l += 1
    print()
