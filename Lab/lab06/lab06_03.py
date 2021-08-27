data = {}

i=0
while True:
    stuId = input('Student ID : ')
    if stuId == '0':
        break
    year = int(input('years : '))
    try:
        data[stuId]=year
    except KeyError:
        data.setdefault(stuId,year)
    i+=1

sepYear = int(input('Separate year: '))
item_data = list(data.items())
filtered_data = filter(lambda d:d[1] >= sepYear,item_data)
for i in filtered_data:
    print(i[0])