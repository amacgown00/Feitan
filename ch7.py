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

prompt = 'What is your favorite color?'
message = ''
while message != 'none':
    message = input(prompt)
    if message != 'none':
        print(message)

electric = 'Maria (210)-485-2325 eversource'

active = True
movies = []
answer = ''
question = 'What are your favorite movies?  '

while True:
    answer = input(question).strip()
    if answer.lower() in ['no more', 'none']:
        break
    movie = answer.title()
    if movie not in movies:
        movies.append(movie)
    if len(movies) == 1:
        print(f'My favorite movie is {movies[0]}')
    elif len(movies) == 2:
        print(f'My favorite movies are {movies[0]} and {movies[1]}')
    else:
        print(f'My favorite movies are {', '.join(movies[:-1])}, and {movies[-1]}')
'''

#7-4
'''
toppings = 'What toppings would you like on your pizza? '
active = True
while active:
    answer = input(toppings)
    if answer == ('no more' or "that's all"):
        print('Your pizza will be our shortly.')
        active = False
    else:
        print('Adding ' + answer + ' to your pizza.')

#7-5
age = 'How old are you? '
ticket_price = ''
while ticket_price == '':
    ticket_price = input(age)
    ticket_price = int(ticket_price)
    if ticket_price < 3:
        print('The ticket is free.')
    elif ticket_price < 12:
        print('Your ticket is $10.')
    else:
        print('Your ticket is $15.')

print('\n')

#7-6 Three Exits
ticket = 'Do you have a ticket?     '
based_test = 'Who are you here to see?  '
artists = ['Francois X', 'Kilopatrah Jones', 'cotton']
second_question = ''
answer = ''
while answer == '':
    answer = input(ticket)
    if answer.lower() == 'yes':
        second_question = input(based_test)
        if second_question == "I don't know":
            print('Step to the left please')
            break
        if second_question in artists:
            print('You can head in')
        else:
            break
    else:
        second_question = input(based_test)
        if second_question in artists:
            print('You can head in, tickets are on the left.')
        else:
            break

ticket = 'Do you have a ticket?     '
based_test = 'Who are you here to see?  '
artists = ['Francois X', 'Kilopatrah Jones', 'cotton']
second_question = ''
answer = ''

active = True
while active:
    answer = input(ticket)
    if answer == 'yes':
        second_question = input(based_test)
        if based_test == "I don't know":
            print('Please step to the left')
            active = False
        if based_test in artists:
            print('Go ahead and head in')
            active = False
    if answer == 'no':
        second_question = input(based_test)
        if second_question in artists:
            print('Alright, head on in')
            active = False
        else:
            print('Step to the left')
            active = False
'''

