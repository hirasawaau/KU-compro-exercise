police = 0
criminal = 100
n=1

while True:
    input_distance = int(input('Input distance: '))
    police+=input_distance
    criminal+=(2**n)

    print(f'Police distance: {police}\nCriminal distance: {criminal}')

    if police>= criminal:
        print('Caught him!')
        break

    n+=1
    continue