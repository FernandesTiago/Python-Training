# Class training

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def details(self):
        print(f"Employee: {self.name} | Salary: $ {self.salary}")
    def __str__(self):
        return f"Employee: {self.name} | Salary: $ {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def __str__(self):
        return f"Employee: {self.name} | Salary: $ {self.salary} | Department: {self.department}"

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    def code(self):
        if self.language == "Python":
            print(f'{self.name}: print("Hello")')
        elif self.language == "Java":
            print(f'{self.name}: System.out.println("Hello")')
        elif self.language == "JavaScript":
            print(f'{self.name}: console.log("Hello")')

manager = Manager("Tiago", 2500, "Cybersecurity")
dev1 = Developer("Juliana", 1500, "Python")
dev2 = Developer("Mari", 1250, "JavaScript")

devs = [dev1, dev2]
managers = [manager]
employees = managers + devs

for employee in employees:
    employee.details()

for dev in devs:
    dev.code()
