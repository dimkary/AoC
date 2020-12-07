# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:00:43 2020

@author: pipi_
"""

import math
from functools import reduce

def tree_finder(right, down, all_lines):    
    iterations = math.floor(len(all_lines)/down)
    total_rights = right*iterations
    
    replications = math.ceil(total_rights/len(all_lines[0]))
    for i in range(len(all_lines)):
        all_lines[i]*=replications
        
    coordinates = (0,0)
    tree_count = 0
    
    for iteration in range(iterations):
        current_cell = all_lines[coordinates[1]][coordinates[0]]
        if (current_cell == "#"):
            tree_count+=1
        coordinates = (coordinates[0]+right, coordinates[1]+down)
    return tree_count


with open('map.txt','r') as f:
     all_lines = f.read().splitlines() 
   
rights = [1]
downs = [2]
rights = [1,3,5,7,1]
downs = [1,1,1,1,2]
tree_list = []

for right,down in zip(rights, downs):
    print(right, " : ", down)
    tree_list.append((tree_finder(right, down, all_lines)))

result = reduce((lambda x, y: x * y), tree_list)