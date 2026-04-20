# Tell whether it is a triangle and which triangle it is

a = int(input("what is the length of one side? "))
b = int(input("what is the length of another side? "))
c = int(input("what is the length of another side? "))

sides = [a, b, c]
sorted_sides = sorted(sides)

if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
    print("it is a triangle!!")
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("it is not a triangle")
