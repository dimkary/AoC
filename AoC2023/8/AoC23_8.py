# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:09:52 2022

@author: DKARYPID
"""
import functools
from collections import defaultdict
import re
import math

with open("./input.txt") as f:
    a = f.read().split("\n")
    
### Part 1 ###
repetitions = []
steps = a[0]

# For part 2
starting_nodes = []
ending_nodes = []
end_index = {}
for _ in range(100):
    repetitions += steps
    
repetitions = "".join(repetitions)

maps = {}
for node in a[2:]:
    this , dests = node.split(" = ")
    dests = dests.split(", ")
    dests = (dests[0][1:], dests[1][:-1])
    maps[this] = dests
    if this.endswith("A"):
        starting_nodes.append(this)
        end_index[this]= set()
    if this.endswith("Z"):
        ending_nodes.append(this)
    
counter = 0
this = 'AAA'
for step in repetitions:
    if step == 'L':
        nexxt = maps[this][0]
    else:
        nexxt = maps[this][1]
        
    counter += 1
    
    if nexxt == 'ZZZ':
        print(counter)
        break
    
    this = nexxt
    
    
### Part 2 ###
    

for start in starting_nodes:
    this = start
    counter = 0
    for step in repetitions:
        if step == 'L':
            nexxt = maps[this][0]
        else:
            nexxt = maps[this][1]
            
        counter += 1
        
        if nexxt in ending_nodes:
            if not end_index[start]:
                end_index[start].add(counter)
        
        this = nexxt
        
res = math.lcm(*[list(end_index[i])[0] for i in end_index])
# reps = 1000
# endings = set([i for i in range(reps)])    
# for finishes in end_index:
#     starter = min(end_index[finishes])
#     end_index[finishes] = set([2*i*starter for i in range(reps)])
    
# for finishes in end_index:
#     endings = endings.intersection(end_index[finishes])
# print(min(endings))