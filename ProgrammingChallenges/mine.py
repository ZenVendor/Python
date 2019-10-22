import os, re, sys

os.system('clear')

wh = input('Enter WxH: ')

if re.search('^\d+x\d+$', wh):
	wh = wh.split('x')
	w = int(wh[0])
	h = int(wh[1])
else:
	sys.exit('Wrong dimensions')

mines =  input('Type "random" or mine indexes (0-{}) separated with comas: '.format(w * h - 1))

if mines == 'random':
	import random
	
	mines = []
	mnumber = random.randrange((w * h)//5, (w * h)//3)
	for d in range(0, mnumber):
		mines.append(random.randrange(0, (w * h)- 1))
	
	mines = set(mines)
			
elif re.search('^(\d+,)+\d+$', mines):
	mines = list(map(int, mines.split(',')))
else:
	sys.exit('No bueno')

mfield = ['.'] * (w * h)
for m in mines:
	mfield[m] = '*'

for c in range(0, h):
	print('{}'.format(mfield[(c*w):(c*w)+(w)]))

field = [0] * (w * h)

for m in mines:
	x = m % w
	y = m // w

	for c in range((0 if (x - 1) < 0 else (x - 1)), ((x + 2) if (x + 2) < w else w)):
		for r in range((0 if (y - 1) < 0 else (y - 1)), ((y + 2) if (y + 2) < h else h)):
			field[(r * w) + c] += 1

field = list(map(str, field))

for m in mines:
	field[m] = '*'

print()
for c in range(0, h):
	print('{}'.format(field[(c*w):(c*w)+(w)]))
		
