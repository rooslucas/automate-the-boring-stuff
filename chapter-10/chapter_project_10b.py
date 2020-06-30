# Chapter project chapter 10
# Project: Backing Up a Folder into a ZIP FIle

import zipfile
import os


# Step 1: Figure Out the ZIP File's Name
def backup_to_zip(folder):
    # Back up the entire contents of "folder" into a ZIP file.

    folder = os.path, abspath(folder)  # make sure folder is absolute

    # Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    # Step 2: Create the new ZIP file
    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # Step 3: Walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        backup_zip.write(foldername)

        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
    backup_zip.close()
    print('Done.')


backup_to_zip('/Users/rosalie/developer/automate-the-boring-stuff')
