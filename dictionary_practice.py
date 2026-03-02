def space():
    print('\n')
    
practice_dictionary = {}

#function to add new keypairs 
add_name = input('Name:     ').title()
add_username = input('Username:     ')

practice_dictionary['name'] = add_name
practice_dictionary['username'] = add_username

print(practice_dictionary)
    

active = True

def name(first, last):
    return (first + ' ' + last).title()

while active:
    first_name = input('What is your first name?    ')
    last_name = input('What is your last name?  ')
    
    if not (first_name and last_name) == 'done':
        print('Done')
        active = False
    else:
        print(name(first_name, last_name))