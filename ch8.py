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

active = True

def new_job(role, company):
    '''Return the job role and company you want to work at'''
    role_in_company = role + ' at ' + company
    return role_in_company.title()

while active:
    print('Tell me about your ideal role')
    n_role = input('Role title: ')
    n_company = input('Company: ')

    formatted_role = new_job(n_role, n_company)
    print('You would like to be a ' + formatted_role)