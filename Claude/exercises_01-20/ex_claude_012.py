# student registration def

def register_student(name, grades):
    return {"name": name, "grades": grades}
def average(grades):
    return sum(grades) / len(grades)
def status(real_average):
    if real_average < 6:
        return "failed"
    else:
        return "passed"
def display(student_list, passed_list):
    for student in student_list:
        name = student["name"]
        grades = student["grades"]
        real_average = average(grades)
        print(f"""Student: {name}
Average: {real_average:.2f}
Status: {status(real_average)}
""")
    print("Passing students: ", end="")
    for passed in passed_list:
        print(passed["name"], end=" ")

def filter_passed(student_list):
    passed_students = []
    for student in student_list:
        if average(student["grades"]) >= 6:
            passed_students.append(student)
    return passed_students


student1 = register_student("Tiago", [10, 5, 10, 6])
student2 = register_student("Mari", [7, 2, 5, 9])
student3 = register_student("Juliana", [9, 7, 8, 5])

students = [student1, student2, student3]
passed = filter_passed(students)

display(students, passed)
