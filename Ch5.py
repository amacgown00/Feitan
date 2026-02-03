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









"""
me = "Me: "
boy = "Boy: "
typical_boy_response = ['Only if you want', "Don't leave early, I don't want to interrupt", "I can't call, I'm gaming"]
recover = "But I can"
reschedule = ['tomorrow', 'later tonight', 'this weekend']
his_actual_response = 'Only if you want'

print(me + 'Can we call tonight?')
print(boy + his_actual_response)
if his_actual_response in typical_boy_response:
    print(me + "Let's just not call then")
"""


#if you ask a boy to call and he says 1, 2, 3, and doesn't add a reschedule, then you 






