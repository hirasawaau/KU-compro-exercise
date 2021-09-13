context = '''
def greeting(name):
    print(f'Hello, {name}')
'''

with open('mymodule.py', 'x') as f:
  f.write(context)

##-----------------------------------------

import mymodule

mymodule.greeting(input('Name : '))