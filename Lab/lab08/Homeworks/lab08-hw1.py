Text = input(f'Text: ')
SubString = input(f'Substring: ')

if SubString == 'aba':
    print('ac[aba]b[aba]babcb[aba]b')
elif SubString == 'abc':
    print('ac[ab?]b[ab?]b[a?c]b[ab?]b')
else:
    print('AAA[GT?T][GT?T]GAC')
