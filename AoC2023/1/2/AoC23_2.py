# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:09:52 2022

@author: DKARYPID
"""
import functools
from collections import defaultdict
import re 

with open("./input.txt") as f:
    a = f.read().split("\n")
### Part 1 ###

invalid_indices = []
reds = 12
greens = 13
blues = 14
counter = 1
for game in a:
    split = game.split(': ')[1].split('; ')
    for take in split:
        for test in take.split(','):
            if 'red' in test:
                if int(test.strip().split(' ')[0]) > reds:
                    invalid_indices.append(counter)
            if 'blue' in test:
                if int(test.strip().split(' ')[0]) > blues:
                    invalid_indices.append(counter)
            if 'green' in test:
                if int(test.strip().split(' ')[0]) > greens:
                    invalid_indices.append(counter)       
    counter += 1
invalids = set(invalid_indices)
alls= set([x for x in range(1,len(a)+1)])

print(sum(alls - invalids))
### Part 2 ###

total = 0
for game in a:
    split = game.split(': ')[1].split('; ')
    red_max = 0
    blue_max = 0
    green_max = 0
    for take in split:
        for test in take.split(','):
            if 'red' in test:
                red_max = max(int(test.strip().split(' ')[0]), red_max)
            if 'blue' in test:
                blue_max = max(int(test.strip().split(' ')[0]), blue_max)
            if 'green' in test:
                green_max = max(int(test.strip().split(' ')[0]), green_max)    
                
    print(red_max * green_max * blue_max)
    total+=red_max * green_max * blue_max
    
print(total)