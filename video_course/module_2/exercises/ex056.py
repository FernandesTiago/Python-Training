# name, age and gender of 4 people: average age, oldest man and women under 20

genders = []
names = []
ages = []

for c in range(1, 5):
    while True:
        gender = input("what is your gender? (M, F) ").strip().upper()
        if gender == "M" or gender == "F":
            genders.append(gender)
            break
        else:
            print("Enter M or F")
    while True:
        name = input("what is your name? ").strip().title()
        if name.isnumeric() or name.isdigit() or name.find(".") != -1:
            print("enter your name!")
        else:
            names.append(name)
            break
    while True:
        try:
            age = int(input("what is your age? "))
            if 0 < age <= 100:
                ages.append(age)
                break
            else:
                print("enter a value from 1 to 100")
        except ValueError:
            print("enter a value from 1 to 100")

young_women = []
men_ages = []

for b in range(len(genders)):
    if genders[b] == "F" and ages[b] < 20:
        young_women.append(names[b])
    elif genders[b] == "M":
        men_ages.append(ages[b])

print()
print(f"The average age is {sum(ages)/len(ages)}")
if men_ages:
    print(f"The oldest man is {names[ages.index(max(men_ages))]} and he is {max(men_ages)} years old")
else:
    print("no men in the group")
if young_women:
    print(f"The women under 20 are: {', '.join(young_women)}")
