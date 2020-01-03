def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
    	print(v, k)
    	item_total += v
    print("Total number of items: " + str(item_total))

def add_to_inventory(inventory, added_items):
	for i in added_items:
        # If item isn't a key in inventory, add it and set value to 0.
        # If the key exists in inventory, leave value unchanged.
		inventory.setdefault(i, 0)
		inventory[i] += 1
	return inventory

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)