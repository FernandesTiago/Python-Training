# student average calculation

while True:
    try:
        grade_1 = float(input("\033[1;31mEnter your first grade: \033[m"))
        if 0 <= grade_1 <= 10:
            break
        else:
            print(" the grade must be a number between 0 and 10.")
    except ValueError:
        print(" the grade must be a number between 0 and 10.")

while True:
    try:
        grade_2 = float(input("\033[1;31mEnter your second grade: \033[m"))
        if 0 <= grade_2 <= 10:
            break
        else:
            print(" the grade must be a number between 0 and 10.")
    except ValueError:
        print(" the grade must be a number between 0 and 10.")

average = (grade_1 + grade_2) / 2

if average >= 7:
    print("\033[1;32mYOU PASSED!! CONGRATULATIONS!!\033[m")
    print(f"AVERAGE: \033[1;32m{average:.2f}\033[m")
elif average < 5:
    print("\033[1;31mYou failed...\033[m")
    print(f"AVERAGE: \033[1;31m{average:.2f}\033[m")
else:
    print("You are in \033[1;33mrecovery\033[m")
    print(f"AVERAGE: \033[1;33m{average:.2f}\033[m")
