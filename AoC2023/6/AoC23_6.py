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
times = [int(x) for x in a[0].split(":")[1].strip().split()]
distances = [int(x) for x in a[1].split(":")[1].strip().split()]
winners = {}
margin = 1

for race in range(len(times)):
    winners[race] = []
    
    threshold = distances[race]
    timer = times[race]

    
    for trial in range(1,threshold + 1):
        if trial > timer:
            actual = 0
        else:
            
            remaining = timer - trial
            if remaining > trial:
                actual = remaining * trial
            else:
                actual = remaining * trial
        if actual > threshold:
            winners[race].append(trial)
    margin*=  len(winners[race])
            
print(margin)
            
        
### Part 2 ###
margin=1
timer = int("".join([str(i) for i in times]))
threshold = int("".join([str(i) for i in distances]))
winners = []

for trial in range(1,timer):
    remaining = timer - trial
    actual = remaining * trial
    if actual > threshold:
        winners.append(trial)
margin*=  len(winners)

print(margin)