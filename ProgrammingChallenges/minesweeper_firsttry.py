import os, re, sys, time

def uncover_zero(width, height, column, row):
	uncovered = {}
	zero = []
	zero_history = []
	for c in range((0 if (column - 1) < 0 else (column - 1)), ((column + 2) if (column + 2) < width else width)):
		for r in range((0 if (row - 1) < 0 else (row - 1)), ((row + 2) if (row + 2) < height else height)):
			uncovered.update({(r * width) + c: (field[(r * width) + c])})
			if field[(r * width) + c] == 0:
				zero.append((r * width) + c)
				print('zero: {}'.format(zero))
				
	return uncovered, zero


os.system('clear')

wh = input('Enter WxH: ')

if re.search('^\d+x\d+$', wh):
	wh = wh.split('x')
	w = int(wh[0])
	h = int(wh[1])
else:
	sys.exit('Wrong dimensions')

mines =  input('Type "rand" or mine indexes (0-{}) separated with commas: '.format(w * h - 1))

if mines == 'rand':
	import random
	
	mines = []
	mnumber = random.randrange((w * h)//5, (w * h)//3)
	for d in range(0, mnumber):
		mines.append(random.randrange(0, (w * h)- 1))
	
	mines = set(mines)
			
elif re.search('^(\d+,)+\d+$', mines):
	mines = list(map(int, mines.split(',')))
else:
	sys.exit('No bueno. Type "random" or comma separated numbers. No spaces.')

field = [0] * (w * h)

for m in mines:
	x = m % w
	y = m // w

	for c in range((0 if (x - 1) < 0 else (x - 1)), ((x + 2) if (x + 2) < w else w)):
		for r in range((0 if (y - 1) < 0 else (y - 1)), ((y + 2) if (y + 2) < h else h)):
			field[(r * w) + c] += 1

for m in mines:
	field[m] = '*'

columns = []
for c in range(ord('A'), ord('A') + w):
	columns.append(chr(c))

mfield = ['.'] * (w * h)

while True:
	#os.system('clear')
	print('   {}'.format(columns))
	for c in range(0, h):
		print('{}:'.format(c), end = ' ')
		print('{}'.format(field[(c*w):(c*w)+(w)]))
	print()
	print('   {}'.format(columns))
	for c in range(0, h):
		print('{}:'.format(c), end = ' ')
		print('{}'.format(mfield[(c*w):(c*w)+(w)]))
		
	print()
	step = input('Enter coordinates (e.g. "a5") or "exit": ')
	
	if step == 'exit':
		sys.exit('Bye')
	elif re.search('^[A-Za-z]\d$', step):
		
		column = ord(step[0].lower()) - ord('a')
		row = int(step[1])
		cell = (row * w) + column
		
		print('{}, {}'.format(column, row))
		time.sleep(1)
				
		if field[cell] == '*':
			sys.exit('BOOM!')
		elif field[cell] > 0:
			mfield[cell] = str(field[cell])
		else:
			uncovered = {}
			zero = []
			zero_history = []
			
			uncovered, zero = uncover_zero(w, h, column, row)
			zero_history = list(zero)
			
			print('uncovered: {}'.format(uncovered))
			print('zero_history: {}'.format(zero_history))
			print('zero: {}'.format(zero))
			
			while zero:
				for z in zero:
					x = z % w
					y = z // w
					un, ze = uncover_zero(w, h, x, y)
					
					print('un: {}'.format(un))
					print('ze: {}'.format(ze))
					
					uncovered.update(un)
					zero = set(zero).symmetric_difference(set(ze))
					print('zero: {}'.format(zero))
					zero = zero.difference_update(zero_history)
					print('zero: {}'.format(zero))	
					zero_history.append(zero)
					print('zero_history: {}'.format(zero_history))
			
			print(uncovered)
			for c in uncovered.keys():
				mfield[c] = str(uncovered[c])
				
			time.sleep(2)
			
			
	else:
		print('Nope')
		time.sleep(2)
	
		
