def spam():
	eggs = 'spam local'
	# Prints 'spam local'.
	print(eggs)

def bacon():
	eggs = 'bacon local'
	print(eggs) # Prints 'bacon local'.
	spam()
	print(eggs) # Prints 'bacon local'.

eggs = 'global'
bacon()
# Prints 'global'
print(eggs)