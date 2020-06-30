import shutil
import os
from pathlib import Path
import send2trash
import zipfile

# Copying Files and Folders
p = Path.home()  # /Users/rosalie
shutil.copy(p / 'spam.txt', p / 'some_folder')
shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt')
shutil.copytree(p / 'spam', p / 'spam_backup')  # Source, destination

# Moving and Renaming Files and Folders
shutil.move('source', 'destination')
shutil.move('source & old name', 'destination & new name')

# Permanently Deleting Files and Folders
os.unlink(path)  # Deletes the file at path.
os.rmdir(path)  # Deletes the folder at path, folder must be empty.
shutil.rmtree(path)  # Removes the folder at path and everything inside.
# Before usage check with print() if you want to delete the right files

# Safe Deletes with the send2trash Module
bacon_file = open('bacon.txt', 'a')
bacon_file.write('Bacon is not a vegetable.')
bacon_file.close()
send2trash.send2trash(bacon_file)

# Walking a Directory Tree
for folder_name, subfolders, filenames in os.walk('/Users/rosalie/developer/automate-the-boring-stuff'):
    print('The current folder is ' + folder_name)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folder_name + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folder_name + ': ' + filename)

    print('')

# Compressing Files with the zipfile Module
# Reading ZIP Files
example_zip = zipfile.ZipFile(p / 'example.zip')
example_zip.namelist()  # ['spam.txt', 'cats/catsnames.txt', 'cats/zophie.jpg']
spam_info = example_zip.getinfo('spam.txt')
spam_info.file_size  # 13908
spam_info.compress_size  # 3828
print(f'Compressed file is {round(spam_info.file_size / spam_info.compress_size, 2)} x smaller!')
# Compressed file is 3.63x smaller!
example_zip.close()

# Extracting from ZIP Files
example_zip.extractall()  # Can give a folder to put the stuff in
example_zip.close()

example_zip.extract('spam.txt')
example_zip.extract('spam.txt', '/Users/rosalie/some/new/folders')  # Put it in a (existing) folder
example_zip.close()

# Creating and Adding to ZIP Files
new_zip = zipfile.ZipFile('new.zip', 'w')  # 'a' is append mode
new_zip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)  # This type works for all data
new_zip.close()
