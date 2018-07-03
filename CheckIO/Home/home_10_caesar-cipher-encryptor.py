import re
def to_encrypt(text, delta):
    first = ord('a')
    last = ord('z')
    result = ''
    for letter in text:
        if re.match('[a-z]', letter):
            num = ord(letter) + delta
            while num > last or num < first:
                if num > last:
                    num = first + (num - last - 1)
                else:
                    num = last - (first - num - 1)
            letter = chr(num)
        result += letter
    return result

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('simple text', 16))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")