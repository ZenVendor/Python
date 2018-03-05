def long_repeat(line):
    repcount = 0
    for i in range(0, len(line)):
        count = 1
        for rep in range(i+1, len(line)):
            if line[rep] != line[i]:
                break
            count += 1
        if count > repcount:
            repcount = count
    return repcount


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
