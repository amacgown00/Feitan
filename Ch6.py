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

space = '\n\n'

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

friend_numbers['mike'] = (17 ** 7) % 287 

print("Mike's favorite number is: " + str(friend_numbers['mike']))

print(space)

new_mike_number = 29
friend_numbers['mike'] = new_mike_number

print(friend_numbers['mike'])

glossary = {'loop': 'code to perform an action on each element of a list',
            'boolean': 'assigning a true or false value to a variable',
            'string': 'set of characters',
            'if-elif-else': 'actions based on true/false arguments',
            'list': 'collection of elements',            
            }
print(glossary['loop'] + '\n'+
      glossary['boolean'] + '\n' +
      glossary['if-elif-else'] + '\n' +
      glossary['list'] + '\n' +
      glossary['string']
      )