value = ''

def collatz(number):
	if number % 2 == 0: # Number is even.
		number = number // 2
		print(number)
		return number
	else: # Number is odd.
		number = 3 * number + 1
		print(number)
		return number

while True:
	print('Enter a positive number.')
	try:
		value = int(input())
		if value < 1:
			print('Input must be a positive integer.')
		else:
			break
	except ValueError:
		print('Input must be a positive integer.')

while value != 1:
	value = collatz(value)

