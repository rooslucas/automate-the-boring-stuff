#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 19:19:40 2020

@author: rosalie
"""
from __future__ import print_function
get_ipython().magic('reset -sf') #reset stuff
import random
import copy
import time

# Learning about lists
spam = ['harry', 'ron', 'george', 'fred']#, [10,20,30,40,50]
print(spam[0][3])
print(spam[1][:])
len(spam)

spam[1] = 'weasley'
print(spam)

del spam[3]
print(spam)

# Storing info in a list

print('Enter the name of candy 1:')
candyName1 = input()
print('Enter the name of candy 2:')
candyName2 = input()
print('Enter the name of candy 3:')
candyName3 = input()
print('Enter the name of candy 4:')
candyName4 = input()
print('Enter the name of candy 5:')
candyName5 = input()
print('Enter the name of candy 6:')
candyName6 = input()
print('The names of the candies are:')
print(candyName1 + ' ' + candyName2 + ' ' + candyName3 + ' ' + candyName4 + ' ' +
candyName5 + ' ' + candyName6)

candyList = [candyName1, candyName2, candyName3, candyName4, candyName5, candyName6]
print(candyList)

# Learning the more efficient way of doing this

candyNames = []
while True:
    print('Enter the name of your candies ' + str(len(candyNames) + 1) + 
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    candyNames = candyNames + [name]  # list concatenation
print('The candy names are:')
for name in candyNames:
    print('  ' + name)

print (candyNames)


for i in range(len(candyNames)):
    print('Candy ' + str(i) + ' is called: ' + candyNames[i])

# Learning about in and not operators

'howdy' in ['hello','hey','howdy','yo']
'harry' not in spam
'cody' in spam

appleDevices = ['iPhone', 'iPad', 'Apple Watch', 'MacBook']
print('Enter an Apple device')
answer = (input())
if answer not in appleDevices:
    print('I do not own a(n) ' + answer)
elif answer in appleDevices:
    print('Yes I do own a(n) ' + answer)

# The multiple assignment trick

iPhone = ['Xr', 'coral', '64 GB']
model, color, storage = iPhone

print(model, color, storage)
print(color)

for index, item in enumerate(appleDevices):
    print('Product ' + str(index) + ' is a(n) ' + item)
    
random.choice(appleDevices)

# The more elegant version of Magic 8 Ball
messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])

name = 'ROSALIE'
for i in name:
    print('***' + i + '***')
    
# Learning about references
    
def lollyPops(someParameter):
    someParameter.append('Hello')

eggs = [1, 2, 3]
lollyPops(eggs)
print(eggs)    

# A Short Program: Conway’s Game of Life

WIDTH = 60
HEIGHT = 20

#creating a list of list for the cells
nextCells = []
Q = 1
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') #Living cell
        else:
            column.append(' ') #dead cell
    nextCells.append(column)

while Q<10: #main loop
    print('\n\n\n\n\n') #seperation
    currentCells = copy.deepcopy(nextCells)
    
    #print currentCells on screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()

    #calculation    
    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
        
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.
            
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors ==3):
                nextCells[x][y] = '#'
            elif currentCells[x][y] == '' and numNeighbors == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ''
    time.sleep(1)
    Q = Q + 1

        