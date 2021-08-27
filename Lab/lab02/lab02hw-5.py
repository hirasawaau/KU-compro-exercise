permenantStack = [0, 0]
temporaryStack = [0, 0]
firstStack = [0, 0]

x = int(input())

firstStack = [x, 1]
temporaryStack = [x, 1]

while True:
    z = int(input())
    if z != firstStack[0]:
        temporaryStack = [z,1]
        break
    firstStack[1] += 1

while True:
    y = int(input())

    if temporaryStack[0] != y:
        if temporaryStack[1] > permenantStack[1]:
            permenantStack = temporaryStack
            if permenantStack[1] > firstStack[1]:
                firstStack = permenantStack
        if y == 0: break
        temporaryStack = [y, 1]

        # print(f'p={permenantStack} t={temporaryStack}')
        continue

    temporaryStack[1] += 1
    # print(f'p={permenantStack} t={temporaryStack}')

    continue

if firstStack[1] == permenantStack[1]:
    print(f'{firstStack[1]}\n{firstStack[0]}')
else:
    print(f'{permenantStack[1]}\n{permenantStack[0]}')
