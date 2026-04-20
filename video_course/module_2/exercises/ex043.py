# BMI calculation

while True:
    try:
        weight = float(input("what is your weight? "))
        if 1 <= weight <= 500:
            break
        else:
            print("The value must be between 1 and 500")
    except ValueError:
        print("The value must be between 1 and 500")

while True:
    try:
        height = float(input("what is your height in meters? "))
        if 1 <= height <= 3:
            break
        else:
            print("The value must be between 1 and 3")
    except ValueError:
        print("The value must be between 1 and 3")

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi <= 25:
    print("Ideal weight")
elif bmi <= 30:
    print("Overweight")
elif bmi <= 40:
    print("Obesity")
else:
    print("Morbid obesity")

print(f"{bmi:.2f}")
