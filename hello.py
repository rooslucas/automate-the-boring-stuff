# This program says hallo and asks for my name.
print ('hallo world')
print ('Whats your name?') #ask for their name
myName = input()
print ('It is good to meet you, ' + myName)
print ('The lenght of name is:')
print (len(myName))
print ('What is your age?') #ask for their age
myAge = input()
print ('You will be ' + str(int(myAge)+ 1) + ' in a year.')
print ('What is your height?') #ask for their height
myHeight = input()
print ('So you are ' + str(float(myHeight)) + ' metres long')
print ('do you want to know your height in inches?')
answer = input()
if answer == 'yes':
    print ('your height in inches is ' + str(float(myHeight) / 0.0245) + ' inches')
else:
    print ('That is okay, have a nice day')
