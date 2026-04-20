# Convert an integer to Binary, Octal and Hexadecimal.

while True:

    number = input("Enter any integer: ")
    if number.isnumeric():
        number = int(number)
        break
    else:
        print("Enter an integer!")

while True:

    base = input("what conversion base do you want? (1-Binary, 2-octal, 3-hexadecimal) ")

    if base == "1":
        print(bin(number)[2:])
        break
    elif base == "2":
        print(oct(number)[2:])
        break
    elif base == "3":
        print(hex(number)[2:])
        break
    else:
        print("You entered the wrong base value!!")
