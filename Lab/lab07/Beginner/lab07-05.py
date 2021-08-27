scores = []
while True:
    x = input('Input score (or just ENTER to finish): ')
    if len(x) == 0:
        break
    scores.append(int(x))

scores.sort(reverse=True)

for rank,score in enumerate(scores):
    print(f'Rank #{rank+1}: {score}')