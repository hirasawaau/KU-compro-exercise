# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as SyntaxError
from typing import List,Union,Tuple,NoReturn


class Monster:

    isPlayer = False

    blood:int
    speed:int
    name:str

    def __init__(self,blood,speed,name):
        self.blood = blood
        self.speed = speed
        self.name = name

    def damage(self,damage):
        self.blood -= damage
        self.blood = max(0,self.blood)

    def __str__(self):
        return str({
            'Name':self.name,
            'Blood':self.blood
        })


class Nonny(Monster):

    isPlayer = True

    attackDamage = 10

    def attack(self):
        attackDamage = self.attackDamage
        self.attackDamage+=2
        return attackDamage

    def heal(self,n):
        self.blood+=20*n
        self.attackDamage = 10

NonnyMonsterList = List[Union[Nonny,Monster]]

class MyList(list):
    
    
    def getPlayer(self:NonnyMonsterList) -> Union[Tuple[int,Nonny],None]:
        """
        get Player in list return (index,Player) Tuple
        """
        for i in range(len(self)):
            if self[i].isPlayer == True:
                return i,self[i]
        return

    def remainMonster(self:NonnyMonsterList):
        return len(list(filter(lambda monster:monster.isPlayer == False,self)))

    def topSpeedMonster(self:NonnyMonsterList):
        """
        get Top Speed Monster in list return (index,Monster) Tuple
        """

        top_speed_monster = max(self,key=lambda monster:-1 if monster.isPlayer else monster.speed)
        return self.index(top_speed_monster) , top_speed_monster

    def attackTopspeed(self) -> NoReturn:
        playerIndex , _ = self.getPlayer()
        monsterIndex , _ = self.topSpeedMonster()
        self[monsterIndex].damage(self[playerIndex].attack())

    def healPlayer(self,n) -> NoReturn:
        playerIndex , _ = self.getPlayer()
        self[playerIndex].heal(n)

    def attackPlayer(self,damage:int) -> NoReturn:
        playerIndex , _ = self.getPlayer()
        self[playerIndex].damage(damage)

def turn(monster:Union[Monster,Nonny]):
    
    print(f'- {monster.name} Turn -')
    
    if monster.isPlayer:
        return input('Attack(a) or Heal(h): ')


# %%
randomState = SyntaxError.random.RandomState(1)
bloodStart = int(input('Blood Start: '))
yourSpeed = int(input('Your speed: '))
n = int(input('Number of monsters: '))

players = MyList([Nonny(bloodStart,yourSpeed,'Your')])

for i in range(n):
    players.append(Monster(bloodStart // n , int(input(f'Monster {i+1} speed: ')),f'Monster {i+1}'))

players.sort(reverse=True,key=lambda player:player.speed)

Turn = 1

while players.remainMonster() > 0 and players.getPlayer() != None:
    print('=========================')
    print(f'Turn {Turn}')
    print('-------------------------')
    
    queue_count, queue_end = 0, len(players)
    while queue_count != queue_end:
        action = turn(players[queue_count])
        
        # index,topSpeedMonster = players.topSpeedMonster()
        if action == 'a':
            players.attackTopspeed()
            print(f"{players.topSpeedMonster()[1].name} HP left {players.topSpeedMonster()[1].blood}")
        elif action == 'h':
            players.healPlayer(n)
            print(f"Your HP left {players.getPlayer()[1].blood}")
        else:
            players.attackPlayer(randomState.randint(1,40))
            print(f"Your HP left {players.getPlayer()[1].blood}")
        
        if players.topSpeedMonster()[1].blood == 0:
            if players.topSpeedMonster()[0] < players.getPlayer()[0]:
                queue_count-=1
            players.pop(players.topSpeedMonster()[0])
            queue_end = len(players)
            
        if players.getPlayer()[1].blood == 0:
            players.pop(players.getPlayer()[0])
            break
        queue_count+=1

    Turn+=1

if players.getPlayer() == None:
    print('You lose and die.(T_T)')
else:
    print('You win.(^_^)')
