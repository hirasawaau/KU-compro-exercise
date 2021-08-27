def isInList(arr: list, value: int) -> bool:
    try:
        arr.index(value)
        return True
    except:
        return False


d = int(input('d: '))
m = int(input('m: '))
y = int(input('y: '))

have31: list = [1, 3, 5, 7, 8, 10, 12]
have30: list = [4, 6, 9, 11]
have2x: list = [2]

is366 = False
if y % 4 == 0 and y % 100 != 0:
    is366 = True

day = 0

for month in range(1, m + 1):
    if month == m:
        day += d
        break
    if isInList(have31, month):
        day += 31
        continue
    if isInList(have30, month):
        day += 30
        continue
    if isInList(have2x, month):
        day += 29 if is366 else 28

print(day)
    
    
