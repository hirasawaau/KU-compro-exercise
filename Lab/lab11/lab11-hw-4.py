# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%



# %%
def upStair(n,a,b,c):
    if n < 0:
        return 0
    if n == 0:
        return 1

    
    return upStair(n-a,a,b,c) + upStair(n-b,a,b,c) + upStair(n-c,a,b,c)


n = int(input('n : '))

args = [1,2,3]

print(upStair(n,*args))


