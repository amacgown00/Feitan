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


new_index_list = list((range(len(guest_list))))
print(new_index_list)

"""for final_guest in guest_list:
    guest_list.pop()"""
    
#list.insert()
"""to print the index. it needs to be (index, VARIABLE), then just print the index even if you don't use it