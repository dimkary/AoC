# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:09:52 2022

@author: DKARYPID
"""

with open("./input.txt") as f:
    a = f.readlines()[0]

for i in range(len(a)-4):
    l1 = a[i]
    l2 = a[i+1]
    l3 = a[i+2]
    l4 = a[i+3]
    if len(set([l1,l2,l3,l4])) == 4:
        break

print(i+4)


for i in range(len(a)-14):

    
    letters = [a[j] for j in range(i,i+14)]
    if len(set(letters)) == 14:
        break
    
print(i+14)