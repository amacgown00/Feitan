'''
-   input() function creates strings 

-   +=  takes the value from one variable and adds it to the next

- int() function    converts string numbers into numerical values

- % modulo 

number = input('Is this number even or or odd?  ')
number = int(number)

if number % 2 == 0:
    print('\nEven')
else:
    print('\nOdd')
    


#7-1
rental = input('What kind of car would you like?    ')
if rental.lower() == 'subaru':
    print('Let me see if I can find you a crosstrek.')
else:
    print('Let me see if I can find you a ' + rental.title())

#7-2
host = int(input('How many are in your party?   '))
if host > 8:
    print('Your expected wait time is 40 minutes.')
else:
    print('Your table is ready')

#7-3
multiple = int(input('Tell me your favorite number  '))
if multiple % 10 == 0:
    print('This number is a multiple of 10.')
else:
    print('This number is not a multiple of 10')



prompt = "\nTell me something and I'll repeat it back to you:"
prompt += "\nEnter 'quit' to end the program.   "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
'''

prompt = 'What is your favorite color?'
message = ''
while message != 'none':
    message = input(prompt)
    if message != 'none':
        print(message)

electric = 'Maria (210)-485-2325 eversource'
