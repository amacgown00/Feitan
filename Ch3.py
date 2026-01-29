#!/usr/bin/env python3
#Chapter 3. Lists
#Actually doing the homework for once 

#3-4    
guest_list = ['Future Husband', 'Zohran Mamdani', 'Anderson Cooper', 'Zodiac Killer']

for guest in guest_list:
    print("Dear "+guest+", please join me for dinner.\n\n\n\n")

#3-5 
flake = guest_list.pop(-1)
print("The "+flake.upper()+" said he's busy and can't make it to my dinner.\n")

bff = 'Friedrich Nietzsche'
guest_list.insert(2, bff)

print("Dear " + guest_list[0]+", I cordially extend my invitation to join me for dinner at my place of residence.\n")

for guest in guest_list:
    print("Dear " + guest + ", I would like to cordially invite you to join me for dinner at my place of residence.\n")

for second_guest in guest_list:
    if second_guest is guest_list[1]:
        print(second_guest)
        
#ENUMERATE IS WHEN YOU WANT TO FIND THE INDEX 
#to print the index of a certain value: (index, VARIABLE), then just print the index even if you don't use the variable
for index, unknown in enumerate(guest_list):
    if unknown == "Future Husband":
        print(index)

#Make a list of the index numbers of a list 
#Get the length of the guest list - len(list_name)
    #Then the range of that number to get all the separate numbers - range(len(list))
    #   #Finally the list out the numbers in the range - list(len(list_name))

separate_list = list(range(len(guest_list)))
print(separate_list)
   
#list.insert()

#to print the index. it needs to be (index, VARIABLE), then just print the index even if you don't use it
for index in enumerate(guest_list):
    print(index)

#
   