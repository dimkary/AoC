# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:39:19 2022

@author: trading
"""
with open('./input.txt', 'r') as f:
    lines = f.read().splitlines() 

### Part 1,2 ###
def printcrt(crt):
    for k in crt:
        print("".join(k))
        
def pix_proc(pixel, pos, crt):
    row    = pixel // width
    column = pixel % width
    
    if column in pos:
        crt[row][column] = "#"
    return crt


X = 1
cycle = 1
cycles = list(range(20,221,40))
snaps=[]
pixel = 0
width = 40
height = 6
crt =[['.' for _ in range(width)] for _ in range(height)]
pos = [X-1, X, X+1]
        

for line in lines:
    if line == "noop":
        pixel = (cycle - 1) % 240
        crt = pix_proc(pixel, pos, crt)
        cycle += 1
        if cycle in cycles:
            snaps.append(cycle * X)        
    if line != "noop":
        operation, strength = line.split()
        for _ in range(1):
            pixel = (cycle - 1) % 240
            crt = pix_proc(pixel, pos, crt)
            cycle += 1
            if cycle in cycles:
                snaps.append(cycle * X)            
        pixel = (cycle - 1) % 240
        crt = pix_proc(pixel, pos, crt)
        cycle += 1
       
        X += int(strength)
        pos = [X-1, X, X+1]
        if cycle in cycles:
            snaps.append(cycle * X)         
print(sum(snaps))
printcrt(crt)