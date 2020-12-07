# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:00:43 2020

@author: pipi_
"""
required_fields = sorted(['byr','iyr','eyr','hgt','hcl','ecl','pid'])
eye_colors = ['amb','blu','brn','gry','grn','hzl','oth']
import re

with open('input.txt','r') as f:
     passports = [dict(keVal.split(':') for keVal in line.split(' ')) 
                  for line in [x.replace("\n"," ") 
                               for x in f.read().split("\n\n")]]
valids = 0

for passport in passports:
    fields = sorted(list(passport.keys()))
    if(set(required_fields).issubset(set(fields))): 
        #byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if not int(passport["byr"]) in range(1920,2003):
            #print(passport["byr"])
            continue
        #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if not int(passport["iyr"]) in range(2010,2021):
            #print(passport["iyr"])
            continue
        #eyr (Expiration Year) - four digits; at least 2020 and at most 2030
        if not int(passport["eyr"]) in range(2020,2031):
            #print(passport["eyr"])
            continue        
        # hgt (Height) - a number followed by either cm or in:
        #   If cm, the number must be at least 150 and at most 193.
        #   If in, the number must be at least 59 and at most 76.  
        x = re.search("([0-9]{2,3})(cm|in)", passport["hgt"])
        if x:
            if x.group(2)=="cm":
                if not int(x.group(1)) in range(150,194):
                    #print("Invalid: ", x.group(1)," cm")
                    continue
            else:
                if not int(x.group(1)) in range(59,77):
                    #print("Invalid: ", x.group(1)," in")
                    continue
        else: continue
        #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        x = re.search("(#)([0-9a-z]{6})", passport["hcl"])
        if not x:
             #print("Invalid color: ", passport["hcl"])
             continue
        #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if passport["ecl"] not in eye_colors:
            #print("Invalid color: ", passport["ecl"])
            continue
        #pid (Passport ID) - a nine-digit number, including leading zeroes.
        pid = passport["pid"]
        if not (pid.isdigit() and len(pid)==9):
            print("Invalid pid :", pid)
            continue
        valids += 1

print(valids)






