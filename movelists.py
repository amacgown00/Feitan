#Trying to work with lists. Appending and moving things around 

def space():
    print('\n')

favorite_colors = ['blue', 'charcoal', 'sage']

my_colors = []

while favorite_colors:
    moving_colors = favorite_colors.pop()

    print('Moving ' + moving_colors + ' to the new list.')
    my_colors.append(moving_colors) #Important moving part

print('Here is the new list:')
for color in my_colors:
    print('\t' + color)

space()



def move(old_list, new_list):
    switch_word = old_list.pop()
    print('Moving ' + switch_word)
    new_list.append(switch_word)

restaurant = ['Prairie Fire', 'Sarma']
favorite_restaurants = []

while restaurant:
    move(restaurant, favorite_restaurants)
print('Favorite restaurant list')
for place in favorite_restaurants:
    print('\t' + place)
space()
#it worked 

person_dictionary = {}

def new_poll():
    name = input('Name: ')
    dept = input('Department:   ')
    question_1 = input('What are your top 1-2 inhibitors?       ')
    question_2 = input('What are your blocks with SFLMS?        ')
    question_3 = input('What do you need support on to fix the current state?       ')
    question_4 = input('What routine communication would be helpful?        ')
    person = {'Question 1': question_1,
              'Question 2': question_2,
              'Question 3': question_3,
              'Question 4': question_4,
              }
    catchall = [name, dept, person]
    
    return catchall

rob = new_poll()
print(rob)

