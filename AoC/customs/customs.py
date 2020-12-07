# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:00:43 2020

@author: pipi_
"""

import re

with open('input.txt','r') as f:
     answers =f.read().split("\n\n")

lengths = []
yes_list = []
for answer in answers:
    print("--- NEW ANSWER ---")
    all_yes = list(set(answer.replace("\n","")))
    group = answer.split("\n")
    yes_num = 0
    for yes in all_yes:
        for person in group:
            print(yes, person)
            if yes not in person: 
                yes_num-=1
                break
        yes_num+=1
    yes_list.append(yes_num)
    