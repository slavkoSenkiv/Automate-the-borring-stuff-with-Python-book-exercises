"""
#comma code
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test
the case where an empty list [] is passed to your function.

def commaFunction(parametr):
        listLen = len(parametr)
        if listLen >= 3:
            for i in range(listLen - 1):
                print(str(list[i]) + ', ' , end='')
            print('and ' + str(parametr[-1]))
        if listLen == 0:
            print('list is empty')
        if listLen == 1:
            print(str(parametr[0]) + ' and that it')
        if listLen == 2:
            print(str(parametr[0]) + ', ' + str(parametr[1]))

list = [1, 2]
commaFunction(list)

#Coin Flip Streaks my variant
import random
flips = 0

while flips <= 100:
    sideOfCoin = random.randint(0, 1)
    if sideOfCoin == 0:
        side = 'H'
    else:
        side = 'T'
    print(side, end='')
    flips = flips + 1

print(0)
import random
lineOfFlips = []

for numberOfFlips in range (10000):
    sideOfCoin = random.randint(0, 1)
    if sideOfCoin == 0:
        side = 'H'
    else:
        side = 'T'
    lineOfFlips.append(side)
print(lineOfFlips)


#Coin Flip Streaks
print(1)

theCases = 0
for index in range(9999):
    if lineOfFlips[index] == 'H' and lineOfFlips[index + 1] == 'H' and lineOfFlips[index + 2] == 'H' and lineOfFlips[index + 3] == 'H' and lineOfFlips[index + 4] == 'H' and lineOfFlips[index + 5] == 'H':
        print('There are 6 H starting at the index ' + str(index))
        theCases += 1
    elif lineOfFlips[index] == 'T' and lineOfFlips[index + 1] == 'T' and lineOfFlips[index + 2] == 'T' and lineOfFlips[index + 3] == 'T' and lineOfFlips[index + 4] == 'T' and lineOfFlips[index + 5] == 'T':
        print('There are 6 T starting at the index ' + str(index))
        theCases += 1

print('there are ' + str(theCases) + ' cases')

#character Picture Grid
#        X 0    1    2    3    4    5        Y
grid =  [['.', '.', '.', '.', '.', '.'],    #0
         ['.', 'O', 'O', '.', '.', '.'],    #1
         ['O', 'O', 'O', 'O', '.', '.'],    #2
         ['O', 'O', 'O', 'O', 'O', '.'],    #3
         ['.', 'O', 'O', 'O', 'O', 'O'],    #4
         ['O', 'O', 'O', 'O', 'O', '.'],    #5
         ['O', 'O', 'O', 'O', '.', '.'],    #6
         ['.', 'O', 'O', '.', '.', '.'],    #7
         ['.', '.', '.', '.', '.', '.']]    #8

for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x], end='')
    print(' ')
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

print('hello GitHub')
