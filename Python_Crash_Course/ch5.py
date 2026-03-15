shows = ['Hunter x Hunter', 'Death Note', 'Naruto', 'One Piece', 'Jujutsu Kaisen']
new_show = 'Dandadan'
if new_show not in shows:
    print(new_show + " is on my watch list.")

#5-1
my_cat= 'Quigley'
print('Is one_cat == "Quigley"? I predict True.')
print(my_cat== 'Quigley')

print('\nIs my cat == "Chamkila"? I predict false.')
print(my_cat == 'Chamkila')

#2 false because case sensitive
brand = 'Hermes'
print("Is brand == 'Hermes'? I predict False")
print(brand == 'hermes')

#3 
color = 'pink'
print("Is my sweatshirt color == 'pink'? I predict True")
print(color == 'pink')

#4 
my_age = 29
your_age = 30
min_age = 29
age_test = (my_age and your_age)
print('We can go if one of us is at least 29')
print(age_test > min_age)

print('\n')

#5 Can I go to the party? 
dad = "yes"
mom = "No"
print('You can only go to the party if both parents say yes.\n')
if (mom and dad).lower() == 'yes':
    print('You can go to the party.')
    print('We get the coolest parents of the year award')
else:
    print("You can't go to the party.")

print('\n\n') 

#6 

candy_1 = "Nerds Gummy Clusters"
candy_2 = "Haribo Peach Gummies"

print('Do I like Haribo Peach Gummies?')
print((candy_1 or candy_2) == 'Nerds Gummy Clusters' or 'Haribo Peach Gummies')

if (candy_1 or candy_2).lower() == ('nerds gummy clusters' or 'haribo peach gummies'):
    print('I like this candy\n\n')

#7#

fav_anime = 'Jujutsu Kaisen'
relationship_test = ''
if relationship_test != fav_anime:
    print("You don't understand me at all; you don't even know what my favorite anime is.\n\n")

#8
cat_breeds = ['ragdoll', 'siamese', 'abyssinian', 'savannah']
your_cat = 'Nebelung'

if your_cat not in cat_breeds:
    print('Your cat is a ' + your_cat) 

#9

mollusk = 'sea'
print('does my head hurt?')
print(mollusk != 'frog')

#10
print(mollusk != 'sea')

alien_color = "blue"
if alien_color == "green":
    print('The player has earned 5 points.')
if alien_color == "blue":
    print('The player has earned 5 points.')

if alien_color == 'green':
    print('The player earned 5 points for shooting the alien')
else:
    print('The player just earned 10 points.')


random = 7928 % 373
if random < 50:
    print("I can't do mental math")
else:
    print("It doesn't matter that I'm right, they'll still think I'm dumb")

5-4
if 39**4 > 1_000_000_000:
    print("I'm going to die alone")
else:
    print("The Donnie Darko dvd I have is scratched and there's nothing I can do about it\n\n")

5-5
alien_color = 'green'
if alien_color == 'green':
    print('The player earned 5 points.')
elif alien_color == 'yellow':
    print('The player earned 10 points.')
elif alien_color == 'red':
    print('The player has earned 15 points')
    
alien_color = 'yellow'
if alien_color == 'green':
    print('The player earned 5 points.')
elif alien_color == 'yellow':
    print('The player earned 10 points.')
elif alien_color == 'red':
    print('The player has earned 15 points')

alien_color = 'red'
if alien_color == 'green':
    print('The player earned 5 points.')
elif alien_color == 'yellow':
    print('The player earned 10 points.')
elif alien_color == 'red':
    print('The player has earned 15 points\n\n')
    
5-6 
age = 93
if age < 2:
    print('The person is a baby')
elif 2 <= age < 4:
    print('The person is a toddler')
elif 4 <= age < 13:
    print('The person is a kid')
elif 13 <= age < 20:
    print('The person is a teenager')
elif 20 <= age < 65:
    print('The person is an adult')
else:
    print('The person is an elder\n\n')

favorite_fruits = ['pomegranates', 'raspberries', 'strawberries']

fruit_1 = 'pomegranates'
if 'pomegranates' in favorite_fruits:
    print('Wow, you really like ' + fruit_1)

fruit_2 = 'raspberries'
if fruit_2 in favorite_fruits:
    print('Wow, you must really like' + fruit_2)

fruit_3 = 'strawberries'
if fruit_3 in favorite_fruits:
    print('Wow, you must really love ' + fruit_3)

fruit_5 = 'blueberries'
if fruit_5 in favorite_fruits:
    print('Wow, you must really love ' + fruit_5)
else:
    print('I do not like ' + fruit_5 + ' as much as I like the other fruits\n\n')

boba_toppings = ['aloe', 'yogurt pop', 'crystal', 'boba']
boba_order = ['aloe', 'yogurt pop']

for toppings in boba_order:
    if toppings in boba_toppings:
        print('Adding ' + toppings + ' to your drink.')
    else:
        print('Sorry, we are all out of ' + toppings)

print('Number 85 is ready\n\n')

#5-9

usernames = []
if usernames:
    for user in usernames:
        print('Hello ' + user)
else:
    print('We need to get some new users\n\n')


#5-10
current_users = ['janerubyjane', 'blonded', 'banksy', 'paloma_wool', 'outlier']
new_users = ['kotn', 'jacquemus', 'glossier', 'hypebae', 'blonded', 'paloma_wool']

for user in new_users:
    if user in current_users:
        print(user + ' has already been taken. Please enter a new username.')
    else:
        print(user + ' is available\n\n')
    
#5-11
numbers = ['1','2','3','4','5','6','7','8','9']
for number in numbers:
    if number == '1':
        print(number + "st")
    elif number == '2':
        print(number + 'nd')
    elif number == '3':
        print(number + 'rd')
    else:
        print(number + 'th')


        













#