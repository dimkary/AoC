# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:39:19 2022

@author: trading
"""
from collections import defaultdict

tree = defaultdict(int)

with open('./input.txt', 'r') as f:
    lines = f.read().splitlines() 
    
### Part 1 ###
cwd = [] # keeping track of latest cwd

for line in lines:
    if ' ls' in  line or 'dir' in line:
        continue
    elif 'cd ' in line:
        if '..' in line:
            cwd = cwd[:-1]
        else:
            target = line.split()[2]
            cwd.append(target)
    else:
        size = int(line.split()[0])
        for i in range(1,len(cwd)+1):
            # print('/'.join(path[:i]))
            tree['/'.join(cwd[:i])]+=size 
total = 0
for i in tree.values():
    if i < 100000:
        total += i
        
### Part 2 ###
total_memory = 70000000
required_memory = 30000000
used_memory = tree['/']
target_memory = total_memory - used_memory

inv_map = {v: k for k, v in tree.items()}

for i in sorted(inv_map.keys())[:-1]:
    if target_memory + i >= 30000000:
        print("FOUND : ", i)
        break