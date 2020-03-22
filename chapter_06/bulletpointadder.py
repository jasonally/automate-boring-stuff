#! /usr/bin/env python3
# bulletpointadder.py - Adds Wikipedia bullet points to the start of each line
# of text on the clipboard.

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n') # Creates a list of strings separated by line breaks.
for i in range(len(lines)): # Loop through all indexes in the list.
	lines[i] = '* ' + lines[i] # Add star to each string in the list.
text = '\n'.join(lines) # Rejoin the lines of text.

pyperclip.copy(text)