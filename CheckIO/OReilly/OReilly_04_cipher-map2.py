def recall_password(cipher_grille, ciphered_password):

    pwd = ''
    for i in range(4):
        for j in range(4):
            if cipher_grille[i][j] == 'X':
                pwd += ciphered_password[i][j]

    for i in range(4):
        for j in reversed(range(4)):
            if cipher_grille[j][i] == 'X':
                pwd += ciphered_password[i][3-j]

    for i in reversed(range(4)):
        for j in reversed(range(4)):
            if cipher_grille[i][j] == 'X':
                pwd += ciphered_password[3-i][3-j]

    for i in reversed(range(4)):
        for j in range(4):
            if cipher_grille[j][i] == 'X':
                pwd += ciphered_password[3-i][j]

    return pwd

recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi'))

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert recall_password(
#         ('X...',
#          '..X.',
#          'X..X',
#          '....'),
#         ('itdf',
#          'gdce',
#          'aton',
#          'qrdi')) == 'icantforgetiddqd', 'First example'
#
#     assert recall_password(
#         ('....',
#          'X..X',
#          '.X..',
#          '...X'),
#         ('xhwc',
#          'rsqx',
#          'xqzz',
#          'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'