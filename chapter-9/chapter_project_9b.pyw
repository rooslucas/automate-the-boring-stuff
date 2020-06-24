# Practice project 2 from chapter 9
# Project: Updatable Multi-Clipboard

# ! python3
# Usage: py.exe chapter_project_9b.pyw save <keyword> -Save clipboard to keyword.
# python3 chapter_project_9b.pyw <keyword> - Loads keyword to clipboard.
# python3 chapter_project_9b.pyw list - Loads all keywords to clipboard

import shelve
import pyperclip
import sys

mcb_shelf = shelve.open('mbc')

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()
