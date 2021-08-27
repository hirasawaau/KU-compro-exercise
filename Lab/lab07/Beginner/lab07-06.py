import math
from typing import List

def calculateScore(xi:int,sd:int,avg:int) -> str:
    if xi>= avg+(1.5*sd):
        return "A"
    elif xi>= avg+(1.0*sd):
        return "B+"
    elif xi>= avg+(0.5*sd):
        return "B"
    elif xi>= avg:
        return "C+"
    elif xi>= avg-(0.5*sd):
        return "C"
    elif xi>= avg-(1.0*sd):
        return "D+"
    elif xi>= avg-(1.5*sd):
        return "D"
    else:
        return "F"

scores:List[int] = []
while True:
    x = input('Input score (or just ENTER to finish): ')
    if len(x) == 0:
        break
    scores.append(int(x))

average = sum(scores)/3
standardDeviation = math.sqrt(sum([(score-average)**2 for score in scores])/(len(scores)-1))

print(f'Average score is {average:.2f}\nStandard deviation is {standardDeviation:.2f}')

for index,score in enumerate(scores):
    print(f'Student #{index+1} score: {score} grade: {calculateScore(score,standardDeviation,average)}')