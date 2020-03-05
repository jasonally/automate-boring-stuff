#! /usr/bin/env python3
# sandwichmaker.py – Sandwich making program using pyinputplus.

import pyinputplus as pyip
import time

# Make this into a function to DRY.
def condiment_checker(name):
	prompt = 'Would you like %s?\n' % name
	response = pyip.inputYesNo(prompt)
	if response == 'yes':
		ingredients.append(name.capitalize())

ingredients = []
price = 0

print('Welcome to Sandwich Maker!\n')
time.sleep(1)

print('Your menu choices are:')
print('Bread: Sourdough, Wheat, White')
print('Protein: Chicken ($5.50), Ham ($5.25), Tofu ($5.75), Turkey ($5.50)')
print('Cheese ($0.50): Cheddar, Mozzarella, Swiss')
print('Condiments: Mayo, Mustard, Lettuce, Tomato\n')
time.sleep(1)

print('Which bread would you like?')
response = pyip.inputMenu(['Sourdough', 'Wheat', 'White'], numbered=True)
ingredients.append(response)

print('\nWhich protein would you like?')
response = pyip.inputMenu(['Chicken', 'Ham', 'Tofu', 'Turkey'], numbered=True)
if response == 'Chicken' or response == 'Turkey':
	price += 5.50
elif response == 'Ham':
	price += 5.25
else:
	price += 5.75
ingredients.append(response)

prompt = '\nWould you like cheese?\n'
response = pyip.inputYesNo(prompt)
# Only display options if user wants cheese.
if response == 'yes':
	print('\nWhich type of cheese would you like?')
	response = pyip.inputMenu(['Cheddar', 'Mozzarella', 'Swiss'], numbered=True)
	ingredients.append(response)
	price += 0.50

condiment_checker('mayo')
condiment_checker('mustard')
condiment_checker('lettuce')
condiment_checker('tomato')

prompt = 'How many sandwiches would you like?\n'
response = pyip.inputInt(prompt, min=1)
time.sleep(1)

order = '\nThe ingredients in your %s sandwich are:' % response
if response > 1:
	order = order.replace('h ', 'hes ') # Make sandwich plural if needed.
print(order)

for item in ingredients:
	print('– ' + item)
time.sleep(1)

price = '${:,.2f}'.format(price * response) # Convert price into $X.XX format.
print('\nYour total is: %s. Have a nice day!' % price)