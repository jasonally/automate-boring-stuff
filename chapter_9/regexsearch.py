#! /usr/bin/env python3
# regexsearch.py – Opens .txt files in folder, looks for regex, prints matches.

import os, re

def file_checker(input_regex):
	# Make list of every file in current working directory.
	for file_name in os.listdir('.'):
		if file_name.endswith('.txt'):
			for i, line in enumerate(open(file_name)):
				for match in re.finditer(input_regex, line):
					print('Found on line %s in %s: %s' % (i+1, file_name, line))

print('What would you like to search for? Enter a regular expression.')
regex = re.compile(input())
file_checker(regex)