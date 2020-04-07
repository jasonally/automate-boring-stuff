#! /usr/bin/env python3

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
play_file = open('romeoandjuliet.txt', 'wb') # Write binary mode.

# Separate the data into 100,000 byte segments.
for chunk in res.iter_content(100000):
	play_file.write(chunk)

play_file.close()