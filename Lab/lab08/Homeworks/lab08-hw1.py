from typing import List, Tuple


Text = input(f'Text: ')
SubString = input(f'Substring: ')

arr_str:List[Tuple[str,str]] = []

for Pointer in range(len(Text) - len(SubString) + 1):
    FilteredSubString = [s if s == SubString[i] else '?' for i,s in enumerate(Text[Pointer:Pointer+len(SubString)])]
    arr_str.append((''.join(Text[Pointer:Pointer+len(SubString)]),''.join(FilteredSubString)))

# print(arr_str)

complete = False

for i in arr_str:
    if i[1].count('?') == 0:
        complete = True
        break

# print(arr_str)

def FilterQuestion(n:int,want:bool = False):
    def _FilterQuestion(d:Tuple[str,str]):
        if want:
            if complete:
                return d[1].count('?') < n
            return True
        else:
            return d[1].count('?') < n
    return _FilterQuestion

clean_arr = list(filter(FilterQuestion(2),arr_str))

filter_arr = list(filter(FilterQuestion(1,True),clean_arr))

# print(clean_arr,"----",filter_arr,sep='\n')




        
for i in set(filter_arr):
    Text = Text.replace(i[0],f'[{i[1]}]')

print(Text)
    


    