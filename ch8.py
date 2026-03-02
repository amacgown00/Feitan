#8-15
from printing_functions import*

eames = ['DCW', 'LCW', 'Lounge', 'shell']
new_eames = []


print_models(eames, new_eames)
show_completed_models(new_eames)

def space():
    #Adding an empty line
    print('\n')


# 8-1 Message 

def display_message():
    '''Display a message about what I'm learning in the chapter on functions.'''
    print('Defining functions is a way to create a customized set of actions to use in the rest of the script without needing to repeat the code each time. \nFunctions can be defined with or without a parameter depending on whether you want to pass data through it.')

display_message()

space()

def favorite_book(title):
    print('One of my favorite books is ' + title.title())
favorite_book('The girl with the dragon tattoo')

space()

'''

Positional arguments - 
def function(pet_name, animal_type)
function('test', 'again')

Keyword arguments 
function(pet_name = 'Quigley', animal_type = 'Cat')
function(animal_type = 'cat', pet_name = 'Quigley')

Default values
def function(pet_name, animal_type = 'cat'):
function(pet_name = 'Quigley')

'''
#8-3 T-Shirt
def make_shirt(size, text):
    print('The shirt is size ' + size + ' with the words ' + text + ' printed on it.')

make_shirt('M', 'Paloma Wool')

#Keyword arguments
def make_shirt(size, text):
    print('The shirt is size ' + size + ' with the words ' + text + ' printed on it.')

make_shirt(text = 'Paloma Wool', size = 'M')

#8-4 Large Shirts

#large and medium shirt with default message 
def make_shirt(size = 'L', text = 'I love Python'):
    print('The shirt is size ' + size + ' with the words ' + text + ' printed on it.')

make_shirt()
make_shirt(size = 'M')
make_shirt(size = '24', text = 'The Row')

#8-5 Cities 
def describe_city(city, country = 'the United States of America'):
    '''Function that accepts the name of a city and its country and prints a sentence. Parameter is the default value'''
    final_destination = (city + ' is in ' + country)
    return final_destination

space()
describe_city('Paris')
describe_city('Los Angeles')
describe_city('Buenos Aires', 'Argentina')
'''
active = True

def new_job(role, company):
    #Return the job role and company you want to work at
    role_in_company = role + ' at ' + company
    return role_in_company.title()

while active:
    print('Tell me about your ideal role')
    n_role = input('Role title: ')
    n_company = input('Company: ')

    formatted_role = new_job(n_role, n_company)
    print('You would like to be a ' + formatted_role)
    
    if n_role or n_company == 'stop':
        active = False
    
#8-7 Album:
def make_album():
    artist_name = input('Artist Name:   ').title()
    album_name = input('Album Name:     ').title()
    tracks = input('Number of Tracks:   ')
    artist_album = {
        'Artist': artist_name,
        'Album': album_name,
    }
    if tracks:
        artist_album['Tracks'] = tracks
    return artist_album

frank = make_album()
mbv = make_album()
cshr = make_album()
print(frank)
print(mbv)
print(cshr)

#8-7
def new_album(artist1, album1, tracks1=''):
    test_album = {'Artist': artist1,
                  'Album': album1,
                  }
    if tracks1:
        test_album['Tracks'] = tracks1
    return test_album

music_test = True
while music_test:
    your_artist = input('Who is your favorite artist?   ')
    your_album = input('What is your favorite album?    ')
    your_tracks = input('How many tracks does the album have?   ')
    if your_artist == 'done' or your_album == 'done' or your_tracks == 'done':
        print('Complete')
        music_test = False
    else:
        al_bum = new_album(your_artist, your_album, your_tracks)
        print(al_bum)
'''

print('NEXT')
#8-10
list_magicians = ['Jeny', 'Sahar', 'Hannah T', 'Abby', 'Hannah']
def show_magicians(example_list):
    print('Magician Names:')
    for token in example_list:
        print('\t' + token)

def make_great(example_list):
    new_list = []
    while example_list:
        new_token = example_list.pop()
        final_token = new_token + ' the Great'
        new_list.append(final_token)
    while new_list:
        pluck = new_list.pop()
        example_list.append(pluck)        

make_great(list_magicians)
show_magicians(list_magicians)

space()

#8-12
def sandwich(bread, *toppings):
    print('This sandwich is on ' + bread + ' with the following toppings:')
    for topping in toppings:
        print('- ' + topping)

sandwich('foccacia', 'fresh mozzerella', 'pesto', 'tomato', 'basil')
sandwich('banh mi', 'barbeque pork', 'paté', 'picked daikon and carrots', 'cilantro','jalapeno')
sandwich('a roll', 'bacon', 'egg', 'cheese')

space()


'''
def make_album(artist, album_title):
    album_dictionary = {'Artist': artist, 'Album Title': album_title}
    return album_dictionary

active = True
while active:
    print('What is your favorite album? \nType STOP at any time to exit')
    album_name = input('Album:  ').title()
    artist_name = input('Artist:    ').title()

    final_album_dictionary = make_album(artist_name, album_name)
    if (artist_name.lower()) or (album_name.lower()) == 'stop':
        active = False
    else:
        print(final_album_dictionary)

active = True

def name(first, last):
    return (first + ' ' + last).title()

while active:
    first_name = input('What is your first name?    ')
    last_name = input('What is your last name?  ')
    
    if first_name == 'done' and last_name == 'done':
        print('Done')
        active = False
    else:
        print(name(first_name, last_name))

active = True
def poll(site, dept, name):
    person = {'Site': site, 'Department': dept, 'Name': name}
    return person

rob = poll('Chelmsford', 'MFG', 'Rob McGrath')
print(rob)

while active:
    site = input('Site: ').title()
    dept = input('Department:   ').title()
    name = input('Name: ').title()
    
    full = poll(site, dept, name)
    print(full)


site_list = []

def questions(name, q1, q2, q3, q4):
    person = {
        'Name': name, 
        'Question 1': q1, 
        'Question 2': q2, 
        'Question 3': q3, 
        'Question 4': q4,
        }
    return person

poll_live = True

while poll_live:
    live = input('New person? (y/n)   ')
    if live == 'y':
        full_name = input('Name: '  ).title()
        q1 = input('Question 1: ')
        q2 = input('Question 2: ')
        q3 = input('Question 3  ')
        q4 = input('Question 4: ')
        
        leader = questions(full_name, q1, q2, q3, q4)
        print(leader)
        new = site_list.append(leader)
        print(site_list)
    else:
        print('Complete')
        poll_live = False
'''

