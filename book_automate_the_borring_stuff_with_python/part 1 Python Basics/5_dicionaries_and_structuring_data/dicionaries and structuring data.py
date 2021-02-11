"""
# ____ dictionaries and structuring data.py
# ____ The Dictionary Data Type
# ____ The keys(), values(), and items() Methods

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

# ____ Checking Whether a Key or Value Exists in a Dictionary

spam = {'name': 'Sophie', 'age': 7}
if 'name' in spam.keys():
    print(1)
if 'Sophie' in spam.values():
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

# ___ The keys(), values(), and items() Methods


dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# ___ dic methods
print(dic.keys())
print(dic.values())
print(dic.items())

# for loops with these methods
for v in dic.values():
    print(v)

for k in dic.keys():
    print(k)

for i in dic.items():
    print(i)

# convert method's output into lists
print(list(dic.keys()))
print(list(dic.values()))
print(list(dic.items()))

# convert tuples from the .item method into lists and modify them
x = list(dic.items())
x.append('d')
print(x)
print(list(x[0]))

# get key and valuables from dics separately
for k, v in dic.items():
    print(' Key here is ' + k + ' and the value here is ' + str(v))



# ____ Checking Whether a Key or Value Exists in a Dictionary

dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
if 'g' in dic.keys():
    print('+')
else:
    print('no')

if 6 in dic.values():
    print('+')
else:
    print('no')

if ('b', 2) in dic.items():
    print('+')
else:
    print('no')


# ____ The get() Method

print('the letter A has ' + str(alphabet.get('g', 9)) + ' number')
print(str(alphabet.get('a', 'x')))



# ___ Adding values to the dic
alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
alphabet['e'] = 5
print(alphabet['e'])


# ___ The setdefault() Method
alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
alphabet.setdefault('e', 5)
print(alphabet)
alphabet.setdefault('a', 3)
print(alphabet)

# ___ character count exercise

message = 'a bb ccc aa'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
"""
# Nested Dictionaries and Lists

allGuests = {'alice': {'apple':  1, 'orange': 2},
            'bob':   {'orange': 3, 'carrot': 4},
            'mike':  {'carrot': 1, 'tomato': 5}}


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought += v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - apple ' + str(totalBrought(allGuests, 'apple')))
print(' - orange ' + str(totalBrought(allGuests, 'orange')))
print(' - carrot ' + str(totalBrought(allGuests, 'carrot')))
print(' - tomato ' + str(totalBrought(allGuests, 'tomato')))
print('TOTAL: ' + str(totalBrought(allGuests, 'apple') + totalBrought(allGuests, 'orange') + \
totalBrought(allGuests, 'carrot') + totalBrought(allGuests, 'tomato')))












