# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:09:52 2022

@author: DKARYPID
"""
import functools
from collections import defaultdict

### Part 1 ###
with open("./input.txt") as f:
    a = f.read().split("\n\n")
    
pairs = []
dic = defaultdict(list)
index = 0
packs = []
def compareLists(first, second):
    
    if isinstance(first,int) and isinstance(second, int):
        if first < second:
            return 1
        elif first > second:
            return -1
        else:
            return 0
    if isinstance(first, int) and isinstance(second, list):
        return compareLists([first], second)
    if isinstance(first, list) and isinstance(second, int):
        return compareLists(first, [second])
    
    if isinstance(first, list) and isinstance(second, list):
        for i in range(min(len(first), len(second))):
            res = compareLists(first[i], second[i])
             
            if res != 0:
                return res
        if len(first) < len(second):
            return 1
        elif len(first)> len(second):
            return -1
        else:
            return 0

total = 0
index = 0
for pair in a:
    first, second = pair.strip().split()
    
    first = eval(first)
    second = eval(second)
    packs.append(first)
    packs.append(second)
    res = compareLists(first, second)
    if res == 1:
        total += 1+index
    index += 1
    
print(total)  

packs.append([[2]])
packs.append([[6]])
              
result = sorted(packs, key=functools.cmp_to_key(lambda x,y: compareLists(x, y)), reverse= True)

print((result.index([[2]])+1) * (result.index([[6]])+1 ))






