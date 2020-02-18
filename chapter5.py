#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:06:41 2020

@author: rosalie
"""
import pprint

# Chapter 5 Dictonaries and Structuring data
from typing import Dict

myLaptop = {'size': '11 inch', 'color': 'silver', 'type': 'air'}
myMacBook = {'color': 'silver', 'type': 'air', 'size': '11 inch'}

# practice dictionaries with birthdays

birthdays = {'Cor': '25/09', 'Mama': '17/12', 'Papa': '30/09'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name + '.')
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updates')

# methods for dictionaries

for v in myLaptop.values():
    print(v)

for k in myLaptop.keys():
    print(k)

for i in myLaptop.items():
    print(i)

# little project about set.default & learning about pprint

message = 'It was a bright cold day in April, and the clocks where stricking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

# making tic, tac, toe

theBoard = {'top-L': '', 'top-M': '', 'top-R': '',
            'mid-L': '', 'mid-M': '', 'mid-R': '',
            'low-L': '', 'low-M': '', 'low-R': ''}

theBoards = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M': 
    'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': '', 'low-R': 'X'} 


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


printBoard(theBoards)

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)

# Nested dictionaries and lists

allGuests = {'Cor': {'Chips': 20, 'Chocolat': 2}, 'Roos': {'Chips': 23,
                                                           'Chocolat': 1}, 'Jolinde': {'Chips': 24, 'Chocolat': 4}}


def totalBrought(guests, item):
    numBrought: int = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought


print('Number of things being brought:')
print(' - Chips ' + str(totalBrought(allGuests, 'Chips')))
print(' - Chocolat ' + str(totalBrought(allGuests, 'Chocolat')))
