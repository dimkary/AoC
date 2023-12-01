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
### Part 1 ###
# tot = 0
# for line in a:
#     temp_nums = []
#     for digit in line:
#         if digit.isnumeric():
#             temp_nums.append(digit)
#     tot += int(''.join(temp_nums)[0]+''.join(temp_nums)[-1])
    
    
### Part 2 ###

tot = 0
for line in a:
    temp_nums = []
    this_line = line.replace('one','on1e'
    ).replace('two','tw2o').replace('three','thr3ee').replace('four','fou4r').replace(
        'five','fi5ve').replace('six','si6x').replace(
            'seven','sev7en').replace('eight','ei8ght').replace('nine','ni9ne').replace('zero','ze0ro')
    for digit in this_line:
        if digit.isnumeric():
            temp_nums.append(digit)
    print(''.join(temp_nums)[0]+''.join(temp_nums)[-1])
    tot += int(''.join(temp_nums)[0]+''.join(temp_nums)[-1])
