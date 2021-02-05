
"""
Say you wanted your program to store data about your friends’ birthdays. You can use
a dictionary with the names as keys and the birthdays as values
"""
birthdays = {'a': 1, 'b': 2, 'c': 3}

while True:
    print('enter a name')
    name = input()
    if name == 'q':
        print('bye')
        break
    if name in birthdays:
        print(name + ' has birthday at ' + str(birthdays[name]))
    else:
        print('idk him/her, enter her birthday')
        newBDay = input()
        birthdays[name] = newBDay
        print('bdays database is updated')