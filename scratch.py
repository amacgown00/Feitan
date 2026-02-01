##!/usr/bin/env python3
#lists

"""
#standard list
warlords_7 = ['Hawkeye Mihawk', 'Kuma', 'Doflamingo', 'Boa Hancock','Jinbe','Crocodile','Gecko Moria']

#looping through a slice
for warlord in warlords_7[0:3]:
    print(warlord.lower())

#returning the second to last in the list
print(warlords_7[-2])

#New way of inserting variables into a string (and adding an index)
print("I don't consider " + warlords_7[5] + " and " + warlords_7[6] + " as warlords.")

#Old way of inserting variables into a string (adding an index)   
print(f"I don't consider {warlords_7[5]} and {warlords_7[6]} to be warlords anymore.")
    #old way
    
favorite1 = warlords_7[0].upper()
favorite2 = warlords_7[3].upper()
favorite3 = warlords_7[4].upper()

#Inserting variables in uppercase the new way
print(favorite1 + ", " + favorite2 + " , and " + favorite3 + " are my favorite warlords.")

#Changing the list to replace Crocodile with Traffy 
warlords_7[5] = "Trafalger D. Water Law"
print(warlords_7)

#Adding Teach to the end of the list
warlords_7.append('Marshall D. Teach')
print(warlords_7)

#Creating a list of the emperors starting with an empty list
emperors4 = []
emperors4.append('Whitebeard')
emperors4.append('Red-Haired Shanks')
print(emperors4)

emp1 = 'Whitebeard'
emp2 = 'Kaido'
emp3 = 'Big Mom'
emp4 = 'Red-Haired Shanks'

emperors4.insert(3, emp3)
emperors4.insert(2, emp2)
print(emperors4)

#Marineford
del emperors4[0]
print(emperors4)

sea = warlords_7.pop(4)
zombie = warlords_7.pop(5)
pink = warlords_7.pop(2)

print(warlords_7)
print(sea + ', ' + zombie + ", and " + pink + " were removed.")

#Removing Traffy by his name since I don't know his position
warlords_7.remove('Trafalger D. Water Law')
print(warlords_7)

#The enumerate() function returns both the index and the value of each item in a list
for index, new_warlords in enumerate(warlords_7):
    print(index, new_warlords)
    
guest_list = ['Future Husband', 'Zohran Mamdani', 'Anderson Cooper']
"""
"""Getting items out of the For loop with append
iceberg = []
for temp in range(1,100, 5):
    iceberg.append(temp)
print(iceberg)

#!/usr/bin/env python3
text = "Hi Steve Buschemi"
print(text)
text = "Hi octopus"
print(text)

drink, ice = ("passionfruit", "70")

print("I'll have a " + drink.title() + " boba with " + ice + "% ice.")

price = "4 "
cost = "3"

orchidaceae = ["paphiopedilum", "vanda", "cattleya", "phalaenopsis", "catasetum", "bulbophyllum", "dendrobium"]

for index, column_header in enumerate(orchidaceae):
    print(index, column_header)
    
for cat in orchidaceae:
    if any(letter in cat for letter in x):
        print(cat)

num_list = [2, 4, 6, 1, 139, 421, 52, 1738]

for digit in num_list:
    if digit > 20:
        print(digit)

List comprehension

List_name = [(new variable of what you want) for (variable) in #####]

pond = [toast**3 for toast in range(1, 4)]
print(pond)

"""




     
    
