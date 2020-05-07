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

print(day)
print(month)
print(year)

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
    if year % 4 == 0 and not year % 100 == 0:
        if day in range(1, 30):
            if year in range(1000, 3000):
                print(f'The date {my_date} is a valid date.')
            else:
                print(f'The date {my_date} is not a valid date.')
        else:
            print(f'The date {my_date} is not a valid date.')
    elif year % 4 != 0 and year % 100 == 0:
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
if (length_regex.search(my_password) is not None) & (digit_regex.search(my_password) is not None) & (
        lower_casing_regex.search(my_password) is not None) & (upper_casing_regex.search(my_password) is not None):
    print("You created a strong password.")
elif length_regex.search(my_password) is None:
    print("The minimum number of characters is eight, otherwise your password isn't great...")
elif digit_regex.search(my_password) is None:
    print("Babidiboo, you need a digit too...")
elif (lower_casing_regex.search(my_password) is None) | (upper_casing_regex.search(my_password) is None):
    print("You need lower and upper, otherwise you ain't getting supper...")
else:
    print("You failed so hard, please begin from the start...")
