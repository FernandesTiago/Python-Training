# employee registration

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data24.json"


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"Employee: {self.name} | Salary: $ {self.salary}"

def delete_data():
    with open(DATA_FILE, "w") as file:
        json.dump([], file)

def display():
    with open(DATA_FILE, "r") as file:
        content = json.load(file)
        print(f"Full list: {content}")

def save_employee(employee):
    try:
        with open(DATA_FILE, "r") as file:
            content = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("List is empty")
        with open(DATA_FILE, "w") as file:
            content = []
            json.dump(content, file)
    else:
        with open(DATA_FILE, "w") as file:
            entry = {"name": employee.name, "salary": employee.salary}
            content.append(entry)
            json.dump(content, file)
        with open(DATA_FILE, "r") as file:
            content = json.load(file)


while True:
    try:
        display()
        break
    except (FileNotFoundError, json.JSONDecodeError):
        print("List is empty")
        with open(DATA_FILE, "w") as file:
            content = []
            json.dump(content, file)

while True:
    choice = input("Do you want to add more people? (Y,N,D) ").title().strip()
    if choice == "Y":
        name = input("What is the name? ")
        while True:
            try:
                salary = int(input("What is the salary? "))
                break
            except ValueError:
                print("Enter an integer!")
        dev = Employee(name, salary)
        save_employee(dev)
    elif choice == "N":
        break
    elif choice == "D":
        delete_data()
    else:
        print("Enter Y, N or D!")

display()

with open(DATA_FILE, "r") as file:
    content = json.load(file)
    employees = []
    for item in content:
        obj = Employee(item["name"], item["salary"])
        employees.append(obj)
for employee in employees:
    print(employee)
