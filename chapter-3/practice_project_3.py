# Practice project from chapter 3

# The Collatz Sequence
def collatz(number):
    even = number % 2 == 0
    if even:
        number = number // 2
    elif not even:
        number = 3 * number + 1
    return number


print(collatz(4))

print('Enter number: ')
number = int(input())
not_one = number != 1

while not_one:
    number =  collatz(number)
    print(number)
    not_one = number != 1