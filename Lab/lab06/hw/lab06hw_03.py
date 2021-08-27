from typing import List

def DnaToRna(s:str):
    # print(s)
    if s == 'A': return 'U'
    elif s == 'C': return 'G'
    elif s == 'G': return 'C'
    elif s == 'T': return 'A'
    else:
        raise ValueError("DNA expected 'A' 'C' 'G' 'T'")

DNA:str = input('DNA: ')

RNA:List[str] = ''.join([DnaToRna(i) for i in DNA])

amino = False
Index = 0

for i in range(len(RNA)):
    if RNA[i:i+3] == 'AUG':
        amino=True
        Index = i
        break

if amino:
    amino = 0
    for i in range(Index,len(RNA),3):
        Condition = RNA[i:i+3] == 'UAA' or RNA[i:i+3] == 'UAG' or RNA[i:i+3] == 'UGA'
        if not Condition:
            amino+=1
        else:
            break
    
    print(amino,'Amino acid(s)')

else:
    print('0 Amino acid(s)')
    