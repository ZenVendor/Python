import math

r = input("Enter radius r: ")
print("Volume of a sphere with radius {} is: {}".format(r, round((4 * math.pi * pow(int(r), 3))/3, 2)))
