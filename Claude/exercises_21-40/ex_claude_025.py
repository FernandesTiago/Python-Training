# Create a terminal menu system with the options:
# 1 - List employees
# 2 - Add employee
# 3 - Update salary
# 4 - Delete employee
# 0 - Exit

def menu():
    print("-=" * 16)
    print("""[1] - List employees
[2] - Add employee
[3] - Update salary
[4] - Delete employee
[0] - Exit""")
    print("-=" * 16)
def choose():
    try:
        choice = int(input())
        return choice
    except ValueError:
        print("Enter a valid number")
def listing():
    pass
menu()
