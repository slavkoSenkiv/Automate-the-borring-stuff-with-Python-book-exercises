"""
Write a function named displayInventory() that would take any possible
“inventory” and display it like the following:
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62""
"""

inventory = {'a': 1, 'b': 2, 'c': 3, 'd': 100}


def displayInventory(dic):
    total = 0
    print('Inventory contains:')
    for k, v in dic.items():
        print('- ' + k + ': ' + str(v))
        total += v
    print('TOTAL items are: ' + str(total))


displayInventory(inventory)