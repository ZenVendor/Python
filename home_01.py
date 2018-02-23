import re

def checkio(data):

    if len(data) < 10:
        return False
    elif re.search("[a-z]+", data) != None and re.search("[A-Z]+", data) != None and re.search("[0-9]+", data) != None:
        return True
    else:
        return False


print(re.search("[a-z]+", "87982") != None)
print(re.search("[a-z]+", "87982dsf") != None)

assert checkio('abc') == False, "1"
assert checkio('abcdefghijklmnop') == False, "2"
assert checkio('abcDEFabcGEF') == False, "3"
assert checkio('abc123DEF091') == True, "4"


