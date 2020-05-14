# Practice projects of chapter 8
# Import important shizzle
import pyinputplus as pyip
import time

# Practice project 1: Sandwich maker
price = 0

bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'])
if bread_type == 'sourdough':
    price += 1.50
else:
    price += 1

protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
if protein_type == 'tofu':
    price += 1
else:
    price += 2

# Ask for cheese
cheese_question = pyip.inputYesNo('Do you want cheese on your sandwich?\n')
if cheese_question == 'no':
    cheese_type = 'none'
else:
    cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
    price += 1.50

# Ask for toppings
toppings_question = pyip.inputYesNo('Do you want toppings on your sandwich?\n')
if toppings_question == 'no':
    toppings_type = 'none'
else:
    toppings_type = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'])
    price += 0.50

# Ask how many sandwiches
number = pyip.inputInt('How many sandwiches do you want?\n')
price = price * number


# Write function to display order
def display_order(order):
    for type, answer in order.items():
        print(type + ': ' + str(answer))


order = {'number of sandwiches': number, 'bread': bread_type, 'protein': protein_type, 'cheese': cheese_type, 'topping': toppings_type}
print('Is this your order?')
display_order(order)
pyip.inputYesNo()

# Display total price
print(f"Your total price is €{price}{0}")