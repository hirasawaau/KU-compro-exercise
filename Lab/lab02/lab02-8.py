isBuInjure:bool = input('Is Bulotelli injured?(y/n) ') == 'y'

if isBuInjure:
    print('Not available')
else:
    isBuLate = input('Is Bulotelli late for the training?(y/n) ') == 'y'
    if isBuLate:
        isBuWellTraining = input('Did Bulotelli perform well in training?(y/n) ') == 'y'
        if isBuWellTraining:
            print('Substitute')
        else:
            print('Not selected')
    else:
        print('Starter')