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

hands = {}
scores = {}
for line in a:
    hand, bid = line.split()
    hands[hand] = int(bid)
    
conversions = {
    'A':14,
    'K':13,
    'Q':12,
    'J':11,
    'T':10
    }

for hand in hands:
    uniques = set(hand)
    secondary_score = 0
    if len(uniques) == 5:
        primary_score = 0
    else:
        counts = []
        for unique in uniques:
            counts.append(hand.count(unique))
        counts = sorted(counts)
        if counts == [1, 1, 1, 2]:
            primary_score = 1000000
        elif counts == [1, 2, 2]:
            primary_score = 2000000
        elif counts == [1, 1, 3]:
            primary_score = 3000000
        elif counts == [2, 3]:
                primary_score = 4000000
        elif 4 in counts:
            primary_score = 5000000
        elif 5 in counts:
            primary_score = 6000000
        
    for i in range(5,0,-1):
        if hand[5-i] in conversions:
            secondary_score += conversions[hand[5-i]] * (15 ** (i-1))
        else:
            secondary_score += int(hand[5-i]) * (15 ** (i-1))
            # quinticimal system from 0-14 instead of 0-9
    scores[primary_score + secondary_score] = hand
    
rank = sorted(scores.keys())

winnings = 0
for i in range(len(rank)):
    # print(i+1, hands[scores[rank[i]]])
    winnings += (i+1) * hands[scores[rank[i]]]

print(winnings)

### Part 2 ###
scores = {}
conversions['J'] = 1
subs = [str(i) for i in range(2,10)] + list(conversions.keys())
subs.remove('J')
for hand in hands:
    uniques = set(hand)
    secondary_score = 0
    best = 0
    if 'J' in hand:
        alts = []
        for sub in subs:
            temp = "".join([i if i!= 'J' else sub for i in hand])
            alts.append(temp)
        for alt in alts:
            uniques = set(alt)
            if len(uniques) == 5:
                primary_score = 0
            else:
                counts = []
                for unique in uniques:
                    counts.append(alt.count(unique))
                counts = sorted(counts)
                if counts == [1, 1, 1, 2]:
                    primary_score = 1000000
                elif counts == [1, 2, 2]:
                    primary_score = 2000000
                elif counts == [1, 1, 3]:
                    primary_score = 3000000
                elif counts == [2, 3]:
                        primary_score = 4000000
                elif 4 in counts:
                    primary_score = 5000000
                elif 5 in counts:
                    primary_score = 6000000
            if primary_score > best:
               best = primary_score
    else:
        if len(uniques) == 5:
            primary_score = 0
        else:
            counts = []
            for unique in uniques:
                counts.append(hand.count(unique))
            counts = sorted(counts)
            if counts == [1, 1, 1, 2]:
                primary_score = 1000000
            elif counts == [1, 2, 2]:
                primary_score = 2000000
            elif counts == [1, 1, 3]:
                primary_score = 3000000
            elif counts == [2, 3]:
                    primary_score = 4000000
            elif 4 in counts:
                primary_score = 5000000
            elif 5 in counts:
                primary_score = 6000000        

    for i in range(5,0,-1):
        if hand[5-i] in conversions:
            secondary_score += conversions[hand[5-i]] * (15 ** (i-1))
        else:
            secondary_score += int(hand[5-i]) * (15 ** (i-1))
            # quinticimal system from 0-14 instead of 0-9
    if "J" in hand:
        scores[best + secondary_score] = hand
    else:
        scores[primary_score + secondary_score] = hand
    
rank = sorted(scores.keys())

winnings = 0
for i in range(len(rank)):
    # print(i+1, hands[scores[rank[i]]])
    winnings += (i+1) * hands[scores[rank[i]]]

print(winnings)