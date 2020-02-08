#automate-the-boring-stuff chapter 2

import random
import sys
import os
import math

#learning about Boolean functions
#blocks of code

name = 'Rosalie'
password = 'fish'

if name == 'Rosalie':
    print ('Hello Rosalie')
    if password == 'swordfish':
        print ('Access granted')
    else: 
        print('Wrong password name combination')
        
#learning more about flow control
age = 3000
if name == 'Alice':
    print('Hello Alice')
elif age < 12:
    print('You are not Alice kiddo')
elif age > 100:
    print('You are not Alice, Granny')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire')
else:
    print('You are neither Alice nor a little kid')
    
#learning about a while loop
spam = 0
while spam < 5:
    print('Hello world.')
    spam = spam + 1
    
#learning more about a while loop
name = ''
while True:
    print('Please enter your name')
    name = input()
    if name == 'your name':
        break
print('Thank you')
  
#while loop about certain input    
while True:
    print('Who are you?')
    name = input()
    if name != 'Roos':
        continue
    print ('Hello Roos, what is your password?')
    password = input()
    if password == 'swordfish':
            break
print ('Access granted')
 
#while loop about a name    
name = ''
while not name:
    print('Enter your name')
    name = input ()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print ('Be sure to have enough room')
print('Done')
    
#learning about for loops and range functions
print('My name is')
for i in range(-5,1,1):
    print('Jimmy Five Times (' + str(i) + ')')

total = 0
for num in range(101):
    total = total + num
print (total)

print ('My name is')
i = 0
while i<5:
    print('Jimmy Five times (' + str(i) + ')')
    i = i+1

#learning about the use of importing packages
for i in range(5):
    print(random.randint(1,10))
    
while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.' )
    
#making a simple programm to guess a number
#This is the number guess game
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20')

#ask the player to guess multiple times
for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())
   
    if guess < secretNumber:
        print('Your guess is to low')
    elif guess > secretNumber:
        print('Your guess is to high')
    else:
        break #Hopefully it's correct now
    
if guess == secretNumber:
    print('Wow you guessed right')
else:
    print('Wow you dumb ass')
    
#Short program rock, paper, scissors
print('ROCK, PAPER, SCISSORS')

#these variables are trackers of the wins and losses
wins = 0
losses = 0
ties = 0

while True:
    print('%s wins,%s losses, %s ties' % (wins, losses, ties))
    while True:
        print('Enter your move')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type one of r, p, s, or q.')
        
# Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
    
    if computerMove == playerMove:
        print("It's a tie")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
#Write code that prints Hello if 1 is stored in spam, 
#prints Howdy if 2 is stored in spam, 
#and prints Greetings! if anything else is stored in spam.

spam = random.randint(1,5)
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings')