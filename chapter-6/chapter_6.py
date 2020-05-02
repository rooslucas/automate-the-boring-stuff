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

# English to Pig Latin
print('Enter the English message to translate to Pig Latin *oink oink*:')
message = input()
pig_latin = []  # The list that wil contain Pig Latin words
vowels = ('a', 'e', 'i', 'o', 'u', 'y')

for word in message.split():
    # Seperate the non-letters at the start of the word:
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]
    if len(word) == 0:
        pig_latin.append(prefix_non_letters)
        continue

    # Separate the non-letters at the end of this word:
    suffix_non_letters = ''
    while not word[-1].isalpha():
        suffix_non_letters += word[-1]
        word = word[:-1]

    # Remember the casing of the words
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()  # Useful for the translation

    # Separate consonants at beginning of the word
    prefix_consonants = ''
    while len(word) > 0 and not word[0] in vowels:
        prefix_consonants += word[0]
        word = word[1:]

    # Now where making the words pig Latin *oink oink*
    if prefix_consonants != '':
        word += prefix_consonants + 'ay'
    else:
        word += 'yay'

    # Restore casing
    if was_upper:
        word = word.upper()
    elif was_title:
        word = word.title()

    # Combine everthing as a word
    pig_latin.append(prefix_non_letters + word + suffix_non_letters)

# Add everything together as a big oinking family
print(' '.join(pig_latin))
