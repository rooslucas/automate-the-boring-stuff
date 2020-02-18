#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 19:38:49 2020

@author: rosalie
"""
import random


# Chapter three learning about functions


def hello(name, number):
    for i in range(1, number):
        print('Howdy, ' + name)
        print('Howdy!!! ' + name)
        print('Hello there, ' + name)


hello("roos", 3)
hello("cor", 1)


# function of magic ball


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


print(getAnswer(random.randint(1, 9)))


# function the Call Stack
def a(name):
    print(name + ' starts')
    b('Deborah')
    d('Cor')
    print(name + ' returns')


def b(name):
    print(name + ' starts')
    c('Andre')
    print(name + ' returns')


def c(name):
    print(name + ' starts')
    print(name + ' returns')


def d(name):
    print(name + ' starts')
    print(name + ' returns')


a('Roos')


# Learning about local and global scopes
def spam():
    eggs = 99
    bacon()
    print(eggs)


def bacon():
    ham = 101
    eggs = 0


def sspam():
    print(eggss)


eggss = 42
sspam()
print(eggss)


def globalChange():
    global pie
    pie = 'spam'


pie = 'global'
globalChange()
print(pie)


# Exeption Handling

def exception(divideBy):
    try:
        return 42 / float(divideBy)
    except ZeroDivisionError:
        print('Delen door nul is flauwekul')


print(exception(2))
print(exception(12))
print(exception(0))
print(exception(1))

# Making a little zig zag program

import time
import sys

indent = 0  # How many spaces you need
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)  # Pause for 1/10 of a second.
        if indentIncreasing: # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False  # Change direction.
            else:
                # Decrease the number of spaces:
                indent = indent - 1
                if indent == 0:
                    indentIncreasing = True  # Change direction.
except KeyboardInterrupt:
    sys.exit()


# Practice Project -> collatz sequence

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result


numb = (input("Enter a number: "))
try:
    while numb != 1:
        numb = collatz(int(numb))
except ValueError:
    print("Use an INTEGER")
