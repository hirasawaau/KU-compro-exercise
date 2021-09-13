def readFile(fileName):
    rawData = open(fileName).read().strip().split('\n')
    return [dict(zip(rawData[0].split(','),data.split(','))) for data in rawData[1:]]

def Menu1(datas:list):
    total = 0
    for data in datas:
        total+=int(data['Total Cases'])

fileName = input('filename: ')
Menu = int(input('type: '))
