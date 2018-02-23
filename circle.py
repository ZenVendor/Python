import math

r = input("Enter radius r: ")
print("Given circle with radius r = {}".format(r))
print("Area: {}".format(round(math.pi * pow(int(r), 2), 2)))
print("Circumference: {}".format(round(2 * math.pi * int(r), 2)))

