# Import all the necessary shit
import pyinputplus as pyip
import random
import time

# Project: How to Keep an Idiot Busy for Hours
while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break

print('Thank you. Have a nice day!')

# Project: Multiplication Quiz
number_of_questions = 10
correct_answers = 0

for question_number in range(number_of_questions):
    # Pick two random numbers:
    num_1 = random.randint(0, 9)
    num_2 = random.randint(0, 9)
    prompt = '#%s: %s x %s = ' % (question_number, num_1, num_2)

    try:
        # Right answers are handled by allowRegexes
        # Wrong answers are handled by blockRegexes, with a custom message
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num_1 * num_2)], blockRegexes=[('.*', 'Incorrect!')],
                      timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exeptions were raised in the try block.
        print('Correct!')
        correct_answers += 1

    time.sleep(1)  # Brief pause to let user see the result.
print('Score: %s / %s' % (correct_answers, number_of_questions))
