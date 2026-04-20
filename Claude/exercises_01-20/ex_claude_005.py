# Student average using dictionary

student1 = {"name": "Tiago", "grades": [7, 8, 9]}
student2 = {"name": "Juliana", "grades": [2, 4, 8]}
student3 = {"name": "Mari", "grades": [9, 2, 6]}

students = [student1, student2, student3]

for student in students:
    print(f" The average of {student['name']} is {sum(student['grades']) / len(student['grades']):.2f}")
