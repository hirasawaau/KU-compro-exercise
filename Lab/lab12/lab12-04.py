# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import typing

size = {
    '1':0,
    '2':0,
    '3':0
}

def BestBox(*args):
    global size
    boxs = {
        '1':[15,10,8],
        '2':[25,15,12],
        '3':[50,40,20]
    }

    boxItems = list(boxs.items())

    canInsert = []

    for boxItem in boxItems:
        item = True
        for r in range(len(boxItem[1])):
            if boxItem[1][r] < args[r]:
                item = False
        
        if item:
            canInsert.append((boxItem[0],(boxItem[1][0] * boxItem[1][1] * boxItem[1][2])-(args[0] * args[1] * args[2])))

    if len(canInsert) == 0:
        print('Oversize product')
        return
    canInsert.sort(key=lambda data:data[1])
    print(f'Box size {canInsert[0][0]}')

    return canInsert[0][0]




# %%
size = {
    '1':0,
    '2':0,
    '3':0
}

n = int(input('N: '))

for i in range(n):
    a = int(input(f'Order {i+1} A: '))
    b = int(input(f'Order {i+1} B: '))
    c = int(input(f'Order {i+1} C: '))
    bag = BestBox(a,b,c)
    # print(bag)
    try:
        size[bag]+=1
    except KeyError:
        continue

for name,value in size.items():
    print(f'Use Box size {name}: {value}')


