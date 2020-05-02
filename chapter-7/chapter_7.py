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

# Matching Zero or More with the Star

bat_regex_star = re.compile(r'Bat(wo)*man')
bat_3 = bat_regex_star.search('The Adventures of Batman')
print(bat_3.group())

bat_4 = bat_regex_star.search('The Adventures of Batwoman')
print(bat_4.group())

bat_5 = bat_regex_star.search('The Adventures of Batwowowowowoman')
print(bat_5.group())

# Matching One or More with the Plus
bat_regex_plus = re.compile(r'Bat(wo)+man')
bat_6 = bat_regex_plus.search('The Adventures of Batwoman')
print(bat_6.group())

bat_7 = bat_regex_plus.search('The Adventures of Batwowowowowoman')
print(bat_7.group())

bat_8 = bat_regex_plus.search('The Adventures of Batman')
print(bat_8 == None)

# Matching Specific Repetitions with Braces
ha_regex = re.compile(r'(Ha){3}')  # or {1,3}
ha_1 = ha_regex.search('HaHaHa')
print(ha_1.group())

ha_1 = ha_regex.search('Ha')
print(ha_1 == None)

# Greedy and Non-Greedy Matching
# Longest one or the shortest one
greedy_ha_regex = re.compile(r'(Ha){3,5}')
greedy_ha_1 = greedy_ha_regex.search('HaHaHaHaHa')
print(greedy_ha_1.group())

non_greedy_ha_regex = re.compile(r'(Ha){3,5}?')
non_greedy_ha_1 = non_greedy_ha_regex.search('HaHaHaHaHa')
print(non_greedy_ha_1.group())

# The Findall() Method
phone_num_regex_3 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phone_num_regex_3.findall('Cell = 415-555-9999 Work = 212-555-0000'))

# Making your own Character Classes
vowel_regex = re.compile(r'[aeiouAEIOU]')
print(vowel_regex.findall('RoboCop eats baby food. BABY FOOD'))

consonant_regex = re.compile(r'[^aeiouAEIOU]')
print(consonant_regex.findall('RoboCop eats baby food. BABY FOOD'))

# The Caret(^) and Dollar($) Sign Characters
# Beginning and End, combination causes whole string
begins_with_hello = re.compile(r'^Hello')
print(begins_with_hello.search('Hello, World!'))
print(begins_with_hello.search('He said Hello.') == None)

ends_with_number = re.compile(r'\d$')
print(ends_with_number.search('Your number is 42'))
print(ends_with_number.search('Your number is one') == None)

whole_string_number = re.compile(r'^\d+$')
print(whole_string_number.search('2174792'))
print(whole_string_number.search('3883h332') == None)

# The Wildcard Character
at_regex = re.compile(r'.at')
print(at_regex.findall('The cat in the hat sat on the flat mat with a bat.'))

# Matching Everything with Dot-Star
# It is always greedy, for non-greedy add a ?
birthday_regex = re.compile(r'Birthday Date: (.*) Birthday month: (.*)')
birthday = birthday_regex.search('Birthday Date: 17 Birthday month: January')
print(birthday.group(1))
print(birthday.group(2))

# Matching Newlines with the Dot Character
no_newline_regex = re.compile('.*')
print(no_newline_regex.search('Serve the public.\nProtect the innocent.\nUphold the law').group())

newline_regex = re.compile('.*', re.DOTALL)
print(newline_regex.search('Serve the public.\nProtect the innocent.\nUphold the law').group())

# Case-Insensitive Matching
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop').group())
print(robocop.search('ROBOCOP is part man, part machine, all cop').group())
print(robocop.search('robocop is part man, part machine, all cop').group())

# Substituting Strings with the sub() Method
names_regex = re.compile(r'Agent \w+', re.I)
print(names_regex.sub('CENSORED', 'Agent Mater gave the secret documents to Agent McQueen'))

agent_names_regex = re.compile(r'Agent (\w)\w*')
print(agent_names_regex.sub(r'\1*****', 'Agent Mater told Agent McQueen that Agent Sally knew Agent Doc was a double '
                                        'agent.'))

# Managing Complex Regexes
phone_regex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # seperator
\d{3} # first 3 digits
(\s|-|\.) # seperator
\d{4} # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)

# Combining ignorecase, dotall and verbose
some_regex_value = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
some = some_regex_value.search('Hey I am a foo')
print(some.group())
