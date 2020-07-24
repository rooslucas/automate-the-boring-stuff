# Notes on chapter 11
# Imports for this chapter
import traceback

# Raising Exceptions
# raise Exception('This is the error message.')


def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))


# Using the try and except statements, you can handle errors more gracefully instead of letting the entire program crash

# Getting the Traceback as a String
def spam():
    bacon()


def bacon():
    raise Exception('This is the error message.')


spam()

try:
    raise Exception('This is the error message.')
except:
    error_file = open('error_info.txt', 'w')
    error_file.write(traceback.format_exc())
    error_file.close()
    print('The traceback info was written to error_info.txt')

# 111, The traceback info was written to error_file.txt

# Assertions
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
ages = [15, 17, 22, 26, 47, 54, 57, 73, 80, 92]
assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age.
