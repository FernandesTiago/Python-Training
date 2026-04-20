# contact list
# added feature to delete contacts


names = []
numbers = []

while True:
    print("\n--- Contact list ---")
    print("""
[1] Add contact
[2] Search contact
[3] Open contact list
[4] Delete contact
[5] Exit
""")
    while True:
        try:
            action = int(input("What do you want to do? "))
            if 1 <= action <= 5:
                break
            else:
                continue
        except ValueError:
            print("Enter a value from 1 to 5")
    if action == 1:
        while True:
            print(f"\n--- add contact {len(names)+1} ---\n")
            name = input("What name do you want to save? ").strip().title()
            if name.replace(" ", "").isalpha():
                names.append(name)
                break
            else:
                print("\nInvalid name\n")
        while True:
            number = input("What is the phone number? (13 digits): ").strip()
            if number.isdigit() and len(number) == 13:
                number = list(number)
                number.insert(0, "+")
                number.insert(3, " ")
                number.insert(4, "(")
                number.insert(7, ")")
                number.insert(8, " ")
                number.insert(14, "-")
                number = "".join(number)
                numbers.append(number)
                print(f"\nContact {name} added with number {number}!\n")
                break
            else:
                print("\nEnter the country code, area code and number all together!\n")
    elif action == 2:
        if len(names) > 0:
            stop = False
            while not stop:
                search = input("\nWhat name do you want to search? ").strip().title()
                if search.replace(" ", "").isalpha():
                    for b in range(len(names)):
                        if search in names[b]:
                            print(f"""
{names[b]}
{numbers[b]}""")
                            stop = True
                    else:
                        if not stop:
                            print("Name not found")
                            while True:
                                keep_going = input("Do you want to try again? (Y/N) ").strip().upper()
                                if keep_going == "Y" or keep_going == "N":
                                    if keep_going == "Y":
                                        break
                                    else:
                                        stop = True
                                        break
                                else:
                                    print('Enter "Y" or "N"')
                else:
                    print("\nEnter a valid name")
        else:
            print("\nContact list is empty")
    elif action == 3:
        if len(names) > 0:
            for b in range(len(names)):
                print(f"""
{names[b]}
{numbers[b]}""")
        else:
            print("\nContact list is empty")
    elif action == 4:
        if len(names) > 0:
            stop = False
            while not stop:
                found_indexes = []
                search = input("\nWhich contact do you want to delete? ").strip().title()
                if search.replace(" ", "").isalpha():
                    for b in range(len(names)):
                        if search in names[b]:
                            found_indexes.append(b)
                            print(f"""
/ [{len(found_indexes)}]
/ {names[b]}
/ {numbers[b]}""")
                    if len(found_indexes) > 1:
                        while not stop:
                            try:
                                choice = int(input(f"\nWhich contact do you want to delete? (1 to {len(found_indexes)}) "))
                                if 1 <= choice <= len(found_indexes):
                                    real_index = found_indexes[choice - 1]
                                    print(f"""
{names[real_index]}
{numbers[real_index]}
""")
                                    while not stop:
                                        delete = input("\nAre you sure you want to delete this contact? (Y/N) ").strip().upper()
                                        if delete == "Y" or delete == "N":
                                            if delete == "Y":
                                                names.pop(real_index)
                                                numbers.pop(real_index)
                                                print("\nName deleted")
                                                stop = True
                                            else:
                                                print("\nName not deleted")
                                                stop = True
                                        else:
                                            print('Enter "Y" or "N"')
                                        break
                            except ValueError:
                                print("Enter a valid value")
                    elif len(found_indexes) == 1:
                        while True:
                            delete = input("\nAre you sure you want to delete this contact? (Y/N) ").strip().upper()
                            if delete == "Y" or delete == "N":
                                if delete == "Y":
                                    real_index = len(found_indexes) - 1
                                    names.pop(real_index)
                                    numbers.pop(real_index)
                                    print("\nName deleted")
                                    stop = True
                                    break
                                else:
                                    print("\nName not deleted")
                                    stop = True
                                    break
                            else:
                                print('Enter "Y" or "N"')
                    else:
                        if not stop:
                            print("Name not found")
                            while True:
                                keep_going = input("Do you want to try again? (Y/N) ").strip().upper()
                                if keep_going == "Y" or keep_going == "N":
                                    if keep_going == "Y":
                                        break
                                    else:
                                        stop = True
                                        break
                                else:
                                    print('Enter "Y" or "N"')
                else:
                    print("Enter a valid name")
        else:
            print("\nContact list is empty")
    else:
        print("\nThank you for using the contact list!!\n")
        break
