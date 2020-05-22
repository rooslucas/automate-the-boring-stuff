# Notes on chapter 9
# imports through the chapter
from pathlib import Path
import os

# The forward slash
Path('bacon', 'eggs', 'ham')
str(Path('spam', 'bacon', 'eggs'))
my_files = ['accounts.txt', 'details.csv', 'data.docs']
for filename in my_files:
    print(Path(r'/Users/Rosalie/', filename))

# Using the / Operator to Join Paths
Path('spam') / 'bacon' / 'eggs'
Path('spam') / Path('bacon/eggs')
Path('spam') / Path('bacon', 'eggs')

home_folder = r'/Users/Rosalie'
sub_folder = 'spam'
total_folder = home_folder + '\\' + sub_folder
'\\'.join([home_folder, sub_folder])

home_folder_2 = Path('/Users/Rosalie')
sub_folder_2 = Path('spam')
print(str(home_folder_2 / sub_folder_2))

# The Current Working Directory
Path.cwd()  # The path for the current directory
os.chdir('/Users/rosalie')
Path.cwd()  # The path for the directory above

# The Home Directory
Path.home()

# Absolute vs. Relative Paths
# An Absolute path always begins with the root folder
# A Relative path is relative to the program's current working directory

# Creating New Folders Using the os.makedirs() Function
# os.makedirs('/Users/rosalie/delicious/walnut/waffles')

# Handling Absolute and Relative Paths
Path.cwd()
print(Path.cwd().is_absolute())
print(Path('spam/bacon/eggs').is_absolute())

Path('my/relative/path')
Path.cwd() / Path('my/relative/path')  # PosixPath('/Users/rosalie/my/relative/path')
Path.home() / Path('my/relative/path')  # For when a path is relative to that path

os.path.abspath('.')  # '/Users/rosalie'
os.path.abspath('./Developer')  # '/Users/rosalie/Developer'
os.path.isabs('.')  # False
os.path.isabs(os.path.abspath('.'))  # True

os.path.relpath('/Users/rosalie/Developer', '/Users/rosalie')  # 'Developer'
os.path.relpath('/Users/rosalie/Developer', '/Users/rosalie/spam/eggs')  # '../../Developer'

# Getting the Parts of a File Path
# Containing the anchor(root folder), parent(folder containing file) and name made of stem(name) and suffix(extension)
p = Path('/Users/rosalie/haha.txt')
p.anchor  # '/'
p.parent  # A path object: PosixPath('/Users/rosalie')
p.name  # 'haha.txt'
p.stem  # 'haha'
p.suffix  # 'txt'
p.drive  # ''

Path.cwd()  # PosixPath('/Users/rosalie/Developer/automate-the-boring-stuff')
Path.cwd().parents[0]  # PosixPath('/Users/rosalie/Developer')
Path.cwd().parents[1]  # PosixPath('/Users/rosalie')
Path.cwd().parents[2]  # PosixPath('/Users')
Path.cwd().parents[3]  # PosixPath('/')

calc_file_path = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(calc_file_path)  # 'calc.exe'
os.path.dirname(calc_file_path)  # 'C:\\Windows\\System32'
os.path.split(calc_file_path)  # 'C:\\Windows\\System32', 'calc.exe'

'/usr/bin'.split(os. sep)  # ['', 'usr', 'bin']

# Finding File Sizes and Folder Contents
os.path.getsize(calc_file_path)  # size of bytes of your path
os.listdir(calc_file_path)  # return a list of filename strings for each file in path

total_size = 0
for filename in os.listdir('C:\\Windows\\System32'):
    total_size = total_size + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
    print(total_size)
# 2559970473

# Modifying a List of Files Using Glob Patterns
p = Path('/Users/Rosalie/Developer')
p.glob('*')
list(p.glob('*'))
list(p.glob('*.txt'))
list(p.glob('project?.docx'))
list(p.glob('*.?x?'))

# You can use this method to get pathways for different text files
