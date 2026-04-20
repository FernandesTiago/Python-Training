# multiplication table using for in range

while True:
    try:
        n = input("Which multiplication table do you want? ")
        n = int(n)
        if 0 < n <= 10:
            break
        else:
            print("Must be a value from 0 to 10")
    except ValueError:
        print("Must be a value from 0 to 10")

for c in range(1, 11):
    print(n * c)
