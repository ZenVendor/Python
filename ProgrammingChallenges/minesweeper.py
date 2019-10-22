"""
TODO:
- coordinate validation
- win state
"""

import os, re, sys

def adjacent(width, height, row, column):
    adjacent = []
    for r in range((0 if (row - 1) < 0 else (row - 1)), ((row + 2) if (row + 2) < height else height)):
        for c in range((0 if (column - 1) < 0 else (column - 1)), ((column + 2) if (column + 2) < width else width)):
            if r != row or c != column:
                adjacent.append((r * width) + c)
    return adjacent

def display_board(width, height, board):
    os.system('clear')
    ruler = []
    for i in range(width):
        ruler.append(chr(ord('A') + i))
    print('    {}'.format(ruler))            
    for h in range(0, height):
        print('{}: {}{}'.format(h, ' ' if h < 10 else '', board[(h * width) : (h * width) + (width)]))


width = int(input('Width: '))
height = int(input('Height: '))

import random
mines = []
for i in range(0, random.randrange((width * height) // 5, (width * height) // 3)):
    mines.append(random.randrange(0, width * height))

mines = set(mines)

minefield = ['.'] * (width * height)
for m in mines:
    minefield[m] = '*'

hints = [0] * (width * height)

for m in mines:
    adj = adjacent(width, height, (m // width), (m % width))
    for a in adj:
        hints[a] += 1

for m in mines:
    hints[m] = -1

board = ['.'] * (width * height)

while True:
    display_board(width, height, board)    

    print('Enter coordinates (e.g. a5), "flag" to flag mines or "exit".')
    selection = input('>: ')
    
    if selection == 'exit':
        break
    
    elif selection == 'flag':
        print('Enter comma-separated coordinates (e.g. "a5,b4").')
        flags = input('flags: ')
    
        if not re.search('^([A-Za-z]\d(,|))+$', flags):
            print('Not valid.')
            time.sleep(1)
            
        else:
            flags = flags.split(',')
            for f in flags:
                board[(int(f[1]) * width) + (ord(f[0].lower()) - ord('a'))] = 'F'
        
    elif not re.search('^[A-Za-z]\d$', selection):
        print("wrong coordinates")
        time.sleep(1)
        
    else:
        sel_row = int(selection[1])
        sel_col = ord(selection[0].lower()) - ord('a')
        
        if hints[(sel_row * width) + sel_col] == -1:
            print("BOOM")
            break
            
        elif hints[(sel_row * width) + sel_col] > 0:
            board[(sel_row * width) + sel_col] = str(hints[(sel_row * width) + sel_col])

        else:
            zero_cache = [(sel_row * width) + sel_col]
            zeroes = []

            while zero_cache:
                z = zero_cache.pop()
                zeroes.append(z)
                adj = adjacent(width, height, (z // width), (z % width))

                for a in adj:
                    board[a] = str(hints[a])
                    if (hints[a] == 0) and (a not in zeroes):
                        zero_cache.append(a)

            for z in zeroes:
                board[z] = '0'

