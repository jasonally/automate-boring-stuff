#! /usr/bin/env python3
# searchebay.py – Opens several search results from eBay.

import requests, sys, webbrowser, bs4, logging

logging.basicConfig(level=logging.INFO, 
	format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

print('Searching...') # Display text while downloading the search result page.
res = requests.get('https://www.ebay.com/sch/i.html?_nkw=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
logging.debug(res)

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
logging.debug(soup.prettify())

# Open a browser tab for each result.
link_elems = soup.select('.s-item__link')
logging.debug(link_elems)

num_open = min(10, len(link_elems))
for i in range(num_open):
	url_to_open = link_elems[i].get('href')
	print('Opening', url_to_open)
	webbrowser.open(url_to_open)