# analyze a man's birth year and check military enlistment status

import datetime

current_year = datetime.date.today().year

while True:

    year = input("Enter your birth year: ")

    if year.isnumeric():
        year = int(year)
        if 1900 <= year <= current_year:
            break
        else:
            print(f"The year must be between \033[32m1900\033[m and \033[32m{current_year}\033[m")
    else:
        print("The year must be an integer.")

age = current_year - year

if age < 18:
    print(f"You have \033[32m{18 - age}\033[m years to enlist.")
elif age == 18:
    print(f"\033[32mYou must enlist this year.\033[m")
else:
    print(f"you should have enlisted \033[32m{age - 18}\033[m years ago.")
