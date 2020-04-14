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


