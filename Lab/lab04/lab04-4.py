N = int(input('N : '))

ar = [int(x) for x in input().split()]


def toBool(i: int):
    return i == 1 if i != 0 else None


arr = list(map(toBool, ar))

isSplit = True
# if ar[1] == 1:

#     for i in range(0, N, 2):
#         if i == 0:
#             print('T')
#             ar[i] = 2
#             continue
#         elif i == N - 1:
#             if ar[i - 1] == 2:
#                 isSplit = False
#                 break
#             else:
#                 ar[i] = 2
#         else:
#             if ar[i + 1] == 2 or ar[i - 1] == 2:
#                 isSplit = False
#                 break
#             else:
#                 ar[i] = 2
# elif ar[1] == 2:
#     for i in range(0, N, 2):
#         if i == 0:
#             ar[i] = 1
#             continue
#         elif i == N - 1:
#             if ar[i - 1] == 1:
#                 isSplit = False
#                 break
#             else:
#                 ar[i] = 2
#         else:
#             if ar[i + 1] == 1 or ar[i - 1] == 1:
#                 isSplit = False
#                 break
#             else:
#                 ar[i] = 2
countNone = 0
for i in range(N):
    if arr[i] != None:
        start = (i, ar[i])
        break
    else:
        countNone += 1

# backward
if countNone < N:
    for i in range(start[0], -1, -1):
        if i == start[0]:
            if arr[i - 1] == arr[i]:
                isSplit = False
            arr[i - 1] = not arr[i]
            continue

        if i == 0:
            if arr[i + 1] == arr[i]:
                isSplit = False
                break
            continue

        if (arr[i - 1] == arr[i] or arr[i]
                == arr[i + 1]) and arr[i - 1] != None and arr[i + 1] != None:
            isSplit = False
            break
        else:
            arr[i - 1] = not arr[i]
    # forward
    for i in range(start[0], N):
        if i == start[0]:
            arr[i + 1] = not arr[i]
            continue

        if i == N - 1:
            if arr[i - 1] == arr[i]:
                isSplit = False
                break
            continue

        if (arr[i - 1] == arr[i] or arr[i]
                == arr[i + 1]) and arr[i - 1] != None and arr[i + 1] != None:
            isSplit = False
            break
        else:
            arr[i + 1] = not arr[i]

    if isSplit:
        print('yes')
    else:
        print('no')
else:
    print('yes')
# print(arr)
