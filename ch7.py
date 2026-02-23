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
'''
'''
prompt = 'What pizza topppings would you like?      '
keep_asking = True
answer = ''
while answer != 'quit':
    answer = input(prompt)
    if answer == 'quit':
        print('Your pizza will be out shortly.')
        keep_asking = False
    else:
        print(answer)
'''
'''active = True
answer = '' 
different_answer = ''
list = []
question = 'What movies do you like?    '
second_q = 'Anything else?  '

while active:
    answer = input(question)
    if answer not in list:
        list.append(answer)
    for response in list:
        if list[0] != '' and list[1] == '':
            print('My favborite movie is ' + response)
        elif list[1] != '':
            print('My favorite movies are ' + list[0] + ' and ' + list[1] + '.')
        else:
            set_3 = list[0] + ', ' + list[1] + ', and '

            print('My favorite movie are ' )
    if list[1] == '':
        print('My favorite movie is ' + answer + list[-1:])
    
        


answer = 'test'
while active:
    if 
different_answer 


active = True
question = 'What would you like?    '
answer = ''

while active:
    answer = input(question)

    if answer == ('nothing' or 'done').lower():
        print('Finished')
    else:
        print(answer)

first_answer = ''
second_answer = ''
question = 'Are your favorite fruits?   '
keep_asking = True

while keep_asking:
    first_answer = input(question)
    
    if first_answer != 'done' or 'stop' or '''

'''
active = True
movies = []
question = 'What are your favorite movies?  '

while active:
    answer = input(question)
    if answer not in movies and answer != ("that's all" or 'no more'):
        movies.append(answer.title())
    one_movie = str(movies[-1:])
    if len(movies) == 1:
        mov_1 = str(movies[0])
        print('My favorite movie is ' + mov_1)
        continue
    if len(movies) == 2:
        mov_1 = str(movies[0])
        mov_2 = str(movies[1])
        print('My favorite movies are ' + mov_1 + ' and ' + mov_2)
        continue
    if len(movies) >= 3:
        mov_1 = str(movies[0])
        mov_2 = str(movies[1])
        for movie in movies:
            incorporate = str(movies[-1:])
            three_or_more = 'My favorite movies are ' + mov_1 + ', ' + mov_2
            last = ', and ' + incorporate
            movie_list = three_or_more + last
            print(movie_list)
            three_or_more = 'My favorite movies are ' + mov_1 + ', ' + mov_2 + ', ' + incorporate
            continue
    if answer == 'no more' or "that's all":
        active = False 
        '''


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


question = input('What toppings would you like?    ')
answer = ''
while answer != 'no more':
    answer= input(question)
    if message != 'no more':
        print('Your pizza has ' + answer)