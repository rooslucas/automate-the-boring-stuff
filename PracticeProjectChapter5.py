# Practice project 2 Fantasy Game Inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item_name, item_value in inventory.items():
        print(str(item_value) + ' ' + item_name)
        item_total = item_total + item_value
    print('Total number of items: ' + str(item_total))


displayInventory(stuff)


# Practice project 3 List to Dictionary Function for Fantasy Game Inventory

def addToInventory(inventory, added_items):
    for item in added_items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print(dragonLoot.count(item))
addToInventory(inv, dragonLoot)
displayInventory(inv)
