"""
#dicionaries and structuring data.py
#The Dictionary Data Type
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




