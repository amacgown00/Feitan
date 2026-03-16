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
        
quigley = Cat('Quigley', 5)
print("My cat's name is " + quigley.name + '.')
print('He is ' + str(quigley.age) + ' years old.')

quigley.meow()
quigley.jump()

space()
'''
9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
    Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
    '''

class Restaurant():
    '''Creating a restaurant with different cuisines.'''
    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize name and cuisine types.'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print('The restaurant is called ' + self.restaurant_name + ' and it serves ' + self.cuisine_type + ' food.')
    
    def open_restaurant(self):
        print(self.restaurant_name + ' is open.')
        
    def read_customers(self):
        print(self.restaurant_name + ' has served ' + str(self.number_served) + ' customers.')
    
    def set_number_served(self, customer_number):
        '''Set the number of customers to the given value.'''
        self.number_served = customer_number
        
    def increment_number_served(self, add_customers):
        '''Add the given number to the customer numbers.'''
        self.number_served += add_customers
        

teado = Restaurant('TeaDo', 'boba')
print('TeaDo has served ' + str(teado.number_served) + ' people.')
teado.number_served = 100
print('TeaDo has served ' + str(teado.number_served) + ' people.')
teado.set_number_served(500)
print('TeaDo has served ' + str(teado.number_served) + ' people.')

teado.increment_number_served(30)
teado.read_customers()

space()


dorsia = Restaurant('Dorsia', 'French',)
print(dorsia.restaurant_name + ' is the name of the restaurant.')
print(dorsia.restaurant_name + ' serves ' + dorsia.cuisine_type + ' food.')

dorsia.describe_restaurant()
dorsia.open_restaurant()

        

'''
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.
'''
sarma = Restaurant('Sarma', 'Mediterranean')
prairie_fire = Restaurant('Prairie Fire', 'American')
byblos = Restaurant('Byblos', 'Lebanese')

sarma.describe_restaurant()
prairie_fire.describe_restaurant()
byblos.describe_restaurant()
space()

class Car():
    '''Attempt to represent a car.'''
    
    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        '''Print a statement showing the car's mileage.'''
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')
    
    def update_odometer(self, mileage):
        '''
        Set the odometer to a given value.
        Reject the change if it attempts to roll the odometer back.
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
            
    def increment_odometer(self, miles):
        '''
        Add the given amount to the odometer reading. 
        '''
        self.odometer_reading += miles
    
my_new_car = Car('Porsche', 'Boxer', 1975)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
space()

my_new_car.odometer_reading = 50
my_new_car.read_odometer()
space()
my_new_car.update_odometer(20000)
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

'''
9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.'''

class User:
    '''Capturing user profile information.'''
    
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.login = 0
    
    def describe_user(self):
        print(self.first_name.title() + ' ' + self.last_name.title() + "'s username is " + self.username)
    
    def greet_user(self):
        print('Hi ' + self.first_name.title())
        
    def increment_login_attempts(self):
        '''Increments login value by 1.'''
        login_attempt = ''
        print('Hi ' + self.first_name.title())
        space()
        while login_attempt != self.password:
            login_attempt = str(input('Enter password:  '))
            
            if login_attempt != self.password:
                self.login += 1
                print('Login unsuccessful attempts:  ' + str(self.login))
            else:
                print('\nLogin successful.')
    def reset_login_attempt(self):
        '''Resets the login value to 0'''
        reset_password = input('Would you like to reset your password? (Y/N)    ')
        if reset_password.lower() == 'y':
            self.login = 0
            new_password = str(input('Enter new password:   '))
            print('Password reset successful.\nNew password:    ' + new_password)
            print('Login attempts:  '  + str(self.login))

        else:
            print('Login attempts:  ' + str(self.login))
            space()           

sahar = User('sahar', 'aftab', 'sahar_ken', 'smith2018')
sophie = User('sophie', 'cox', 'swxpt', 'oldp')
jeny = User('jeny', 'kwon', 'jkwon', 'smith2020')

sahar.describe_user()
sahar.greet_user()
space()
sophie.describe_user()
sophie.greet_user()
space()
jeny.describe_user()
jeny.greet_user()
space()
sahar.increment_login_attempts()
space()
sahar.reset_login_attempt()



'''9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.'''