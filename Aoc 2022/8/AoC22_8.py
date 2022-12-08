# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:09:52 2022

@author: DKARYPID
"""
import numpy as np

with open("./input.txt") as f:
    a = f.readlines()
    
####### Part 1 #######
size = len(a)
grid = np.zeros(shape=(size, size))
i = 0

for row in a:
    j = 0
    for height in row.strip():
        grid[i,j] = int(height)
        j+=1
    i+=1

total_left = 0
total_right = 0
total_top = 0
total_bottom = 0
for i in range(1, len(a)-1):
    for j in range(1, len(a)-1):
        print(i,j, " Value: ", grid[i,j])
        cursor = grid[i, j]
        ### Top ###
        # print("Top cells:")
        state = True
        for l in range(i-1, -1, -1):
            # print(grid[l, j])
            compare = grid[l, j]
            if cursor <= grid[l, j]:
                print("Top blocked")
                state = False
                break
        if state:
            total_top += 1
            continue
            
            
        ### Bottom ###
        # print("Bottom cells:")
        state = True
        for l in range(i+1, size):
            # print(grid[l, j])
            compare = grid[l, j]
            if cursor <= grid[l, j]:
                print("Bottom blocked")
                state = False
                break
        if state:
            total_bottom += 1
            continue
        
        ### Left ###
        # print("Left cells:")
        state = True
        for l in range(j-1, -1, -1):
            # print(grid[i, l])
            compare = grid[i, l]
            if cursor <= grid[i, l]:
                print("Left blocked")
                state = False
                break
        if state:
            total_left += 1
            continue
        
        ### Right ###
        # print("Right cells:")k
        state = True
        for l in range(j+1, size):
            # print(grid[i, l])
            compare = grid[i, l]
            if cursor <= grid[i, l]:
                print("Right blocked")
                state = False
                break
        if state:
            total_right += 1
            continue
        
        
print(total_bottom+total_left+total_right+total_top+ 2* size + 2 * (size - 2))

####### Part 2 #######
scores = []
for i in range(1, len(a)-1):
    for j in range(1, len(a)-1):
        score_left = 0
        score_right = 0
        score_top = 0
        score_bottom = 0
        
        cursor = grid[i, j]
        for l in range(i-1, -1, -1):
            score_top += 1
            compare = grid[l, j]
            if cursor <= grid[l, j]:
                print("Top blocked")
                break
            
        for l in range(i+1, size):
            score_bottom +=1
            compare = grid[l, j]
            if cursor <= grid[l, j]:
                print("Bottom blocked")
                break

        for l in range(j-1, -1, -1):
            score_left +=1
            compare = grid[i, l]
            if cursor <= grid[i, l]:
                print("Left blocked")
                break
            
        for l in range(j+1, size):
            score_right += 1
            compare = grid[i, l]
            if cursor <= grid[i, l]:
                print("Right blocked")
                break
        scores.append(score_bottom * score_left * score_right * score_top)
        
print(max(scores))
