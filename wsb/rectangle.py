import math

a = input("Enter length of side a: ")
b = input("Enter length of side b: ")
print("Given rectangle with sides a = {} and b = {}".format(a, b))
print("Area: {}".format(int(a)*int(b)))
print("Perimeter: {}".format((2*int(a))+(2*int(b))))
print("Diagonal: {}".format(round(math.sqrt(pow(int(a), 2)+pow(int(b), 2)), 2)))

