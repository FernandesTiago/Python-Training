# app that allows entering infinite numbers until 999 is entered, showing how many numbers were entered and their sum.

total = 0
count = 0

while True:
    try:
        number = int(input("Enter a number: "))
        if number == 999:
            print(f"the sum of the values is {total}. Items added: {count}")
            break
        else:
            total += number
            count += 1
    except ValueError:
        print("Invalid value")
