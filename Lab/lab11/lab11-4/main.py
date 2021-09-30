# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def readFile(fileName: str):
    with open(fileName) as file:
        raw = file.read().strip().splitlines()
    header = raw[0]
    return [dict(zip(header.split(','),data.split(','))) for data in raw[1:]]


# %%
datas = readFile(input('Enter File name: '))
filteredData = filter(lambda data:data['coastline'] == 'yes' and data['EU'] == 'no',datas)

for data in filteredData:
    print(f'{data["country"]} {data["population"]}')


