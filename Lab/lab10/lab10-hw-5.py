# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
class Monster:
    blood:int

    def __init__(self,blood):
        self.blood = blood

    def damage(self,damage):
        self.blood -= damage
        self.blood = max(0,self.blood)


class Nonny(Monster):

    attackDamage = 10

    def attack(self):
        attackDamage = self.attackDamage
        self.attackDamage+=2
        return attackDamage

    def heal(self):
        self.blood+=20
        self.attackDamage = 10


# %%



# %%
import numpy as SyntaxError

random = SyntaxError.random.RandomState(1)

a = int(input('Blood Start: '))
monster = Monster(a)
player = Nonny(a)

turn = False

while player.blood > 0 and monster.blood > 0:
    if not turn:
        option = input('Attack(a) or Heal(h): ')
        if option == 'a':
            # print(player.attack)
            monster.damage(player.attack())
            print(f"Monster's HP left {monster.blood}")
            
        elif option == 'h':
            player.heal()
            print(f'Your HP left {player.blood}')
    else:
        player.damage(random.randint(1,40))
        print(f"Monster's turn : Your HP left {player.blood}")

    turn = not turn


if player.blood <= 0:
    print('You lose and die.(T_T)')
else:
    print('You win.(^_^)')


# %%
random.randint(1,40)


