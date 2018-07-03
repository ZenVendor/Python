import re
from collections import Counter
def checkio(text):
    z = Counter(re.findall('[a-z]', text.lower()))
    maxd = max(z.values())
    for i in sorted(z.keys()):
        if z[i] == maxd:
            return i












if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    assert checkio("Z") == "z", "letter."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")