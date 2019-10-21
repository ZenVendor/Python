import re

print('Print two integers separated with space (e.g. "10 20").')
numbers = input('> ')

if re.search('^\d+ \d+$', numbers):
    rng = numbers.split(' ')
    cycle_length = []

    for number in range(int(rng[0]), int(rng[1]) + 1):
        counter = 1

        while number != 1:
            if number % 2 == 0:
                number /= 2
            else:
                number = (number * 3) + 1

            counter += 1

        cycle_length.append(counter)
	
    print('{} {}'.format(numbers, max(cycle_length)))

else:
    print('No bueno')
