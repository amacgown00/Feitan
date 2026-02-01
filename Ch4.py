#Chapter 4

#4-1
"""
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


a_milli = []
for num in range(1, 1000001):
    a_milli.append(num)
print(min(a_milli))
print(max(a_milli))
print(sum(a_milli))

#4-6
odd = [count_odd for count_odd in range(1, 21, 2)]
print(odd)

#4-7
multiples_3 = [multiple for multiple in range(3, 31, 3)]
print(multiples_3)

#4-8
for gem in range(1, 11):
    print(gem**3)

#4-9
cubes = [cube**3 for cube in range(1, 11)]
print(cubes)
"""

lux = ['emitter', 'enhancer', 'transmuter', 'specialist']
print(lux[-2:])

results = [2, 4, 9, 100, 34, 21, 59, 60, 83, 31]
print(sorted(results, reverse=false))

"""for top_3 in sorted(results):
    print(top_3[])Z"""
