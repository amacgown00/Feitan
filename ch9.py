# Chapter 8 - Classes 
def space():
    print('\n')

class Cat():
    '''Modeling a cat.'''

    def __init__(self, name, age):
        '''Initialize name and age attributes.'''
        self.name = name
        self.age = age
    
    def meow(self):
        '''Simulate a cat meowing in response to a command.'''
        print(self.name.title() + ' is now meowing.')

    def jump(self):
        '''Simulate a cat jumping.'''
        print(self.name.title() + ' jumped.')

class Restaurant():
    '''Creating a restaurant class.'''
    
    def __init__(self, restaurant_name, cuisine):
        '''Initializing restaurant name and cuisine attributes.'''
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        print(self.restaurant_name.title() + ' serves ' + self.cuisine.title() + ' food.')

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is open.')

restaurant = Restaurant('Sarma', 'Mediterranean')
print(restaurant.restaurant_name)
print(restaurant.cuisine)
ba_le = Restaurant('Ba Le', 'Vietnamese')
little_tao = Restaurant('Little Tao', 'Sichuan')
oleana = Restaurant('Oleana', 'Mediterranean')

ba_le.describe_restaurant()
little_tao.describe_restaurant()
oleana.describe_restaurant()

class User():
    '''Creating a class for users'''
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
    
    def describe_user(self):
        print('First name:  ' + self.first_name + 
              '\nLast name: ' + self.last_name + 
              '\nUsername:  ' + self.username)
        
    def greet_user(self):
        print('Hi ' + self.username + '!')

sahar = User('Sahar', 'Aftab', 'sya')
jeny = User('Jeny', 'Kwon', 'jkwonn')
hannah = User('Hannah', 'Tymann', 'atypicalginger')

sahar.describe_user()
sahar.greet_user()
space()
jeny.describe_user()
jeny.greet_user()
space()
hannah.describe_user()
hannah.greet_user()