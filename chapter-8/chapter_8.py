# Notes on chapter 8 about input validation
# import as ... makes the typing shorter
import pyinputplus as pyip

while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use numeric digits')
        continue
    if age < 1:
        print("Please enter a positive number, we don't time travel here.")
        continue
    break

print(f'Your age is {age}.')
last_age = age - 1
print(f'Last year you where {last_age} years, you are getting old.')

# # The pyinputplus module
# response = pyip.inputNum()
# response_2 = pyip.inputInt(prompt='Enter a number: ')
# # Wanna know more use help(pyip.inputChoice)
#
# # The min, max, greaterThan, and lessThan Keyword Arguments
# response_3 = pyip.inputNum('Enter num: ', min=4)
# response_4 = pyip.inputNum('Enter num: ', greaterThan=4)
# response_5 = pyip.inputNum('Enter num: ', min=4, lessThan=6)
#
# # The blank Keyword Argument
# # Makes input optional
# response_6 = pyip.inputNum(blank=True)

# The limit, timeout, and default Keyword Arguments
response_7 = pyip.inputNum(limit=2)
response_8 = pyip.inputNum(timeout=10)
response_9 = pyip.inputNum(limit=2, default='N/A')  # Makes sure there is something stored in variable
print(response_9)
