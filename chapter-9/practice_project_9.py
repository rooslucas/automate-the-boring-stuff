# Practice projects of chapter 9
import pyinputplus as pyip
import re

# Practice project: Mad Libs
# Open the file and create a list
mad_lips_open = open(r'mad_lips_text.txt', 'r')
mad_lips_text = mad_lips_open.read()

# Check the text for adjectives, nouns, adverbs and verbs
words_regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
for word in words_regex.findall(mad_lips_text):
    new_word = pyip.inputStr(" Enter an " + word.lower() + ": ")
    mad_lips_text = mad_lips_text.replace(word, new_word, 1)

# Print the new text and add to a new file
print(mad_lips_text)
new_mad_lips = open(r'new_mad_lips.txt', 'w+')
new_mad_lips.write(mad_lips_text)
