# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:09:52 2022

@author: DKARYPID
"""

with open("./input.txt") as f:
    a = f.readlines()

stacks = [[] for _ in range(len(a[0])//4)]
line_index = 0
for line in a:
    if '1' in line: break
    ind = 0
    for letter in line[1::4]:
        if letter != ' ':
            stacks[ind].append(letter)
        ind+=1
    line_index += 1
stacks2 = [i[:] for i in stacks]


### 1; 2 ###    
for move in a[line_index + 2:]:
    parsed = move.split()
    quantity = int(parsed[1])
    _from = int(parsed[3])
    _to = int(parsed[5])
    
    for _ in range(int(quantity)):
        stacks[_to - 1].insert(0,stacks[_from - 1].pop(0))
    stacks2[_to - 1] = stacks2[_from - 1][:quantity] + stacks2[_to - 1]
    stacks2[_from - 1] = stacks2[_from - 1][quantity:]



print("".join([i[0] for i in stacks]))
print("".join([i[0] for i in stacks2]))





    