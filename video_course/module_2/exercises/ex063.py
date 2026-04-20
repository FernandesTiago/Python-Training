# n terms of the Fibonacci sequence

a = 0
b = 1

while True:
    try:
        count = int(input("how many terms of the Fibonacci sequence do you want to see? "))
        if count > 0:
            break
        else:
            print("Invalid value")
    except ValueError:
        print("Invalid value")
while count > 0:
    print(f"{a}", end=" ")
    a, b = b, a + b
    count -= 1
