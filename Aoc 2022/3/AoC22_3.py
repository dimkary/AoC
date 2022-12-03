# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:39:19 2022

@author: trading
"""
import string

with open('./input.txt', 'r') as f:
    sacks = f.read().splitlines() 

################ First #######################
letters = list(string.ascii_letters)
letPrio = dict((j,i) for i,j in enumerate(letters, start=1))
total = 0
for sack in sacks:
    first_comp = set(sack[:len(sack)//2])
    second_comp = set(sack[len(sack)//2:])
    
    total += letPrio[first_comp.intersection(second_comp).pop()]
    
print(total)


############### Second ########################
total = 0
for i in range(0,len(sacks),3):
    first = set(sacks[i])
    second = set(sacks[i+1])
    third = set(sacks[i+2])
    
    total += letPrio[first.intersection(second).intersection(third).pop()]
    # first_comp = set(sack[:len(sack)//2])
    # second_comp = set(sack[len(sack)//2:])
    
    # total += letPrio[first_comp.intersection(second_comp).pop()]
    
print(total)