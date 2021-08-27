from typing import List

data = {}

n = int(input())

for i in range(n):
    msg = input().split()
    if msg[2] == 'father' or msg[2] == 'mother':
        try:
            data[msg[4]].append(msg[0])
        except:
            data.update({msg[4]: [msg[0]]})

# is A and X are sibling
question = input().split()

isSibling = False

try:
    parents1: List[str] = data[question[1]]
    parents2: List[str] = data[question[3]]

    for i in parents1:
        try:
            parents2.index(i)
            isSibling = True
            break
        except ValueError:
            continue
except:
    pass

if isSibling: print('Yes')
else: print('No')