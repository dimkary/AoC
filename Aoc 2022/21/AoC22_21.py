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

dic = {}

for i in a:
    this = i.split(sep = ":")
    monkey = this[0]
    yell = this[1].strip()
    
    if yell.isdigit() :
        dic[monkey] = int(yell)
    else:
        dic[monkey] = yell
dic2 = dic.copy()
     
def monkmonk(monkey):
    expression = dic[monkey]
    if isinstance(expression, int):
        return expression
    else:
        expre = expression.split()
        
        first = expre[0]
        second = expre[2]
        calc = expre[1]
        
        if calc == '+':
            res = monkmonk(first) + monkmonk(second)
        elif calc == '-':
            res = monkmonk(first) - monkmonk(second)
        elif calc == '*':
            res = monkmonk(first) * monkmonk(second)
        else: #calc == '/':
            res = monkmonk(first) // monkmonk(second)            
        dic[monkey] = res
        return res
            
monkmonk('root')

print(dic['root'])

### Part 2 ###
# real input goes monotonically down
# test goes up
# for test input, reverse all 'first_result' 'second_result' checks
dic = dic2.copy()
trial = 9

def monkmonk2(monkey):
    expression = dic[monkey]
    if isinstance(expression, int):
        if monkey != 'humn':
            return expression
        else:
            return trial
    else:
        expre = expression.split()
        
        first = expre[0]
        second = expre[2]
        calc = expre[1]
        
        if calc == '+':
            res = monkmonk2(first) + monkmonk2(second)
        elif calc == '-':
            res = monkmonk2(first) - monkmonk2(second)
        elif calc == '*':
            res = monkmonk2(first) * monkmonk2(second)
        else: #calc == '/':
            res = monkmonk2(first) // monkmonk2(second)            
        dic[monkey] = res
        return res

root = dic['root'].split()
first_path = root[0]
second_path = root[2]

second_result = monkmonk2(second_path)
first_result = monkmonk2(first_path)

# Loop to find the Magnitude
while first_result > second_result:
    dic = dic2.copy()
    trial = int(str(trial) + '9')
    first_result = monkmonk2(first_path)

first_result = monkmonk2(first_path)
trial = list(str(trial).replace('9', '0'))
trial[0] = '1'

# Loop all digits from left to right to
# fine tune the correct number to match the root components
for i in range(len(trial)):
    cont = True
    while cont == True:
        dic = dic2.copy()
        pretrial = trial.copy()
        trial = int(''.join(trial))
        first_result = monkmonk2(first_path)
        if first_result > second_result:
            trial = pretrial.copy()
            if trial[i] == '9':
                cont = False
            else:
                trial[i] = str(int(trial[i]) + 1)
            reset = pretrial.copy()
        elif first_result < second_result:
                trial = reset.copy()
                cont = False
        else:
            print(trial)
            break
# second path is not relevant to humn
            
            
    