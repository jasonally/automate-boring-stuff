#! /usr/bin/env python3
# tableprinter.py - A table printing program using a list of lists.

table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(table):
	col_widths = [0] * len(table)

	# Standard logic to iterate through a list of lists.
	# For each list, set col_widths[x] equal to the longest value.
	for x in range(len(table)):
		for y in range(len(table[x])):
			if len(table[x][y]) > col_widths[x]:
				col_widths[x] = len(table[x][y])

	# Flip the iteration logic to get the table output the right way.
	# We're told: "Assume that all the inner lists will contain the same number 
	# of strings."
	for x in range(len(table[0])):
		for y in range(len(table)):
			print(table[y][x].rjust(col_widths[y]), end=' ')
		print('')

print_table(table_data)