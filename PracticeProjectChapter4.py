#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 18:11:13 2020

@author: rosalie
"""

from __future__ import print_function
get_ipython().magic('reset -sf') #reset stuff
import random
import copy
import time
from itertools import groupby

# Project 1: Comma Code

spam = ['Frozen 2', 'BigHero 6', 'Tangled', 'Little Mermaid']

def comma(a_list):
    count=0
    a_string=''
    for i in range(len(a_list)-1):
        a_string += a_list[count] + ', '
        count+=1
    return a_string + 'and ' + a_list[count]

print(comma(spam))

# Project 2: Coin Flip Streak

randomlist = []
numberOfStreaks = 0

for experimentNumber in range(20):
    number = random.randint(0,1)
    if number == 0:
        number = 'Heads'
    elif number == 1:
        number = 'Tails'
    randomlist.append(number)
    patternDataHeads = ['Heads','Heads','Heads','Heads','Heads','Heads']
    patternDataTails = ['Tails','Tails','Tails','Tails','Tails','Tails']
for i in range(len(randomlist)):
    if randomlist[i:i+len(patternDataHeads)]==patternDataHeads or randomlist[i:i+len(patternDataTails)]==patternDataTails:
        numberOfStreaks +=1
print(randomlist)
print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))


