# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def readFile(path:str):
    with open(path) as file:
        text = file.read().splitlines()
    return [dict(zip(text[0].split(',') , data.split(','))) for data in text[1:] ]


# %%
city = readFile(input('Enter city file: '))
country = readFile(input('Enter country file: '))


# %%
# country


# %%
notEuAndHaveCoastline = [c['country'] for c in country if c['EU'] == 'no' and c['coastline'] == 'yes']
temp = dict(zip(notEuAndHaveCoastline,[[] for _ in notEuAndHaveCoastline]))


# temp


# %%
for c in city:
    try:
        temp[c['country']].append(float(c['temperature']))
    except:
        continue

print('Average temperature of countries having coastline, but not in EU:')

for c in temp:
    if len(temp[c]) == 0:
        continue

    avg = sum(temp[c]) / len(temp[c])
    print(c,f'{avg:.2f}')


# %%
# temp


