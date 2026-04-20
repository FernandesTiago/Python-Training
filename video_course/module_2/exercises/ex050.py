# input of 6 numbers and sum only the even ones

total = 0

for c in range(0, 6):
    while True:
        try:
            n = int(input("Enter a value: "))
            break
        except ValueError:
            print("Enter an integer!!")
    if n % 2 == 0:
        total = total + n

print(total)
