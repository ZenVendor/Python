import math

print("ax2 + bx + c = 0")
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

if a == 0:
    print("Function {}x + {} has zero at x = {} and intercept at y = {}.".format(b, c, -c/b, b))
else:
    delta = pow(b, 2) - 4 * a * c
    if delta > 0:
        x1 = float((-b - math.sqrt(delta)) / (2 * a))
        x2 = float((-b + math.sqrt(delta)) / (2 * a))
        print("Function {}x2 + {}x + {} has two roots: x1 = {}, x2 = {}".format(a, b, c, x1, x2))
    elif delta == 0:
        x1 = float(-b / (2 * a))
        print("Function {}x2 + {}x + {} has one root: x = {}".format(a, b, c, x1))
    else:
        print("Function has no roots.")
