# Practice Project 2 from chapter 10
# Deleting Unneeded Files

import os
from pathlib import Path


def find_big_files(folder):
    folder = os.path.abspath(folder)

    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Searching for big files in {foldername}...')

        for filename in filenames:
            file_path = Path(filename)
            size = os.path.getsize(filename)
            if size >= 100:
                file_path = str(folder / file_path)
                print(f'{file_path} is {size} MB')

    print('Done')
