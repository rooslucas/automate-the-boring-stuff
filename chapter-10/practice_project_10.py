# Practice Project 1 from chapter 10
# Selective Copy

import os
import shutil
from pathlib import Path
import fnmatch


# Step 3: Walk the entire folder tree and compress the files in each folder
def selective_copy(folder, extension):
    matches = []
    folder = os.path.abspath(folder)

    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Searching for {extension} files...')

        for filename in fnmatch.filter(filenames, f"*.{extension}"):
            matches.append(os.path.join(foldername, filename))

    for file in matches:
        home_path = Path.home()
        shutil.copy(folder / file, home_path / 'new_folder' / file)

    print('Done.')
