#euklidean algorithm
import math

math.gc

x = input("Enter integer x: ")
y = input("Enter integer y: ")

while x != y:
    if x > y:
        x -= y
    else:
        y -= x
