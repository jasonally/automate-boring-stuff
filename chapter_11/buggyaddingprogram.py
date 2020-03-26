#! /usr/bin/env python3

# Running this in a debugger lets you see the bug of not
# converting the inputs to integers.
print('Enter the first number to add:')
first = int(input())
print('Enter the second number to add:')
second = int(input())
print('Enter the third number to add:')
third = int(input())
print('The sum is ' + str(first + second + third))