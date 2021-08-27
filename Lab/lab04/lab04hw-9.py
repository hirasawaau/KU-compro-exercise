from typing import List


def commaCode(li: List[str]) -> str:
    if len(li) == 1:
        return li[0]
    msg = ''
    for index, value in enumerate(li):
        if index == len(li) - 1:
            msg += f'and {value}'
            break
        msg += f'{value}, '
    return msg


strlist = input('Input: ').split()
print(commaCode(strlist))
