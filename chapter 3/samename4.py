def spam():
	print(eggs) # Triggers an UnboundLocalError
	eggs = 'spam local'

eggs = 'global'
spam()