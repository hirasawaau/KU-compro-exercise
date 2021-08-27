name = list(input('Input name: '))
reversedName = name[::-1]

for index, value in enumerate(name):
    for j in name:
        if j == value:
            print(j.upper(), end="")
        else:
            print(j, end="")

    print(end=" ")

    value = reversedName[index]
    for j in reversedName:
        if j == value:
            print(j.upper(), end="")
        else:
            print(j, end="")

    print()
