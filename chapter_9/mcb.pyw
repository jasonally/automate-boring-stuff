#! /usr/bin/env python3
# mcb.pyw – Saves and loads pieces of text to the clipboard.
# Usage: python3 mcb.pyw save <keyword> – Saves keyword to clipboard.
#        python3 mcb.pyw <keyword> – Loads keyword to clipboard.
#		 python3 mcb.pyw list – Loads all keywords to clipboard

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3:
	# Save clipboard content.
	if sys.argv[1].lower() == 'save':
		mcb_shelf[sys.argv[2]] = pyperclip.paste()
	# Delete keyword and associated content.
	elif sys.argv[1].lower() == 'delete':
		del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
	# List keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcb_shelf.keys())))
	# Delete all keywords and content.
	elif sys.argv[1].lower() == 'delete':
		mcb_shelf.clear()
	elif sys.argv[1] in mcb_shelf:
		pyperclip.copy(mcb_shelf[sys.argv[1]])

mcb_shelf.close()