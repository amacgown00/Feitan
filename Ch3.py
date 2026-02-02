#!/usr/bin/env python3
#Chapter 3. Lists
#Actually doing the homework for once 

print("3-4") 
guest_list = ['Future Husband', 'Zohran Mamdani', 'Anderson Cooper', 'Zodiac Killer']

for guest in guest_list:
    print("Dear "+guest+", please join me for dinner.\n")

print("\n\n3-5\n")

print("1\n")
flake = guest_list.pop(-1)
print("The "+flake.upper()+" said he's busy and can't make it to my dinner.\n")

print('2\n')
bff = 'Friedrich Nietzsche'
guest_list.insert(2, bff)

print("Dear " + guest_list[0]+", I cordially extend my invitation to join me for dinner at my place of residence.\n")

#3
print('3\n')
for guest in guest_list:
    print("Dear " + guest + ", I would like to cordially invite you to join me for dinner at my place of residence.\n")

print("\n\n3-6 More Guests\n")
print("Dear " + guest_list[0] + ", I have found a bigger dining table and will be inviting more guests.\n\n")

for guest in guest_list:
    print("Dear " + guest + ", I have found a different dining table that can accommodate more guests, and I will be inviting 3 more people.\n")

new_x, new_y, new_z = "Frank Costanza", "Al Gore", "Warren Buffett"

guest_list.insert(0, new_x)
guest_list.insert(2, new_y)
guest_list.append(new_z)

line2 = '\n\n'
line1 = '\n'
#String interpolation operator ("%s") % (variable)
for guest in guest_list:
    print("Dear %s, I would like to cordially invite you to a dinner party I am hosting.%s" % (guest, line1))
    
print('%s3-7%s' % (line2, line1))
print('I can only invite 2 people to dinner%s' % line1)


new_index_list = (list((range(len(guest_list)))))
print(new_index_list)

for rain_check in guest_list[0:5]:
    rain_check = guest_list.pop()
    print("Dear %s, unfortunately the table I bought will not arrive in time and I don't have enough space. Are you available to come to my dinner party next week instead?\n" % rain_check)
    print(guest_list)
    
    print("Dear %s, I've had to cut down on the headcount because of my table situation, but you are still invited.\n" % guest_list)
    
print(guest_list)

#list.insert()
"""to print the index. it needs to be (index, VARIABLE), then just print the index even if you don't use it
    for index in enumerate(guest_list):
    print(index)"""
    
#Finding the value of index 1
for second_guest in guest_list:
    if second_guest is guest_list[1]:
        print(second_guest)

#ENUMERATE IS WHEN YOU WANT TO FIND THE INDEX 
"""Print the index of a certain value: 
    1. (index, VARIABLE) 
    2. then just print the index even if you don't use the variable"""

for index, unknown in enumerate(guest_list):
    if unknown == "Future Husband":
        print(index)

#Make a list of the index numbers of a list 
    """1. Get the length of the guest list - len(list_name)
    2. Then the range of that number to get all the separate numbers - range(len(list))
    3. Finally the list out the numbers in the range - 
    list(range(len(list_name)))"""
    
separate_list = list(range(len(guest_list)))
print(separate_list)

#3-8
destinations = ['Berlin', 'Damascus', 'Alabama','Paris, Texas', 'Reykjavik', 'Saigon', 'Morocco', 'somewhere not many people have been to']

string_destinations = str(destinations)
og_list = 'Original list: ' + str(destinations)
print(og_list)
print('\nSorted list: ' + str(sorted(destinations)))
print('\nThe unchanged original list: ' + string_destinations)

#function(variable, argument)
print(sorted(destinations, reverse=True))
print(destinations)

destinations.reverse()
print(destinations)

destinations.reverse()
print(destinations)

destinations.sort()
print(destinations)

destinations.sort(reverse=True)
print(destinations)

#3-9

guest_num = str(len(guest_list))
junaloo = "I am inviting " + guest_num + " people to dinner."
print(junaloo)

