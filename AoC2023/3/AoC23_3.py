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
    
test_numbs = []
number_pattern = re.compile(r'\b\d+\b')

grid = []
for i in a:
    grid.append([x for x in i])
    # Find all matches in the input string
    matches = number_pattern.findall(i) 
    test_numbs.extend([int(c) for c in matches])

test_numbs = set(test_numbs)
    
withh = []
without = []
all_nums = []
num_buf = []
adj = False 

gears = {}
temp_gears = set() 

# Part 1
for row in range(len(grid)):
    if num_buf:
        this_num = ''.join(num_buf)               
        if adj:
            withh.append(int(this_num))
        else:
            without.append(int(this_num))
        all_nums.append(int(this_num))
        num_buf = []
        adj = False  
        for gear in set(temp_gears):
            if gear not in gears:
                gears[gear] = [int(this_num)]
            else:
                gears[gear].append(int(this_num))
        temp_gears = set()        
    num_buf = []
    adj = False
    for col in range(len(grid)):

        digit = grid[row][col]
        if digit not in [str(i) for i in range(0,10)]:
            if num_buf:
                this_num = ''.join(num_buf)               
                if adj:
                    withh.append(int(this_num))
                else:
                    without.append(int(this_num))
                all_nums.append(int(this_num))
                num_buf = []
                adj = False
                for gear in set(temp_gears):
                    if gear not in gears:
                        gears[gear] = [int(this_num)]
                    else:
                        gears[gear].append(int(this_num))
                temp_gears = set()
        else:
            if digit in [str(i) for i in range(0,10)]:
                num_buf.append(digit)               
                try:
                    if grid[row - 1][col - 1] not in [str(i) for i in range(0,10)]+['.']:
                        adj = True
                        temp_gears.add((row - 1, col - 1))
                            
                except:
                    pass
                try:
                    if grid[row - 1][col] not in [str(i) for i in range(0,10)]+['.']:
                        adj = True
                        temp_gears.add((row - 1, col))
                except:
                    pass            
                try:
                    if grid[row - 1][col + 1] not in [str(i) for i in range(0,10)]+['.']:
                        adj = True
                        temp_gears.add((row - 1, col + 1))
                except:
                    pass                        
                try:
                    if grid[row][col - 1] not in [str(i) for i in range(0,10)]+['.']:
                        adj = True
                        temp_gears.add((row, col - 1))
                except:
                    pass
                try:
                    if grid[row][col + 1] not in [str(i) for i in range(0,10)]+['.']:
                        adj = True
                        temp_gears.add((row, col + 1))
                except:
                    pass            
                try:
                    if grid[row + 1][col - 1] not in [str(i) for i in range(0,10)]+['.']:
                        adj = True
                        temp_gears.add((row + 1, col - 1))
                except:
                    pass
                try:
                    if grid[row + 1][col] not in [str(i) for i in range(0,10)]+['.']:
                        adj = True
                        temp_gears.add((row + 1, col))
                except:
                    pass
                try:
                    if grid[row + 1][col + 1] not in [str(i) for i in range(0,10)]+['.']:
                        adj = True
                        temp_gears.add((row + 1, col + 1))
                except:
                    pass

print(sum(withh))     
total = 0

for gear in gears:
    if len(gears[gear]) == 2:
        total += gears[gear][0] * gears[gear][1]
        
print(total)