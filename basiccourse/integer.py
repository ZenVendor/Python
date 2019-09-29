x = int("Enter integer x: ")
if x % 2 == 0:
    print("Number {} is even.".format(x))
else:
    print("Number {} is odd.".format(x))

if x > 0:
    print("It is also positive.")
elif x < 0:
    print("It is also negative.")
else:
    print("It is also zero.")
