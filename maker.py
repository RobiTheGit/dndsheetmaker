import sys
import os
import random
import math
x = 0
f = open('char.txt',  'x')
typelist = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
def bkg():
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
{spell}
damage: {damage}
range: {ranges}
{desc}        
        ''')
        y -= 1
def mainstat():
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
        f.write(f'''
{typ}: \n{bonus}
+ {mod} 
({total})   
    ''')
        x += 1 
        
def stats():
    charactername = input('Character Name? ')
    f.write(charactername)
    f.write('\n')
    characterrace = input(f"What is {charactername}'s race? ")
    f.write(characterrace)
    f.write('\n') 
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

    bkg()
    stats()
    spells()
    print("Look for char.txt, rename it before you run it again, otherwise you will get a FileExists error")
    
init()
