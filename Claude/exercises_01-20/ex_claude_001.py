# 5 employees, salary average, who earns more than average, and the lowest and highest salary

employees = []
salaries = []

c = 0

while c < 5:
    print(f"\n--- Registering employee {c+1} ---")
    employee = input("\nWhat is the employee name? ").strip().title()
    if employee.replace(" ", "").isalpha():
        employees.append(employee)
    else:
        print("\nEnter a valid name")
        continue
    try:
        salary = float(input("What is their salary? $"))
        salaries.append(salary)
        c += 1
    except ValueError:
        print("\nEnter a valid value\n")
print(f"The salary average is {sum(salaries)/c}")
print("Employees that earn equal to or more than the average are: ", end="")
for b in range(len(salaries)):
    if salaries[b] >= sum(salaries)/c:
        print(employees[b], end=", ")
print(f"\nThe highest salary is ${max(salaries)}")
print(f"And the lowest is ${min(salaries)}")
