#! /usr/bin/env python3
# randomquizgenerator.py – Creates quizzes with questions and answers in random
# order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
	'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
	'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
	'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
	'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
	'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
	'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
	'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
	'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
	'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
	'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
	'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
	'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 
	'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 
	'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 
	'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
	'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

# Generate 5 quiz files.
for quiz_num in range(5):
	# Create the quiz and answer key files.
	quiz_file = open(f'capitalsquiz{quiz_num + 1}.txt', 'w')
	answer_key_file = open(f'capitalsquizanswers{quiz_num + 1}.txt', 'w')
	# Write out the header for the quiz.
	quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quiz_file.write((' ' * 20) + f'State Capitals Quiz (Form {quiz_num + 1})')
	quiz_file.write('\n\n')
	
	# Create a list of just the states. Each entry in states corresponds to a
	# key in capitals. So capitals[states[i]] gives you the value of capitals 
	# for value i in states.
	states = list(capitals.keys())
	# Shuffle the order of the states.
	random.shuffle(states)

	# Loop through all 50 states, making a question for each.
	for question_num in range(50):
		# Get right and wrong answers.
		correct_answer = capitals[states[question_num]]
		wrong_answers = list(capitals.values())
		# Remove the correct answer from our list of wrong answers.
		del wrong_answers[wrong_answers.index(correct_answer)]
		# Need three wrong answers to go with our correct answer.
		wrong_answers = random.sample(wrong_answers, 3)
		# New list with all answer options.
		answer_options = wrong_answers + [correct_answer]
		# Shuffle answer options so the correct answer isn't always last.
		random.shuffle(answer_options)

		# Write the question and answer options to the quiz file.
		# Formatting from
		# https://stackoverflow.com/questions/45965007/multiline-f-string-in-python
		quiz_file.write(f'{question_num + 1}. What is the capital of '
			f'{states[question_num]}?\n')
		for i in range(4):
			quiz_file.write(f"    {'ABCD'[i]}. { answer_options[i]}\n")
		quiz_file.write('\n')

		# Write the answer key to a file.
		answer_key_file.write(f"{question_num + 1}. "
			f"{'ABCD'[answer_options.index(correct_answer)]}\n")
	quiz_file.close()
	answer_key_file.close()