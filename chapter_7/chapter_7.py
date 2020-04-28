import re


# Notes on chapter 7
# Pattern Matching with Regular Expressions

# phone number check without regular expressions
def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
        for i in range(4, 7):
            if not text[i].isdecimal():
                return False
        if text[7] != '-':
            return False
        for i in range(8, 12):
            if not text[i].isdecimal():
                return False
        return True


# print('Is 415-555-4242 a phone number?')
# print(is_phone_number('415-555-4242'))
# print('Is Moshi moshi a phone number?')
# print(is_phone_number('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i + 12]
    if is_phone_number(chunk):
        print('Phone number found: ' + chunk)
print('Done')

# Creating Regex Objects
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

# Grouping with Parentheses
print(mo.group(1))
print(mo.group(2))
area_code, main_number = mo.groups()
print(area_code)
print(main_number)

phone_num_regex_2 = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
# add a \ for character to make it part of pattern
mu = phone_num_regex_2.search('My phone number is (415) 222-3232.')
print(mu.group(1))
print(mu.group(2))

# Matching Multiple Groups with the Pipe
hero_regex = re.compile(r'Thor|Captain America')
mo_1 = hero_regex.search('Thor and Captain America')
print(mo_1.group())
mo_2 = hero_regex.search('Captain America and Thor')
print(mo_2.group())

# you can use | to specify a prefix with different words
bat_regex = re.compile(r'Bat(man|mobile|coper|bat)')
mo_3 = bat_regex.search('Batmobile lost a wheel')
print(mo_3.group())
print(mo_3.group(1))

# Optional Matching with the Question mark
bat_gender_regex = re.compile(r'Bat(wo)?man')
bat_1 = bat_gender_regex.search('The Adventures of Batman')
print(bat_1.group())

bat_2 = bat_gender_regex.search('The Adventures of Batwoman')
print(bat_2.group())