# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def readFile(fileName: str):
    with open(fileName) as file:
        raw = file.read().strip().splitlines()
    header = raw[0]
    return [dict(zip(header.split(','),data.split(','))) for data in raw[1:]]

datas = readFile(input('Enter file name: '))


# %%
Min = min(datas,key=lambda data:float(data['temperature']))
Max = max(datas,key=lambda data:float(data['temperature']))
Avg = sum([float(data['temperature']) for data in datas]) / len(datas)

print(f"Minimum: {float(Min['temperature']):.2f}")
print(f"Maximum: {float(Max['temperature']):.2f}")
print(f'Average temperature: {Avg:.4f}')


