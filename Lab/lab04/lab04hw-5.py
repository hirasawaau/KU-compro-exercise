luckyNumber = int(input('Enter lucky number : '))
amountCandidates = int(input('Enter amount of candidates : '))

idCard = ''
amountOfNumber = 0

for i in range(amountCandidates):
    idCardTem = input(f'Enter ID card number {i+1}: ')
    luckyCount = idCardTem.count(str(luckyNumber))
    if luckyCount > amountOfNumber:
        idCard = idCardTem
        amountOfNumber = luckyCount
    elif luckyCount == amountOfNumber:
        if int(idCardTem) > int(idCard):
            idCard = idCardTem

print(f'Winner: {idCard}')