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
numberOfSequenceHeads = 0
numberOfSequenceTails = 0
numberOfStreaks = 0

for experimentNumber in range(10000):
    number = random.choice(['Heads','Tails'])
    randomlist.append(number)
for i in range(len(randomlist)):
    if randomlist[i] == 'Heads':
        numberOfSequenceTails = 0
        numberOfSequenceHeads +=1
        if numberOfSequenceHeads ==6:
            numberOfStreaks +=1
    elif randomlist[i] == 'Tails':
        numberOfSequenceHeads = 0
        numberOfSequenceTails += 1
        if numberOfSequenceTails == 6:
            numberOfStreaks +=1
print(randomlist)
print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))


