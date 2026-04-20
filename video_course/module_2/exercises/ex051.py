# Arithmetic progression

while True:
    try:
        first_term = int(input("what is the first term? "))
        break
    except ValueError:
        print("enter an integer")
while True:
    try:
        ratio = int(input("what is the common difference? "))
        break
    except ValueError:
        print("enter an integer")

for c in range(first_term, first_term + ratio * 10, ratio):
    print(c)
