#! /usr/bin/env python3
# renameamerdates.py – Renames filenames with American MM-DD-YY date format to
# European DD-MM-YYYY.

import shutil, os, re

# Create a regex which matches files with the American date format.
date_pattern = re.compile(r"""^(.*?)  # All text before the date.
	((0|1)?\d)-						  # One or two digits for the month.
	((0|1|2|3)?\d)-					  # One or two digits for the day.
	((19|20)\d\d)					  # Four digits for the year.
	(.*?)$							  # All text after the date.
	""", re.VERBOSE)

# Loop over the files in the working directory.
for amer_filename in os.listdir('.'):
	mo = date_pattern.search(amer_filename)

	# Skip files without a date. mo will contain something if there is a match.
	if mo == None:
		continue

	# Get the different parts of the filename. The regex has a particular
	# pattern, so if there's a match, we can know with certainty which parts
	# of the regex match which parts of the text.
	# From the book text:
	# "To keep the group numbers straight, try reading the regex from the 
	# beginning, and count up each time you encounter an opening parenthesis. 
	# Without thinking about the code, just write an outline of the regular 
	# expression. This can help you visualize the groups.""
	before_part = mo.group(1)
	month_part = mo.group(2)
	day_part = mo.group(4)
	year_part = mo.group(6)
	after_part = mo.group(8)

	# Form the European-style filename.
	euro_filename = (before_part + day_part + '-' + month_part + '-' + 
		year_part + after_part)

	# Get the full, absolute file paths.
	abs_working_dir = os.path.abspath('.')
	amer_filename = os.path.join(abs_working_dir, amer_filename)
	euro_filename = os.path.join(abs_working_dir, euro_filename)

	# Rename the files.
	print(f'Renaming "{amer_filename}" to "{euro_filename}"...')
	# shutil.move(amer_filename, euro_filename) # Uncomment after testing.