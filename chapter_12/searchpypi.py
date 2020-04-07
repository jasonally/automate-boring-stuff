#! /usr/bin/env python3
# searchpypi.py – Opens several search results from PyPI.

import requests, sys, webbrowser, bs4, logging

logging.basicConfig(level=logging.INFO, 
	format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

print('Searching...') # Display text while downloading the search result page.
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
logging.debug(res)

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
logging.debug(soup.prettify())

# Open a browser tab for each result.
link_elems = soup.select('.package-snippet')
logging.debug(link_elems)

num_open = min(5, len(link_elems))
for i in range(num_open):
	url_to_open = 'https://pypi.org' + link_elems[i].get('href')
	print('Opening', url_to_open)
	webbrowser.open(url_to_open)