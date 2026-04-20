# comparison of two numbers (greater/lesser/equal)

while True:
    number1 = input("Enter any integer: ")
    if number1.isnumeric():
        number1 = float(number1)
        break
    else:
        print("enter a valid number!")

while True:
    number2 = input("Enter another integer: ")
    if number2.isnumeric():
        number2 = float(number2)
        break
    else:
        print("enter a valid number!")

if number1 > number2:
    print("The first value is greater than the second")
elif number1 < number2:
    print("The second value is greater than the first")
else:
    print("The values are equal")
