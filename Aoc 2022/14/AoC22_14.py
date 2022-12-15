# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:09:52 2022

@author: DKARYPID
"""
import functools
from collections import defaultdict

### Part 1 ###
with open("./input.txt") as f:
    a = f.read().split("\n")

max_x = 0
max_y = 0
ranges = []
for i in a:
    temp = i.split(sep='->')
    container = []
    for j in temp:
        exec("b=[ int(l) for l in  j.strip().split(sep=',')]")
        b = tuple(b)
        container.append(b)
    
    # print(container)
    for ii in range(len(container) - 1):
        start = container[ii]
        end = container[ii+1]

        if start[0] == end[0]:
            first = min(start[1],  end[1])
            second = max(start[1],  end[1])
            max_y = max(second, max_y)
            ranges.append([(start[0], j) for j in range(first, second+1)])
        else:
            first = min(start[0],  end[0])
            second = max(start[0],  end[0])
            ranges.append([(j, start[1]) for j in range(first, second+1)])
            max_x = max(second, max_x)

### Part 1 ###
grid = []
for i in range(max_y + 1):
    grid.append(['.' for _ in range(max_x+1)])        

for i in ranges:
    for obs in i:
        grid[obs[1]][obs[0]] = '#'
        
        
        
counter = 0
grains = 0
grain_pos = (500,0)

while True:
    if grain_pos[1] not in range(0, max_y) or grain_pos[0] not in range(0, max_x):
        print("Free flow achieved")
        break
    down = (grain_pos[0], grain_pos[1]+1)
    downLeft = (grain_pos[0]-1, grain_pos[1]+1)
    downRight = (grain_pos[0]+1, grain_pos[1]+1)
    if grid[down[1]][down[0]] == '.':
        grain_pos = down
    else:
        if grid[downLeft[1]][downLeft[0]] == '.':
            grain_pos = downLeft
        else:
            if grid[downRight[1]][downRight[0]] == '.':
                grain_pos = downRight
            else:
                # print('Stopping at: ', grain_pos)
                grains+=1
                grid[grain_pos[1]][grain_pos[0]] = '#'
                grain_pos = (500,0)
print(grains)

### Part 2 ###
### try to offset by x by max_y

max_y += 2
offset = max_y
max_x += 2 * offset
end_pos = (500 + offset,0)
grain_pos = (500 + offset,0)
grid = []
grains = 0
ranges_new = []
for i in ranges:
    ranges_new.append([(j[0]+offset, j[1]) for j in i])
    
for i in range(max_y + 1):
    if i == max_y: 
        grid.append(['#' for _ in range(max_x+1)])
    else: 
        grid.append(['.' for _ in range(max_x+1)])
for i in ranges_new:
    for obs in i:
        grid[obs[1]][obs[0]] = '#'            
                
while True:
    if grid[end_pos[1]][end_pos[0]] == '#':
        print("I am safe.")
        break
    down = (grain_pos[0], grain_pos[1]+1)
    downLeft = (grain_pos[0]-1, grain_pos[1]+1)
    downRight = (grain_pos[0]+1, grain_pos[1]+1)
    if grid[down[1]][down[0]] == '.':
        grain_pos = down
    else:
        if grid[downLeft[1]][downLeft[0]] == '.':
            grain_pos = downLeft
        else:
            if grid[downRight[1]][downRight[0]] == '.':
                grain_pos = downRight
            else:
                # print('Stopping at: ', grain_pos)
                grains+=1
                grid[grain_pos[1]][grain_pos[0]] = '#'
                grain_pos = end_pos
print(grains)                
                
    
        