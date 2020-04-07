#! /usr/bin/env python3
# news.py – Launches a bunch of news sites I tend to check each morning.

import webbrowser

addresses = [
	'https://old.reddit.com/',
	'https://fivethirtyeight.com/',
	'https://www.vox.com/',
	'https://www.sfchronicle.com/',
	'https://www.washingtonpost.com/',
	'https://www.nytimes.com/'
]

for address in addresses:
	webbrowser.open(address)