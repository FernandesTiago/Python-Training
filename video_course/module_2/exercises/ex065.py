# average of numbers, continue prompt, largest, smallest

while True:
    try:
        v = int(input("enter a value: "))
        total = largest = smallest = v
        count = 1
        break
    except ValueError:
        print("Invalid value")
while True:
    v = input("""If you don't want to continue type ( exit )
enter another value: """)
    try:
        v = int(v)
        total += v
        count += 1
        if v > largest:
            largest = v
        if v < smallest:
            smallest = v
    except ValueError:
        v = v.strip().upper()
        if v == "EXIT":
            break
        else:
            print("Invalid value")
print(f"""
The average of the values is {total/count}
The largest value was {largest}
The smallest value was {smallest}
""")
