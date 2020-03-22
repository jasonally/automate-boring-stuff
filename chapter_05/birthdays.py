birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
	print('Enter a name: (blank to quit)')
	name = input()
	if name == '':
		print('Have a nice day!')
		break
	if name in birthdays:
		print(birthdays[name] + ' is the birthday of ' + name)
	else:
		print('I don\'t have birthday information for ' + name)
		print('What is their birthday?')
		new_birthday = input()
		birthdays[name] = new_birthday
		# This doesn't actually save the changes to memory.
		print('Birthday database updated.')