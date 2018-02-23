x = input("Enter integer x: ")
y = input("Enter integer y: ")
if y != 0:
    print("Quotient: {}".format(int(int(x) / int(y))))
    print("Remainder: {}".format(int(x) % int(y)))
else:
    print("Cannot divide by 0!")
