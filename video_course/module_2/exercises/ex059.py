# Number operations menu

lo = 0

while True:
    try:
        n1 = int(input("what is the first value? "))
        break
    except ValueError:
        print("enter an integer")
while lo != 1:
    try:
        n2 = int(input("what is the second value? "))
        lo += 1
    except ValueError:
        print("enter an integer")
# I used both while loops just to test and learn.

while True:
    print(f"""
    What do you want to do with the numbers: \033[1;33m{n1}\033[m and \033[1;33m{n2}\033[m?

    \033[1;33m[1]\033[m Add
    \033[1;33m[2]\033[m Multiply
    \033[1;33m[3]\033[m Greater
    \033[1;33m[4]\033[m New numbers
    \033[1;33m[5]\033[m Exit program
    """)

    try:
        action = int(input("what is the action? "))
        if 0 < action <= 5:
            if action == 1:
                print(f"{n1} + {n2} = {n1 + n2}")
            elif action == 2:
                print(f"{n1} * {n2} = {n1 * n2}")
            elif action == 3:
                if n1 > n2:
                    print(f"{n1} > {n2}")
                elif n1 < n2:
                    print(f"{n1} < {n2}")
                else:
                    print(f"{n1} = {n2}")
            elif action == 4:
                while True:
                    try:
                        n1 = int(input("what is the first value? "))
                        break
                    except ValueError:
                        print("enter an integer")
                while True:
                    try:
                        n2 = int(input("what is the second value? "))
                        break
                    except ValueError:
                        print("enter an integer")
            else:
                print("Thanks for testing my program!!")
                break
        else:
            print("The value must be a number between 1 and 5")
    except ValueError:
        print("The value must be a number between 1 and 5")
