# Practice project Date Detection
import re

# Create the regex
date_detection = re.compile(r'''(
(\d{2})
(\s|/|\.)
(\d{2})
(\s|/|\.)
(\d{4})
)''', re.VERBOSE)

print("Enter your date in the format dd/mm/yyyy:")
my_date = input()

# Store date in variables
day = int(date_detection.search(my_date).group(2))
month = date_detection.search(my_date).group(4)
year = int(date_detection.search(my_date).group(6))

# Create lists with months
short_months = ['04', '06', '09', '11']
long_months = ['01', '03', '05', '07', '08', '10', '12']
february = ['02']

# Check if date is a valid date
# Check the months with 30 days
if month in short_months:
    if day in range(1, 31):
        if year in range(1000, 3000):
            print(f'The date {my_date} is a valid date.')
        else:
            print(f'The date {my_date} is not a valid date.')
    else:
        print(f'The date {my_date} is not a valid date.')

# Check the month february
elif month in february:
    is_leap_year = year % 4 == 0 and not year % 100 == 0
    if is_leap_year:
        if day in range(1, 30):
            if year in range(1000, 3000):
                print(f'The date {my_date} is a valid date.')
            else:
                print(f'The date {my_date} is not a valid date.')
        else:
            print(f'The date {my_date} is not a valid date.')
    elif year % 4 != 0 or year % 100 == 0:
        if day in range(1, 29):
            if year in range(1000, 3000):
                print(f'The date {my_date} is a valid date.')
            else:
                print(f'The date {my_date} is not a valid date.')
        else:
            print(f'The date {my_date} is not a valid date.')
    else:
        print(f'The date {my_date} is not a valid date.')

# Check the months with 31 days
elif month in long_months:
    if day in range(1, 32):
        if year in range(1000, 3000):
            print(f'The date {my_date} is a valid date.')
        else:
            print(f'The date {my_date} is not a valid date.')
    else:
        print(f'The date {my_date} is not a valid date.')
else:
    print(f'The date {my_date} is not a valid date.')

# Practice project 2: Strong Password Detection

# Length regex
length_regex = re.compile(r'.{8,}')

# Digit regex
digit_regex = re.compile(r'[0-9]')

# Casing regex
lower_casing_regex = re.compile(r'[a-z]')
upper_casing_regex = re.compile(r'[A-Z]')

print("Enter your password:")
my_password = input()

# Run through the regexes
long_enough = length_regex.search(my_password) is not None
digit_included = digit_regex.search(my_password) is not None
lower_case_included = lower_casing_regex.search(my_password) is not None
upper_case_included = upper_casing_regex.search(my_password) is not None

if long_enough and digit_included and lower_case_included and upper_case_included:
    print("You created a strong password.")
elif not long_enough:
    print("The minimum number of characters is eight, otherwise your password isn't great...")
elif not digit_included:
    print("Babidiboo, you need a digit too...")
elif not lower_case_included or not upper_case_included:
    print("You need lower and upper, otherwise you ain't getting supper...")
else:
    print("You failed so hard, please begin from the start...")

# Shorter code but less fun
# if not long_enough:
#     print("The minimum number of characters is eight, otherwise your password isn't great...")
# elif not digit_included:
#     print("Babidiboo, you need a digit too...")
# elif not lower_case_included or not upper_case_included:
#     print("You need lower and upper, otherwise you ain't getting supper...")
# else:
#     print("You created a strong password.")