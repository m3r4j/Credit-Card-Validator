# credit_card_validator.py
import sys
number = input('Enter the number: ')


def check(number):
	# Get rid of spaces
	number = number.split()
	number = ''.join(number)
	added_numbers = ''

	# Check if its 16
	if not len(number) == 16:
		print('Invalid!')
		sys.exit()

	# Get the total of numbers by adding up every second index in a 4-digit number
	total = 0

	for x in range(0, len(number), 2):
		total += int(number[x])


	# Multiply the total by 2
	total *= 2

	# Count the ones (odds) in the numbers that are 5 or more and add them to total
	count = 0
	for x in range(0, len(number), 2):
		if int(number[x]) > 4:
			count += 1

	total += count


	# Count every second and fourth number in the groups and add them to total
	for x in range(0, len(number) + 2, 2):
		if not int(number[x - 1])  < 0:
			total += int(number[x - 1])


	# Check if the total is divisible by 10, if it is then set valid to true
	if total % 10 == 0:
		return True


	return False


if check(number):
	print('Valid!')
else:
	print('Invalid!')