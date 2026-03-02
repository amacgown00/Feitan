# Chapter 8 - Classes 

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