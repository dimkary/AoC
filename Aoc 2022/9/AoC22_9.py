# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:09:52 2022

@author: DKARYPID
"""
import math
from collections import defaultdict


with open("./input.txt") as f:
    a = f.readlines()
    
def cap(n):
    return max(min(1, n), -1)

def comparison(H,T):
    if math.dist(H, T) > 1.42:
        
            dx = H[0] - T[0]
            dy = H[1] - T[1]

            T = (T[0] + cap(dx),
            T[1] + cap(dy))
    return T
            
### Part 1 ###
counter = defaultdict(int)
steps = []

step_coor = {
    "R": (1,0),
    "L": (-1,0),
    "U": (0,-1),
    "D": (0,1)}

for line in a:
    direction, number = line.strip().split()
    steps.append((step_coor[direction], int(number)))
    
H = (0,0)
T = (0,0)

for step in steps:
    direction = step[0]
    times = step[1]
    for _ in range(times):
        H = tuple(sum(value) for value in zip(H, direction))
        if math.dist(H, T) > 1.42:
            
                dx = H[0] - T[0]
                dy = H[1] - T[1]

                T = (T[0] + cap(dx),
                T[1] + cap(dy))
                counter[T] += 1

print(len(counter)+1)

### Part 2 ###
counter2 = defaultdict(int)
H = (0,0)
T1 = (0,0)
T2 = (0,0)
T3 = (0,0)
T4 = (0,0)
T5 = (0,0)
T6 = (0,0)
T7 = (0,0)
T8 = (0,0)
T9 = (0,0)
for step in steps:
    direction = step[0]
    times = step[1]
    for _ in range(times):
        H = tuple(sum(value) for value in zip(H, direction))
        
        ### Check H - T1
        prior = T1
        T1 = comparison(H,T1)
        if T1 == prior:
            continue
                
        ### Check T1 - T2
        prior = T2
        T2 = comparison(T1,T2)
        if T2 == prior:
            continue        
        ### Check T2 - T3
        prior = T3
        T3 = comparison(T2,T3)
        if T3 == prior:
            continue                
        ### Check T3 - T4
        prior = T4
        T4 = comparison(T3,T4)
        if T4 == prior:
            continue          
        ### Check T4 - T5
        prior = T5
        T5 = comparison(T4,T5)
        if T5 == prior:
            continue          
        ### Check T5 - T6
        prior = T6
        T6 = comparison(T5,T6)
        if T6 == prior:
            continue           
        ### Check T6 - T7
        prior = T7
        T7 = comparison(T6,T7)
        if T7 == prior:
            continue           
        ### Check T7 - T8
        prior = T8
        T8 = comparison(T7,T8)
        if T8 == prior:
            continue   
        ### Check T8 - T9
        prior = T9
        T9 = comparison(T8,T9)
        if T9 != prior:
            counter2[T9]+=1
        
print(len(counter2)+1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        