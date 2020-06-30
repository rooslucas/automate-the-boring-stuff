# Chapter project chapter 10
# Project: Renaming Files with American-Style Dates to European-Style Dates

# American-style dates: MM/DD/YYYY
# European-style dates: DD/MM/YYYY

import os
import re

# Step 1: Create a Regex for American-Style Dates
date_pattern = re.compile(r"""^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)\d\d)
(.*?)$
""", re.VERBOSE)

# Step 2: Identify the Date Parts from the Filenames
# Loop over the files in the working directory.
for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)

    # Skip files without a date
    if mo is None:
        continue

    # Get the different parts of the filename.
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    # Step 3: Form the New Filename and Rename the Files
    # Form the European-style filename.
    euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part

    # Get the full, absolute file paths.
    abs_working_dir = os.path.abspath('.')
    amer_filename = os.path.join(abs_working_dir, amer_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)

    # Rename the files.
    print(f'Renaming "{amer_filename}" to "{euro_filename}"...')
    # shutil.move(amer_filename, euro_filename) # uncomment after testing
