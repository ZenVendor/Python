def checkio(game_result):
    result = 'D'
    for row in game_result:
        if row == 'XXX':
            result = 'X'
            break
        if row == 'OOO':
            result = 'O'
            break
    for column in range(0, 3):
        if game_result[0][column] == 'X' and game_result[1][column] == 'X' and game_result[2][column] == 'X':
            result = 'X'
            break
        if game_result[0][column] == 'O' and game_result[1][column] == 'O' and game_result[2][column] == 'O':
            result = 'O'
            break
    if game_result[0][0] == 'X' and game_result[1][1] == 'X' and game_result[2][2] == 'X':
        result = 'X'
    if game_result[0][2] == 'X' and game_result[1][1] == 'X' and game_result[2][0] == 'X':
        result = 'X'
    if game_result[0][0] == 'O' and game_result[1][1] == 'O' and game_result[2][2] == 'O':
        result = 'O'
    if game_result[0][2] == 'O' and game_result[1][1] == 'O' and game_result[2][0] == 'O':
        result = 'O'
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    assert checkio(["OO.", "XOX", "XOX"]) == "O", "Another O"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

