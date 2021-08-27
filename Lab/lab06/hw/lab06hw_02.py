Text = input('Text: ')
SubString = input('Substring: ')

s = []

if Text.partition(SubString)[0] == Text:
    print('Not found')
else:
    P = Text.partition(SubString)
    s.extend(P[0:3])
    while True:
        R = P[2].partition(SubString)
        if R[0] == P[2]:
            break
        s.pop()
        s.extend(R[0:3])
        P = R

r = '['
# print(s)

for i in range(len(s)):
    print(s[i],end='')
    if i == len(s) - 1:
        break
    print(r,end='')
    if r == '[':
         r = ']'
    else:
        r = '['