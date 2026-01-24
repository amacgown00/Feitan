from datetime import datetime
now = datetime.now()

formatted = now.strftime("%b %d, %Y")
print(formatted)

from datetime import date
birthday = date(1996, 4, 18)

target_date = date(2017, 3, 30)

age = target_date.year - birthday.year

if (target_date.month, target_date.day) < (birthday.month, birthday.day):
    age-= 1

print(f"Birthday: {birthday}")
print(f"Target date: {target_date}")
print(f"I was {age} years old on {target_date}")