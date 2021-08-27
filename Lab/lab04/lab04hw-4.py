phoneNumber = input()

if phoneNumber[1] == '8':
    result = 0
    for num in phoneNumber:
        result += int(num)
    if result % 13 == 0 and result < 56:
        print('Have bad luck.')
    else:
        print('Have good luck.')
elif phoneNumber[1] == '9':
    badLuck = False
    for i in range(len(phoneNumber) - 1):
        twoDec = phoneNumber[i] + phoneNumber[i + 1]
        if twoDec == '20' or twoDec == '13' or twoDec == '18' or twoDec == '80' or twoDec == '31' or twoDec == '93':
            badLuck = True
            break
    if badLuck:
        print('Have bad luck.')
    else:
        print('Have good luck.')