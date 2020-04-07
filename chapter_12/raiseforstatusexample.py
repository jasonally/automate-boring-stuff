#! /usr/bin/env python3

# Download requests module if needed.
# Run pip3 install --user requests
import requests

res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
	res.raise_for_status()
except Exception as exc:
	print('There was a problem: %s' % (exc))