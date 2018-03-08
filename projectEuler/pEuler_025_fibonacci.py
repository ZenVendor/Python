x = 1
y = 1
number = 0
index = 2

while len(str(number)) < 1000:
    number = x + y
    x = y
    y = number
    index += 1
    #print("{} - {}".format(index, number))

print("index = {}".format(index))
