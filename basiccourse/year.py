year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0:
    print("Year {} is a leap year.".format(year))
elif year % 400 == 0:
    print("Year {} is a leap year.".format(year))
else:
    print("Year {} is a common year.".format(year))
