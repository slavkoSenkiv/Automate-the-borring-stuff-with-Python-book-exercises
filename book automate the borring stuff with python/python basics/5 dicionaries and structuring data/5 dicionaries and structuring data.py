"""
#dicionaries and structuring data.py
#The Dictionary Data Type

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
         print('I do not have birthday information for ' + name)
         print('What is their birthday?')
         bday = input()
         birthdays[name] = bday
         print('Birthday database updated.')

birthdays = {'a': 1, 'b': 2, 'c': 3}

while True:
    print('enter the name')
    name = input()
    if name == 'q':
        break

    if name in birthdays:
        print('the bday of ' + name + ' is ' + str(birthdays[name]))
    else:
        print('there is not that name in the base')
        print('enter his bday')
        newBDay = input()
        birthdays[name] = newBDay
        print('bday base updated')

#The keys(), values(), and items() Methods

spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

spam = {'color': 'red', 'age': 42}
print(type(spam.keys()))
print(list(spam.keys()))

spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key ' + k + ' has value ' + str(v))

spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key ' + k + ' has value ' + str(v))

#Checking Whether a Key or Value Exists in a Dictionary

spam = {'name': 'Zophie', 'age': 7}
if 'name' in spam.keys():
    print(1)
if 'Zophie' in spam.values():
    print(2)
if 'color' in spam.keys():
    print(3)
if 'color' not in spam.values():
    print(4)

items ={'apples': 5, 'cups': 2}
print('im bringing ' + str(items.get('cups', 0)) + ' cups')
print('im bringing ' + str(items.get('eggs', 0)) + ' eggs')

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('name', 'sam')
print(spam)

"""




