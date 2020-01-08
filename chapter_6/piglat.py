#! /usr/bin/env python3
# piglat.py – English to Pig Latin.

print('Enter the English message to translate into Pig Latin:')
message = input()

# Use a tuple because this won't change. Make it immutable.
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pig_latin = [] # A list of the words in Pig Latin.

# Basic idea: Check each word in message. Depending on the characters you'll
# perform different actions to convert the word into Pig Latin. For loop to
# iterate through each word, if-else statements for the conditional logic.
for word in message.split():
	# Separate the non-letters a the start of this word. We don't want
	# old. to be translated to old.yay, nor do we want 4,000 to become ,0004ay.
	prefix_non_letters = ''
	while len(word) > 0 and not word[0].isalpha():
		prefix_non_letters += word[0]
		word = word[1:] # Move to the next character in word, begin check again.
	if len(word) == 0:
		pig_latin.append(prefix_non_letters) # No translating needed.
		continue

	# Separate the non-letters at the end of this word.
	suffix_non_letters = ''
	while not word[-1].isalpha():
		suffix_non_letters += word[-1]
		# Ranges don't include last charcter, so this shortens the word.
		word = word[:-1]

	# Remember if the word was in uppercase or title case.
	was_upper = word.isupper()
	was_title = word.istitle()

	word = word.lower() # Make the word lowercase for translation.

	# Separate the consonants at the start of this word.
	prefix_consonants = ''
	while len(word) > 0 and not word[0] in VOWELS:
		prefix_consonants += word[0]
		word = word[1:] # Iterate until you hit a vowel.

	# Add Pig Latin ending to the word.
	if prefix_consonants != '':
		word += prefix_consonants + 'ay'
	else:
		word += 'yay'

	# Set the word back to uppercase or title case.
	if was_upper:
		word = word.upper()
	if was_title:
		word = word.title()

	# Add the non-letters back to the start or end of the word.
	pig_latin.append(prefix_non_letters + word + suffix_non_letters)

# Join the words back together into a single string.
print(' '.join(pig_latin))







