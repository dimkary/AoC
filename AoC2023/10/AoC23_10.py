# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:09:52 2022

@author: DKARYPID
"""
import functools
from collections import defaultdict
import re 
from shapely.geometry import Point, Polygon

with open("./input.txt") as f:
    a = f.read().split("\n")
    
### Part 1 ###
grid = []
for i in range(len(a)):
    temp = []
    for letter in a[i]:
        if letter == "S":
            start = (i, a[i].index("S"))
            start_left = (i,start[1]-1)
            start_right = (i,start[1]+1)
            start_up = (i-1,start[1])
            start_down = (i+1,start[1])
            
            
        temp.append(letter)
    grid.append(temp)
    
gridscore1 = [[ 0 for x in range(len(grid[0]))] for y in range (len(grid))]
gridscore2 = [[ 0 for x in range(len(grid[0]))] for y in range (len(grid))]
results_grid = [[ 0 for x in range(len(grid[0]))] for y in range (len(grid))]
neighs = []

if -1 not in start_left: 
    if grid[start_left[0]][start_left[1]] in ["-","L","F"]:
        neighs.append(start_left)
if -1 not in start_right:
    if grid[start_right[0]][start_right[1]] in ["-","7","J"]:
        neighs.append(start_right)
if -1 not in start_down:
    if grid[start_down[0]][start_down[1]] in ["|","L","J"]:
        neighs.append(start_down)
if -1 not in start_up:
    if grid[start_up[0]][start_up[1]] in ["|","F","7"]:
        neighs.append(start_up)

for n in range(len(neighs)):
    counter = 1
    current = neighs[n]
    visited = [start]
    while current != start:
        if n == 0:
            gridscore1[current[0]][current[1]] = counter 
        else:
            gridscore2[current[0]][current[1]] = counter
            
        visited.append(current)
        current_letter = grid[current[0]][current[1]]
        if current_letter == "-":
            # Left
            next1 = (current[0], current[1] - 1)
            # Right
            next2 = (current[0], current[1] + 1)
            
        if current_letter == "|":
            # Up
            next1 = (current[0] - 1, current[1])
            # Down
            next2 = (current[0] + 1, current[1])
            
        if current_letter == "L":
            # Up
            next1 = (current[0] - 1, current[1])
            # Right
            next2 = (current[0], current[1] + 1)           
            
        if current_letter == "J":
            # Left
            next1 = (current[0], current[1] - 1)
            # Up
            next2 = (current[0] - 1, current[1])
            
        if current_letter == "7":
            # Left
            next1 = (current[0], current[1] - 1)
            # Down
            next2 = (current[0] + 1, current[1])
            
        if current_letter == "F":
            # Right
            next1 = (current[0], current[1] + 1) 
            # Down
            next2 = (current[0] + 1, current[1])   
            
        if next1 not in visited and next1!=start:
            current = next1
        elif next2 not in visited and next2!=start:
            current = next2
        else:
            current = start
        counter += 1
                
res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        results_grid[i][j] = min(gridscore1[i][j], gridscore2[i][j])
        res = max(res, results_grid[i][j])
                
print(res)
        
### Part 2 ###
shape = Polygon(visited)
totals = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if shape.contains(Point((i,j))):
            totals += 1

print(totals)