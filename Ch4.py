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
for count in range(1, 21):
    print(count)

blank_list = [val**2 for val in range(1, 5)]
print(blank_list)
print(sum(blank_list))

print("\n\n")

a_milli = []
for num in range(1, 1000001):
    a_milli.append(num)
print(min(a_milli))
print(max(a_milli))
print(sum(a_milli))

print("\n\n")

#4-6
odd = [count_odd for count_odd in range(1, 21, 2)]
print(odd)

print("\n\n")

#4-7
multiples_3 = [multiple for multiple in range(3, 31, 3)]
print(multiples_3)

print("\n\n")

#4-8
for gem in range(1, 11):
    print(gem**3)

print("\n\n")

#4-9
cubes = [cube**3 for cube in range(1, 11)]
print(cubes)

print("\n\n")

lux = ['emitter', 'enhancer', 'transmuter', 'specialist', 'manipulator', 'conjurer']
print(lux[-2:])

print("\n\n")

results = [2, 4, 9, 100, 34, 21, 59, 60, 83, 31]
new_results = sorted(results, reverse=True)
print(new_results[:3])

print("\n\n")

for top_3 in sorted(results[-3:], reverse=True):
    print(top_3)
          
#4-10
cubes = [cube**3 for cube in range(1, 11)]
print('The first three items in the list are: ')
for junapi in cubes[:3]:
    print(junapi)

print('\n\n')

print('Three items from the middle of the list are: ')
for middle_3 in cubes[3:6]:
    print(middle_3)
    
print('\n\n')

print('The last three items in the list are: ')
for last_3 in cubes[-3:]:
    print(last_3)

print('\n\n')
#4-11    
friends_pizzas = toppings[:]
my_pizzas = toppings[:]

friends_pizzas.append('vodka sauce')
my_pizzas.append('soppresata and hot honey')
bullet = '- '
print('My favorite pizzas are: ')
for my_types_pizza in my_pizzas:
    print(bullet + my_types_pizza)

print("My friend's favorite pizzas are")
for their_pizza in friends_pizzas:
    print(bullet + their_pizza)
    
print('\n\n')

buffet = ('Fried rice', 'Chicken teriyaki', 'Spare ribs', 'Crab rangoon', 'Ice cream')
for buffet_item in buffet:
    print(buffet_item)

print("\n\n")

#buffet.append('Garlic Chicken')

buffet = ("General Tso's chicken", 'Chicken teriyaki', 'Lap cheung fan', 'Crab rangoon', 'Ice cream')
print('New buffet menu: ')
for buffet_item in buffet:
    print(bullet + buffet_item)