# Create a function that receives a list of student dictionaries
# (each with "name" and "grade") and returns only the passing ones
# (grade >= 6).
# Print the passing students formatted with name left-aligned
# in 15 characters and grade with 1 decimal place.

# Test with:
students = [
    {"name": "Ana", "grade": 8.0},
    {"name": "Bruno", "grade": 4.5},
    {"name": "Carla", "grade": 6.0},
    {"name": "Diego", "grade": 3.0},
    {"name": "Elena", "grade": 9.5}
]

def passing_students(student_list):
    """RECEIVES A LIST OF STUDENT DICTIONARIES AND RETURNS THE LIST OF PASSING ONES"""
    passed = []
    for student in student_list:
        if student["grade"] >= 6:
            passed.append(student)
    return passed

passed_list = passing_students(students)

print("Passing students:")
for i in range(0, len(passed_list)):
    print(f"Student: {passed_list[i]['name']:<15} Grade: {passed_list[i]['grade']:.1f}")
