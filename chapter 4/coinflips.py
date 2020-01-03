import random
number_of_streaks = 0

for experiment_number in range(10000):
	flips = []
	for i in range(100):
		# Let 0 and 1 represent heads and tails. No need to
		# expliclty define them as H and T.
		flips.append(random.randint(0,1))
	# Convert list into a string, use if-in statement to quickly
	# search through it.
	if ('000000' or '111111') in ''.join(str(x) for x in flips):
		number_of_streaks += 1
	# print(experiment_number)

print('Chance of streak: %s%%' % (number_of_streaks / 100))