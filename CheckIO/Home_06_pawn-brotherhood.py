def safe_pawns(pawns):
    pawnsNum = []
    count = 0
    for pawn in pawns:
        pawnsNum.append(int(pawn[1] + str(ord(pawn[0]) - 96)))
    for pawn in pawnsNum:
        if pawnsNum.count(pawn - 9) > 0 or pawnsNum.count(pawn - 11) > 0:
            count += 1
    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


