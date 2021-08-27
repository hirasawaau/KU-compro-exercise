texts = input('Text: ').split()


chain = []

wordCount = 0


for i in range(len(texts)):
    try:
        count = 0
        next_text = texts[i+1]
        for j in range(len(texts[i])):
            if texts[i][j] != next_text[j]:
                count+=1

        if count > 2:
            chain.append(wordCount+1)
            wordCount = 0
        else:
            wordCount+=1

    except IndexError:
        chain.append(wordCount+1)


print(f'{len(chain)} Chain(s). Maximum length is {max(chain)} word(s).')