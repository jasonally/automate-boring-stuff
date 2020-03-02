#! /usr/bin/env python3
# passworddetection.py – Tells user if an input string is a strong password.

import re, time

# From:
# https://www.itworld.com/article/2833081/how-to-validate-password-strength-using-a-regular-expression.html
# https://rubular.com/r/Q66wtCcTUJ
password_regex = re.compile(r'''(
	(?=^.{8,}$)				# At least eight characters.
	(?=.*\d)				# Digit.
	(?=.*[!@#$%^&*]+)		# Special character.
	(?![.\n])				# Do not match if . or new line is at end of input.
	(?=.*[A-Z])				# Upper case character.
	(?=.*[a-z]).*$			# Lower case character.
	)''', re.VERBOSE)

def password_checker():
	while True:
		time.sleep(1)
		print('Enter a string.')
		password_test = input()
		time.sleep(1)
		if password_regex.search(password_test):
			print('Congratulations, you entered a strong password.')
			break
		else:
			print('You did not enter a strong password. Please try again.')

print('Enter a string to test if it is a strong password.')

time.sleep(1)

print('''A strong password has:
– At least eight characters
– One upper case letter (A-Z)
– One lower case letter (a-z)
– One digit (0-9)
– One special character (!@#$%^&*).''')

password_checker()