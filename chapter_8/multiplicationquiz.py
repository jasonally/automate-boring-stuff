#! /usr/bin/env python3
# multiplicationquiz.py – Simple multiplication quiz program using pyinputplus.

import pyinputplus as pyip
import random, time

number_of_questions = 10
correct_answers = 0
for question_number in range(number_of_questions):
	# Pick two random numbers:
	num_1 = random.randint(0,9)
	num_2 = random.randint(0,9)
	prompt = '#%s: %s x %s = ' % (question_number + 1, num_1, num_2)
	try:
		# Correct answers are handled by allowRegexes.
		# Incorrect answers are handled by blockRegexes, with a custom message.
		pyip.inputStr(prompt, allowRegexes=['^%s$' % (num_1 * num_2)],
			blockRegexes=[('.*', 'Incorrect!')],
			timeout=8, limit=3)
	# timeout and limit parameters trigger exceptions; need error handling.
	except pyip.TimeoutException:
		print('Out of time!')
	except pyip.RetryLimitException:
		print('Out of tries!')
	else:
		# This block runs if no exceptions were raised in the try block.
		print('Correct!')
		correct_answers += 1
	time.sleep(1) # Brief pause to let user see the result.
print('Score: %s / %s' % (correct_answers, number_of_questions))