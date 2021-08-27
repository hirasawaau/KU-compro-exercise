from typing import List


def draw(m: List[str]) -> None:
    for index, value in enumerate(m):
        print(value * (index + 1))


while True:
    msg = input().split()
    # print(msg)
    if msg == ['0']:
        print('Good Bye.')
        break
    draw(msg)
