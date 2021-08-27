from sys import maxsize

positiveNumber = 0
summary = 0
arr = []

while positiveNumber < 5:
    x = int(input('Enter a positive number: '))
    if (x > 0):
        arr.append(x)
        summary += x
        positiveNumber += 1

arr.sort()

# if (len(arr)+1) % 2 == 1:
#     a = (len(arr) + 1) // 2
#     med = arr[a - 1]
# else:
#     a = (len(arr) + 1) // 2
#     b = a + 1
#     med = (arr[a - 1] + arr[b - 1]) // 2
med = arr[(len(arr) + 0) // 2]
print(f'sum: {summary}')
print(f'min: {arr[0]}')
print(f'max: {arr[-1]}')
print(f'med: {med}')
