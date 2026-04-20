# highest and lowest weights read

weights = []

for c in range(1, 6):
    while True:
        try:
            weight = int(input("what is your weight? "))
            break
        except ValueError:
            print("enter an integer")
    weights.append(weight)
weights.sort()
print(min(weights), max(weights))
