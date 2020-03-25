#! /usr/bin/env python3
# renameeurodates.py – Renames filenames with European DD-MM-YYYY date format to
# American MM-DD-YY. Converse of renameamerdates.py.

import shutil, os, re

# Create a regex which matches files with the European date format.
date_pattern = re.compile(r"""^(.*?)  # All text before the date.
	((0|1|2|3)?\d)-					  # One or two digits for the day.
	((0|1)?\d)-						  # One or two digits for the month.
	((19|20)\d\d)					  # Four digits for the year.
	(.*?)$							  # All text after the date.
	""", re.VERBOSE)

for euro_filename in os.listdir('.'):
	mo = date_pattern.search(euro_filename)

	if mo == None:
		continue

	before_part = mo.group(1)
	day_part = mo.group(2)
	month_part = mo.group(4)
	year_part = mo.group(6)
	after_part = mo.group(8)

	amer_filename = (before_part + month_part + '-' + day_part + '-' + 
		year_part + after_part)

	abs_working_dir = os.path.abspath('.')
	euro_filename = os.path.join(abs_working_dir, euro_filename)
	amer_filename = os.path.join(abs_working_dir, amer_filename)

	# Rename the files.
	print(f'Renaming "{euro_filename}" to "{amer_filename}"...')
	# shutil.move(amer_filename, euro_filename) # Uncomment after testing.