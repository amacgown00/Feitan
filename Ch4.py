#Chapter 4

#4-1
toppings = ['pepperoni', 'squash and ricotta', 'Tripoli']
for pizza in toppings:
    print('I like %s pizza' % pizza)

print('Pizza is one of my favorite foods.\n\n')

#4-2
animals = ['Dachshund', 'Ragdoll', 'Siamese']
for pet in animals:
    print('A %s would make a good pet' % pet)
print('These are all pets I had wanted growing up.\n')

#4-3 
"""
for count in range(1, 21):
    print(count)
"""
a_milli = []
for num in range(1, 1000001):
    a_milli.append(num)
print(min(a_milli))
print(max(a_milli))

for val in range(1, 10):
   print(sum(val))