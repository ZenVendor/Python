VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

import re
def checkio(text):
    count = 0

    words = re.findall('[A-Z]+', text.upper())
    for word in words:
        if len(word) > 1:
            previous = 1
            flag = 1

            if word[0] in VOWELS:
                previous = 0

            for i in range (1, len(word)):
                if word[i] in VOWELS:
                    current = 0
                else:
                    current = 1

                if current == previous:
                    flag = 0
                    break
                previous = current

            if flag == 1:
                count += 1

    print(count)
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio("My name is ...") == 3, "All words are striped"
    # assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"