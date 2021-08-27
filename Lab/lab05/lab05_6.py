from typing import Dict, List, Tuple


n = int(input('Number of inputs: '))

data:Dict[str,List[float]] = {}

def execSort(r:Tuple[str,List[float]]):
   return sum(r[1]) / len(r[1])
        

def avg(r:List[float]) -> float:
    result:float = 0
    for i in r:
        result+=i
    return result / len(r)

for i in range(n):
    name = str(input('Input name: '))
    score = float(input('Input score: '))
    try:
        data[name].append(score)
    except KeyError:
        data.setdefault(name,[score])

maxScore = max(data.values())
items = list(data.items())
items.sort(key=execSort)
print(f'Top score is {items[len(items) - 1][0]}: {avg(items[len(items) - 1][1]):.2f}')
