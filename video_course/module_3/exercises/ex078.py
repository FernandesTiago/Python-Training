# 5 values in a list, largest, smallest and positions

values = []
loop = 0

while loop < 5:
    try:
        n = int(input("enter a value: "))
        values.append(n)
        loop += 1
    except ValueError:
        print("Invalid value")

largest = max(values)
smallest = min(values)

print(f"{', '.join(str(i) for i in values)} {largest} {smallest} {values.index(largest)} {values.index(smallest)}")
