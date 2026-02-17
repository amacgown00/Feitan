media = {'Film': 'Tarkovsky', 'anime': 'Jujutsu Kaisen'}
my_favorite_media = media['Film']
print('My favorite director is ' + my_favorite_media)

media['Museum'] = 'Museum of Modern Art'
media['Book'] = 'Hemlock Grove'
print(media)

hxh_char = {}
hxh_char['Killua'] = 'transmuter'
hxh_char['Gon'] = 'enhancer'
hxh_char['Chrollo'] = 'specialist'
hxh_char['Kurapika'] = 'conjurer'
print(hxh_char['Kurapika'])

kurta_eyes = 'red'
if kurta_eyes == 'red':
    hxh_char['Kurapika'] = 'specialist'
    print("When Kurapika's eyes are " + kurta_eyes + ", he becomes a " + hxh_char['Kurapika'] + '.\n\n\n')

space = '\n'

friend = {
    'first_name' : 'Sahar',
    'last_name' : 'Aftab',
    'age' : '29',
    'city' : 'Yonkers',   
}
print(friend['first_name'] +
      " " +
      friend['last_name'] +
      ' ' +
      friend['age'] + 
      ' ' + 
      friend['city'] + '\n'
      )

friend_numbers = {
    'sahar' : '24',
    'jeny' : '73',
    'hannah' : '36',
    'mike' : '',
}
friend_numbers['mike'] = ((17 ** 7) % 287) / (4 ** -30) 
print("Mike's favorite number is: " + str(friend_numbers['mike']))
print(space)
new_mike_number = ((17 ** 7) % 287) 
friend_numbers['mike'] = new_mike_number
print(friend_numbers['mike'])
print(space)

glossary = {'loop': 'code to perform an action on each element of a list',
            'boolean': 'assigning a true or false value to a variable',
            'string': 'set of characters',
            'if-elif-else': 'actions based on true/false arguments',
            'list': 'collection of elements',            
            }
print('loop: ' + glossary['loop'] + '\n'+
      'boolean: ' + glossary['boolean'] + '\n' +
      'if-elif-else: ' + glossary['if-elif-else'] + '\n' +
      'list: ' + glossary['list'] + '\n' +
      'string: ' + glossary['string']
      )

# items() does both the key and the value
for fren, num in friend_numbers.items():
    print(fren.title() + ": " + str(num))

print(space)
favorite_poros = {'Claire': 'Benzyl Ultra',
                   'Brett': 'R550', 
                   'Joe': 'AAV', 
                   'Ryan': 'R150', 
                   'Nick': 'FcXP', 
                   'Tyler': 'EP150', 
                   'Rob' : 'A220',
                   'Matt': 'FcXP'}
poros_friends = ['Joe', 'Nick', 'Rob']


"""Looping all the keys in the dictionary
    If any of those names match the smaller list"""

for name in favorite_poros.keys():
    print(name)
    if name in poros_friends:
        print(name + "'s favorite POROS material is " + favorite_poros[name])
print(space)



#sorted() to return the original order 
for name in sorted(favorite_poros.keys()):
    print(name + ', thank you for taking the poll.')
print(space)



# .values() method to return the complete list of values
for poros in favorite_poros.values():
    print(poros)
print(space)

#set  to find a list of unique values
print('This is a list of the materials people like without repeats.')
for material in set(favorite_poros.values()):
    print(material)
print(space)
print(space)

'''
favorite_poros = {'Claire': 'Benzyl Ultra',
                   'Brett': 'R550', 
                   'Joe': 'AAV', 
                   'Ryan': 'R150', 
                   'Nick': 'FcXP', 
                   'Tyler': 'EP150', 
                   'Rob' : 'A220',
                   'Matt': 'FcXP'}
'''

for friend, product in favorite_poros.items():
    print(friend + "'s favorite material is " + product)

print(space)

favorite_poros['Ragna'] = 'HIC'
favorite_poros['Colleen'] = 'XQ'
favorite_poros['Kevin'] = 'AAV9'

for friend, product in favorite_poros.items():
    print(friend + "'s favorite material is " + product)



# .item() to loop the key-value pair
print(space)
rivers = {'Nile': 'Egypt', 'Seine': 'France', 'Thames': 'England'}
for river, country in rivers.items():
    print('The ' + river + ' runs through ' + country)
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)

new_poros_list = []
for person, product in favorite_poros.items():
    new_for_poros_list = new_poros_list.append(person)


new_poros_list.append('Riley') #Adding new person
new_poros_list.append('Sean') #Adding new person

for v in new_poros_list:
    if v in favorite_poros:
        print('Hi ' + v + ', thank you for responding.')
    else:
        print('Hi ' + v + ', please take this poll.')



#Dictionaries inside a list
quigley = {'species': 'cat',
           'color': 'blue-point',
           'age': '5'}
juniper = {'species': 'cat', 'color': 'seal-point', 'age': '4'}

my_pets = [quigley, juniper]
for cat in my_pets:
    print(cat)

for cat in range(5):
    new_cat = {'species': 'ragdoll','color': 'lynx-point', 'age': '0'}
    my_pets.append(new_cat)

for cat in my_pets[:2]:
    print(cat)
print('...')

print('Total number of pets I have: ' + str(len(my_pets)))

for cat in my_pets:
    if cat['species'] == 'ragdoll':
        cat['eye color'] = 'green'
    else:
        cat['eye color'] = 'blue'
    for k, v in cat.items():
        print('Key: ' + k)
        print('\nValue: ' + v)
    print('\n*****')


#List within a dictionary
life_at_age = {
    'age': '10',
    'home': 'Beverly, MA',
    'school': 'Brookwood',
    'Hobbies': ['Reading Percy Jackson books', 'Neopets', 'karate']
}

print('This is what my life looked at age ' + life_at_age['age'] + ':')
print('I lived in ' + life_at_age['home'] + ' and went to ' + life_at_age['school'] + '.\nMy hobbies were:')
for hobby in life_at_age['Hobbies']:
    print('\t' + hobby)