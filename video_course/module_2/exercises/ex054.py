# counter of people over 18 years old

from datetime import date

current_year = date.today().year
adults = 0

for c in range(1, 8):
    while True:
        try:
            birth_year = int(input("when were you born? "))
            break
        except ValueError:
            print("enter a number")
    if current_year - birth_year >= 18:
        adults += 1
if adults > 0:
    print(f"{adults} people are 18+")
else:
    print("no one is 18+")
