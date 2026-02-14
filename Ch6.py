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
    print("When Kurapika's eyes are " + kurta_eyes + ", he becomes a " + hxh_char['Kurapika'] + '.')
    