scores = []

while True:
    x = input('Input score (or just ENTER to finish): ')
    if len(x) == 0:
        break
    scores.append(int(x))

for i,score in enumerate(scores):
    print(f'Student #{i+1} score:',score)

print('Average score is',f'{sum(scores)/len(scores):.2f}')
print('Minimum score is',min(scores))
print('Maximum score is',max(scores))