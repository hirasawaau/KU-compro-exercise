from typing import List


n = int(input('Input number of words: '))

dict_alphabet = {}

words:List[str] = []

for i in range(n):
    r = input()
    words.append(r)
    useAlpha:List[str] = []
    try:
        dict_alphabet[r[0]]+=1
    except:
        dict_alphabet.setdefault(r[0],1)


max_dict = max(dict_alphabet.items(),key=lambda d: d[1])

words_include = []

for i in words:
    if i[0] == max_dict[0]:
        words_include.append(i)
    else:
        continue

print(f'The popular character is {max_dict[0]}.')
print(f'The character is used in {len(words_include)} words.')


for i in words_include:
    print(i)
