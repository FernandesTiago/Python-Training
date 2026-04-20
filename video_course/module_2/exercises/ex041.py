# Athletic category based on age in the sport

from datetime import date

current_year = date.today().year

while True:
    try:
        year = int(input("When were you born? "))
        if 1900 <= year <= current_year:
            break
        else:
            print(f"It must be a year between 1900 and {current_year}.")
    except ValueError:
        print(f"It must be a year between 1900 and {current_year}.")

age = current_year - year

while True:
    try:
        swim_age = int(input("at what age did you start swimming? "))
        if swim_age <= age:
            break
        else:
            print(f"You have been training longer than you've been alive...")
    except ValueError:
        print(f"The value must be less than your age.")

years_swimming = age - swim_age

if years_swimming <= 1:
    print("JUVENILE")
elif years_swimming <= 2:
    print("CHILD")
elif years_swimming <= 3:
    print("JUNIOR")
elif years_swimming <= 4:
    print("SENIOR")
else:
    print("MASTER")
