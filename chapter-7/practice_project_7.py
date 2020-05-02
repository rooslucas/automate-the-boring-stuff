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
if month in short_months:
    if day in range(1, 31):
        if year in range(1000, 3000):
            print(f'The date {my_date} is a valid date.')
        else:
            print(f'The date {my_date} is not a valid date.')
    else:
        print(f'The date {my_date} is not a valid date.')
elif month in february:
    if year % 4 == 0 and not year % 100 == 0 and not year % 400 == 0:
        if day in range(1, 30):
            if year in range(1000, 3000):
                print(f'The date {my_date} is a valid date.')
            else:
                print(f'The date {my_date} is not a valid date.')
        else:
            print(f'The date {my_date} is not a valid date.')
    elif year % 4 != 0 and year % 100 == 0 and year % 400 == 0:
        if day in range(1, 29):
            if year in range(1000, 3000):
                print(f'The date {my_date} is a valid date.')
            else:
                print(f'The date {my_date} is not a valid date.')
        else:
            print(f'The date {my_date} is not a valid date.')
    else:
        print(f'The date {my_date} is not a valid date.')
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
