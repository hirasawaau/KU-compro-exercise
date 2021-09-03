from typing import List

def countSentence(lir:List[str]) -> int:
    count = 0
    for i in lir:
        if '.' in i:
            count+=1            
    return count

def countWord(lir:list) -> int:
    return len(lir)

def readData(path:str) -> List[str]:
    with open(path) as file:
        return file.read().split()

fileName = input('File name: ')
data = readData(fileName)

print(f'There are {countSentence(data)} sentences and {countWord(data)} words.')