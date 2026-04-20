# factorial of a number

while True:
    try:
        factor = int(input("What value do you want to factorialize? "))
        break
    except ValueError:
        print("Invalid value")

answer = factor

if factor > 0:
    print(f"{factor}! = ", end="")
    while factor > 1:
        print(f"{factor} * ", end="")
        factor -= 1
        answer *= factor
    print(f"{factor} = ", end="")
    print(answer)
elif factor == 0:
    print("The factorial of 0 is 1")
else:
    print("The value must be greater than or equal to zero!")
