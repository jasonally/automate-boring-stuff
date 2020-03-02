#! /usr/bin/env python3
# datedetection.py – Tells user if a date in DD/MM/YYYY format is valid.

import re

date_regex = re.compile(r'''
	([0-3]\d)			# Between 01-39, further date validation later.
	/
	([0-1]\d)			# Month between 0-12.
	/
	([1-2]\d\d\d)		# Year between 1000-2999.
	''', re.VERBOSE)

too_many_days = ('There are too many days in the month you entered. '
	'Please try again.')

not_leap_year = ('The year you entered is not a leap year. Please try again.')

def date_check(date):
	date_match = date_regex.search(date)
	if not date_match:
		return('You entered an invalid date. Please try again.')
	else:
		day, month, year = date_match.groups()	# Multiple assignment trick.
		# Convert valiues to integers.
		day = int(day)
		month = int(month)
		year = int(year)

	# No month has more than 31 days.
	if day > 31:
		return(too_many_days)
	# April, June, September, and November have 30 days.
	if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
		return(too_many_days)
	if month == 2:
		# February at most has 29 days.
		if day >= 30:
			return(too_many_days)
		if day == 29:
			# Years divisible by 100 and not divisible by 400 aren't leap years.
			if (year % 100 == 0) and (year % 400 != 0):
				return(not_leap_year)
			if year % 4 != 0:
				return(not_leap_year)

	return('Congratulations, ' + date + ' is a valid date.')

print(date_check('18/04/1906'))
print(date_check('24/10/1929'))
print(date_check('32/03/2063'))
print(date_check('07/12/1941'))
print(date_check('test'))
print(date_check('22/11/1963'))
print(date_check('17/10/1989'))
print(date_check('09/11/1989'))
print(date_check('29/02/1993'))
print(date_check('29/02/2020'))