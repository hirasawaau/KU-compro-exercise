ogPassword = list(input())

isCorrect = True

for i in ogPassword:
    password = input()
    if password != i:
        isCorrect = False
        break

if isCorrect:
    print('Succeed!!')
else:
    print('Fail!!')