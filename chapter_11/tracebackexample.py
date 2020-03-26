#! /usr/bin/env python3

import traceback

try:
	raise Exception('This is the error message.')
except:
	error_file = open('errorinfo.txt', 'w')
	error_file.write(traceback.format_exc())
	error_file.close()
	print('The traceback info was written to errorinfo.txt')