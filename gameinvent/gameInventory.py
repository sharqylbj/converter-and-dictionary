# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification

import csv


# Displays the inventory.
def display_inventory(inventory):

    inventory = {}
    total_items = 0
    print("Inventory:")

    for key, value in inventory.items():
        total_items += value
        print(value, key)

    print("Total number of items: " + total_items)


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):

    for item in added_items:
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1

    return inventory


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):

    dash = "-"
    space = " "
    longest_item_name = max(inventory.keys(), key=len)
    longest_name_value = len(longest_item_name)
    longest_value = max(inventory.values(), key=len)
    longest_value = len(longest_value)
    total_items_number = sum(inventory.values())
    items_tuple = ()

    for key, value in inventory.items():
        items_tuple.append((key, value))

    if order == "count,desc":
        items_tuple = sorted(items_tuple, key=lambda value: value[1], reverse=True)
    elif order == "count,asc":
        items_tuple = sorted(items_tuple, key=lambda value: value[1])

    print("\nInventory:\n")

    if longest_name_value < 7:
        print("  " + "count:" + "    " + "item name:")
        print(dash * 22)
        for item in items_tuple:
            print(str(item[1]).rjust(8, " ") + str(item[0].rjust(14, " ")))
        print(dash * 22)
    else:
        print("  " + "count:" + "item name:".rjust((longest_name_value + 4), " "))
        print(dash * (12 + longest_name_value))
        for item in items_tuple:
            print(str(item[1]).rjust(8, " ") +
                  str(item[0]).rjust(longest_name_value + 4, " "))
        print(dash * (12 + longest_name_value))

    print("Total number of items: " + total_items_number)


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename):

    with open(filename, "r") as f:
        r = csv.reader(f, delimiter=" ")
        for item in f:
            added_items = item.split(',')

    added_items[-1] = added_items[-1].rstrip('\n')

    for item in added_items:
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1

    return inventory


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename):

    with open(filename, "w") as f:
        w = csv.writer(f)
        key_list = []
        for key, value in inventory.items():
            for i in range(value):
                key_list.append(key)
        w.writerow(key_list)
