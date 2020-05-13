# Notes on chapter 9
# imports through the chapter
from pathlib import Path

# The forward slash
Path('bacon', 'eggs', 'ham')
str(Path('spam', 'bacon', 'eggs'))
my_files = ['accounts.txt', 'details.csv', 'data.docs']
for filename in my_files:
    print(Path(r'/Users/Rosalie/', filename))

# Using the / Operator to Join Paths