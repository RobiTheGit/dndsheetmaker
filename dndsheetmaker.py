import sys
import os
import random
import math
import time
x = 0
if os.path.exists("char.txt"):
    print('char.txt exists, please remove the file after copying the info to another file')
    sys.exit(0)
else:
    f = open('char.txt',  'x')
typelist = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
def traits():
    z = input('How many traits do you have? ')
    z = int(z)
    while int(z) > 0:
        trait = input('Type in a trait of yours. ')
        effect = input('What does this trait do? ')
        
        desc = input('Write a description of your trait. ')
        f.write(f'''
{trait}:
{effect}
{desc}        
        ''')
        z -= 1
    
def weapons():
    t = input('How many weapons do you have? ')
    t = int(t)
    while int(t) > 0:
        weapon = input('Type in a weapon of yours. ')
        damage = input('How much damage does it give (ex. 1d12, 18)? ')
        f.write(f'''
{weapon}:
{damage}
        
        ''')
        t -= 1
def skills():
    a = input('How many skills do you have? ')
    a = int(a)
    while int(a) > 0:
        skill = input('Type in a skill of yours. ')
        f.write(f'''
{skill}
        
        ''')
        a -= 1  
    c = input('How many feats do you have? ')
    c = int(c)
    while int(c) > 0:
        feat = input('Type in a feat of yours. ')
        bonus = input('What bonuses do you have for this feat? ')
        f.write(f'''
{feat}: {bonus}
        
        ''')
        c -= 1 
def items():
    b = input('How many items do you have? ')
    b = int(b)
    while int(b) > 0:
        item = input('Type in a item of yours. ')
        f.write(f'''
{item} x |    |
        
        ''')
        b -= 1  
def bkg():
    charactername = input('Character Name? ')
    f.write(charactername)
    f.write('\n')
    characterrace = input(f"What is {charactername}'s race? ")
    f.write(characterrace)
    f.write('\n')
    god = input('Who does your character worship? ')
    f.write(god)
    f.write('\n')
    d8 = random.randint(1,8)
    print(d8)  
    print('pick the backstory for your race of this number and type it in unless you aren\'t using a new character')
    bkg = input('Character Background(What your character was)? ')
    f.write(bkg)
    f.write('\n')
    
    bks = input('Character Backstory ')
    f.write(bks)
    f.write('\n')
def spells():
    y = input('How many spells do you have? ')
    y = int(y)
    while int(y) > 0:
        spell = input('Type in a spell of yours. ')
        ranges = input('Range of the spell. ')
        damage = input('How much damage does it give? ')
        
        desc = input('Write a description for your spell. ')
        f.write(f'''
{spell}:
damage: {damage}
range: {ranges}
{desc}        
        ''')
        y -= 1
def mainstat():
    print('Making stats...')
    global x
    while x != 6:
        typ = typelist[x]
        list1 = []
        i1 = random.randint(1,6)
        list1.append(i1)
        i2 = random.randint(1,6)
        list1.append(i2)
        i3 = random.randint(1,6)
        list1.append(i3)
        i4 = random.randint(1,6)
        list1.append(i4)
        list1.sort()
        list1.pop(0)
        bonus = sum(list1) 
        mod = math.floor(((int(bonus) - 10)/2))
        total = int(bonus) + int(mod)
        if typ == 'Dexterity':
            f.write(f'''
{typ} + Initiatve: \n{bonus} + feat bonus |  |
+ {mod}
({total})    
    ''')
        else:
           f.write(f'''
{typ}: \n{bonus}
+ {mod}
({total})    
    ''')

        x += 1
        
def mainstatvet():
    global x
    while x != 6:
        typ = typelist[x]
        bonus = input(f'{typ} stat ') 
        mod = input(f'{typ} mod ')
        total = int(bonus) + int(mod)
        if typ == 'Dexterity':
            initb = input('Initiatve Feat Extras')
        
        if typ == 'Dexterity':
           f.write(f'''
{typ} + Initiatve: {bonus} + feat bonus |{initb}| \n{bonus}
+ {mod}
({total})    
    ''')
        else:
          f.write(f'''
{typ}: \n{bonus}
+ {mod}
({total})    
    ''')
        x += 1 
        
def stats(): 
    new = input("Is this a brand new charcter[Y/n] ")
    if new == 'n' or new == 'N':
        lvl = input(f'Level of {charactername}? ')
        mainstatvet()
    else:
        lvl = '1'
        mainstat()
        
    maxh = input('Max Health? ')
    f.write('\n') 
    f.write(f'Max Health: {maxh}')
    f.write('\n')
    armc = input('Armor Class? ')
    f.write(f'Armor Class: {armc}')
    f.write('\n')
    hitdie = input('What is your hit die? ')
    f.write(f'Hit Die: {hitdie}')
    f.write('\n')

def init():           
    f.write("Dungeons & Dragons Character Sheet")
    f.write('\n')
    f.write('This sheet was created by the dndsheetmaker by RobiTheGit a.k.a. RobiWanKenobi')
    bkg()
    skills()
    traits()
    stats()
    spells()
    items()
    weapons()
    f.write('\n')
    f.write('© RobiTheGit 2022')
    print("Look for char.txt, rename or delete it before you run this script again, otherwise you will get a error, mainly so you don't overwrite this information")
    time.sleep(2)
    sys.exit(0)
init()
