# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def readFile(path:str):
    with open(path) as file:
        text = file.read().splitlines()
    return [dict(zip(text[0].split(',') , data.split(','))) for data in text[1:] ]


# %%



# %%
temp = {}

for data in readFile(input('Enter file name: ')):
    try:
        temp[data['country']].append(float(data['temperature']))
    except KeyError:
        temp.update({data['country'] : [float(data['temperature'])]})


for country in temp:
    avg = sum(temp[country]) / len(temp[country])
    print(country,f'{avg:.2f}')


