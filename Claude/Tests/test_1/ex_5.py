# Contact registration system using a .txt file
#
# Create a program with 3 functions:
#
# 1. save_contact(name, phone)
#    -> Adds a contact to the file "contacts.txt"
#    -> Format of each line: "name;phone"
#
# 2. list_contacts()
#    -> Reads the file and prints all contacts like:
#    -> Name: Ana | Phone: 99999-0000
#    -> Handle the case where the file does not exist
#    -> Handle the case where the file is empty
#
# 3. search_contact(name)
#    -> Reads the file and returns the phone of the contact
#    -> If not found, returns None
#    -> Handle the case where the file does not exist
#
# Test by calling the 3 functions at the end

from pathlib import Path

DATA_FILE = Path(__file__).parent / "contacts.txt"


def clear_file():
    with open(DATA_FILE, "w"):
        pass

def save_contact(name, phone):
    """ADDS A CONTACT TO THE FILE"""
    with open(DATA_FILE, "a") as file:
        file.write(f"{name};{phone}\n")

def list_contacts():
    try:
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()
            if lines:
                print("\nContact list:\n")
                for i in range(0, len(lines)):
                    lines[i] = lines[i].split(";")
                    number = lines[i][1]
                    number = list(number.replace("\n", ""))
                    number.insert(5, "-")
                    number = "".join(number)
                    print(f"Name: {lines[i][0]:<10} | Phone: {number}")
                print()
            else:
                print("List is empty")
    except FileNotFoundError:
        with open(DATA_FILE, "a") as file:
            pass
        print("list is empty")

def search_contact(name):
    try:
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()
            print("Search contacts:\n")
            if lines:
                for i in range(0, len(lines)):
                    lines[i] = lines[i].split(";")
                    if lines[i][0] == name:
                        number = lines[i][1]
                        number = list(number.replace("\n", ""))
                        number.insert(5, "-")
                        number = "".join(number)
                        return number
            else:
                print("List is empty")
    except FileNotFoundError:
        with open(DATA_FILE, "a") as file:
            pass
        print("list is empty")


save_contact("Tiago", "999380440")
save_contact("Juliana", "991713132")

list_contacts()

number = search_contact("Tiago")
print(number)

clear_file()
