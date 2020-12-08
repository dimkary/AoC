# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:00:43 2020

@author: pipi_
"""
def jmper(programm_file):
    instructions = dict([i for i in enumerate(programm_file)])
    instruction_counter = dict([(i,0) for i in range(len(programm_file))])
    
    counter = 0
    accu = 0
    line_number = len(programm_file)
    while True:
        temp_instruction = instructions[counter]
        instruction_counter[counter]+=1
        
        if instruction_counter[counter]>1:
            print ("Infinito looperito")
            return None
                    
        if "acc" in temp_instruction:
            accu += int(temp_instruction[4:])
            counter+=1
        
        if "nop" in temp_instruction:
            counter+=1
            
        if "jmp" in temp_instruction:
            counter+=int(temp_instruction[4:])    

        
        if counter == line_number:
            print("Success!!!")
            return accu
        
        counter = counter - (counter//line_number) * line_number
with open('input.txt','r') as f:
    all_lines = f.read().splitlines()

jumps = [i for i, x in enumerate(all_lines) if "jmp" in x or "nop" in x]

for jump in jumps:
    print(all_lines[jump])
    temp_program = all_lines.copy()
    if "jmp" in temp_program[jump]:
        temp_program[jump] = temp_program[jump].replace("jmp","nop")
    else:
        temp_program[jump] = temp_program[jump].replace("nop","jmp")        
    result = jmper(temp_program)
    if result:
        break

        