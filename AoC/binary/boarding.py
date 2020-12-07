# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:00:43 2020

@author: pipi_
"""
import re

def boardingParse(line:str):
    row = int(line[0:7],2)
    col = int(line[7:],2)
    setID=row*8+col
    return (row,col,setID)

seatID_list = []

with open('input.txt','r') as f:
    all_lines = f.read().replace("B","1").replace("F","0").replace(
        "R","1").replace("L","0").splitlines()
  
for line in all_lines:
    seatID_list.append(boardingParse(line)[2])