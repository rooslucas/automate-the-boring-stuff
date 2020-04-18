import pyperclip

spam = "That is Alice's cat"
spam2 = 'Say hi to Bob\'s mom.'
print("Hello there!\nHow are you?\nI\'m doing fine.")
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')


def spam():
    """This is a multiline comment to help
    explain what the spam() function does."""
    print('Hello!')


# Learning about f-string --> always put the f in front of it.
name = 'Rosalie'
age = 19
frubbles = f'My name is {name}. I am {age} years old.'  # with f

rubbles = 'My name is {name}. I am {age} years old.'  # without f
print(frubbles)
print(rubbles)

# Upper and lower casing
greeting = 'Hello, world!'
greeting = greeting.upper()
print(greeting)
greeting = greeting.lower()
print(greeting)

# Learning about the isX() methods
while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only).')
    password = input()
    if password.isalnum():
        break
    print('Password can only have letters and numbers.')
spam3 = '''Dear Alice, 
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''

print(spam3)
print(spam3.split('\n'))


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# Learning about the Pyperclip Module
pyperclip.copy('Hello, world!')
print(pyperclip.paste())

