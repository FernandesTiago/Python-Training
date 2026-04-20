while True:
    try:
        value1 = int(input("what is the first value? "))
        operator = input("what is the operator? (+, -, x, / )? ")
        value2 = int(input("what is the second value? "))

        if operator == "+":
            print(value1 + value2)
        elif operator == "-":
            print(value1 - value2)
        elif operator == "x":
            print(value1 * value2)
        elif operator == "/":
            print(value1 / value2)
        else:
            print("the operator must be in the list!")

        break

    except:
        print("the value must be a number!")
