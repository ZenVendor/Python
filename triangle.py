import math

sides = []

print("Enter lengths of triangle sides")
sides.append(int(input("First side: ")))
sides.append(int(input("Second side: ")))
sides.append(int(input("Third side: ")))

sides.sort()
a = sides[0]
b = sides[1]
c = sides[2]

if c > a + b:
    print("This is not a triangle.")
else:
    a = pow(a, 2)
    b = pow(b, 2)
    c = pow(c, 2)

    if a + b == c:
        if math.gcd(a, b) == 1 and math.gcd(a, c) == 1 and math.gcd(b, c):
            print("This is a Pythagorean triple.")
        else:
            print("This is a right triangle.")
    elif a + b > c:
        if a == b == c:
            print("This is an equilateral triangle.")
        elif b == c:
            print("This is an isosceles triangle.")
        else:
            print("This is an acute triangle.")
    else:
        print("This is an obtuse triangle.")
