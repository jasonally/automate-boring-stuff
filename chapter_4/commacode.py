spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_print(input):
	output = ''
	if not spam:
		print("List is empty.")
	elif len(spam) == 1:
		print(spam[0])
	else:
		for item in spam[:-1]:
			output += item + ', '
		output += 'and ' + spam[-1]
		print(output)

comma_print(spam)