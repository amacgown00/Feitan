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