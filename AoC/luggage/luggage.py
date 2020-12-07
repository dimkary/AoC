# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:00:43 2020

@author: pipi_
"""
from string import digits
from itertools import islice
remove_digits = str.maketrans('', '', digits)

with open('input.txt','r') as f:
    all_lines = f.read().splitlines()
    
parsed = {}
for line in all_lines:
    temp = line.split(" contain ")
    bags = temp[1].replace(".","").translate(remove_digits).replace("bags","").replace("bag","").split(",")
    bags = [i.strip() for i in bags]
    numbers = [int(i) for i in temp[1] if i.isdigit()]
    parsed[temp[0].replace("bags","").replace("bag","").strip()] = dict(zip(bags, numbers))
    #parsed[temp[0].replace("bags","bag").replace("bag","")]=value

def traverse(bag="A"):
    check = parsed[bag]
    if check:
        print("Looking into : ", bag)
        print("Contains : ", parsed[bag])
        print(len(parsed[bag])==2)
        head = bag
        travel = list(parsed[head].keys())
        values = list(parsed[head].values())
        left = travel[0]
        leftTravel = values[0]*traverse(left)
        rightTravel = 0
        if (len(parsed[bag])==2):
            right = travel[1]
            rightTravel = values[1]*traverse(right) 
            print(rightTravel)
        
        elif (len(parsed[bag])==1):
            rightTravel=0
        else:
            right = travel[1:]
            rightValues = values[1:]
            trial = [traverse(x) * y for x,y in zip(right,rightValues)]
            rightTravel = sum(trial)
            
        print(leftTravel)

        return leftTravel + rightTravel + 1
    else:
        return 1
bag = "shiny gold"
# bag="A"
hi = traverse(bag = bag) - 1

