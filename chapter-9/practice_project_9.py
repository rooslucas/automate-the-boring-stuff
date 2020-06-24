# Practice projects of chapter 9
import pyinputplus as pyip
import re

# Practice project: Mad Libs
# Open the file and create a list
mad_lips_open = open(r'mad_lips_text.txt', 'r')
mad_lips_text = mad_lips_open.read()
list_mad_lips = mad_lips_text.split(' ')

# Check for dots (also possible for other punctuation marks)
dots = []
for i in range(len(mad_lips_text)):
    if mad_lips_text[i] == '.':
        dots.append(i)
mad_lips_text = mad_lips_text.replace('.', '')

# Check the text for adjectives, nouns, adverbs and verbs
words_regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
for word in words_regex.findall(mad_lips_text):
    if word == 'ADJECTIVE':
        adjective = pyip.inputStr("Enter an adjective: ")
        list_mad_lips[(list_mad_lips.index(word))] = adjective
    elif word == 'NOUN':
        noun = pyip.inputStr("Enter a noun: ")
        mad_lips_text.replace('NOUN', noun)
        list_mad_lips[(list_mad_lips.index(word))] = noun
    elif word == 'ADVERB':
        adverb = pyip.inputStr("Enter an adverb: ")
        list_mad_lips[(list_mad_lips.index(word))] = adverb
    elif word == 'VERB':
        verb = pyip.inputStr("Enter a verb: ")
        list_mad_lips[(list_mad_lips.index(word))] = verb

# Combine the list into a string and add the punctuation marks
str_mad_lips = ' '.join([str(word) for word in list_mad_lips])

for i in range(len(dots)):
    index = dots[i]
    total_mad_lips = str_mad_lips[:index] + '.' + str_mad_lips[index:]

# Print the new text and add to a new file
print(total_mad_lips)
new_mad_lips = open(r'new_mad_lips.txt', 'w+')
new_mad_lips.write(total_mad_lips)
