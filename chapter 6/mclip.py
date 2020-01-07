#! /usr/bin/env python3
# mclip.py - A multi-clipboard program.

TEXT = {'agree': """Yes, I agree. That sounds find to me.""",
		'busy': """Sorry, can we do this later this week or next week?""",
		'upsell': """Would you consider making this a monthly donation?"""}

import sys, pyperclip

if len(sys.argv) < 2:
	print('Usage: python3 mclip.py [keyphrase] - copy phrase text')
	sys.exit()

keyphrase = sys.argv[1] # First command line arg is the keyphrase.

if keyphrase in TEXT:
	pyperclip.copy(TEXT[keyphrase])
	print('Text for ' + keyphrase + ' copied to clipboard.')
else:
	print('There is no text for ' + keyphrase)