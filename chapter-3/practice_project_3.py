# Practice project from chapter 3


# The Collatz Sequence
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


try:
    print('Enter number: ')
    number_input = int(input())

    while number_input != 1:
        number_input = collatz(number_input)
        print(number_input)

except ValueError:
    print("You must enter an integer")
