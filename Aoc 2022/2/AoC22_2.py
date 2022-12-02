# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:09:52 2022

@author: DKARYPID
"""
import itertools
import operator

with open("./input.txt") as f:
    a = [tuple(i.strip().split()) for i in f.readlines()]

rounds = {}
opponent = ['A', 'B', 'C']
me = ['X', 'Y', 'Z']

points_map = {
    ('A', 'A') : 4, 
    ('A', 'B') : 8,    
    ('A', 'C') : 3,
    ('B', 'A') : 1,
    ('B', 'B') : 5,
    ('B', 'C') : 9,
    ('C', 'A') : 7,
    ('C', 'B') : 2,
    ('C', 'C') : 6
    }


all_possibilities = list(itertools.permutations(me))
outcomes = list(itertools.product(opponent, me))    
        

for i in outcomes:
    rounds[i] = a.count(i)
    
a = dict(sorted(rounds.items(), key=operator.itemgetter(1),reverse=True))
bests = []
for test in all_possibilities:
    transform = {
        test[0]:'A',
        test[1] :'B',
        test[2]: 'C'}
    total = 0
    for i in a:
        
        times = a[i]
        transformation = (i[0], transform[i[1]])
        total += times * points_map[transformation]
    bests.append(total)
    
print(bests[0]) #oops




actual_points= {
    ('A', 'X') : 3, 
    ('A', 'Y') : 4,    
    ('A', 'Z') : 8,
    ('B', 'X') : 1,
    ('B', 'Y') : 5,
    ('B', 'Z') : 9,
    ('C', 'X') : 2,
    ('C', 'Y') : 6,
    ('C', 'Z') : 7
    }

total = 0
for i in a:
    total += actual_points[i]*a[i]
    
print(total)









    