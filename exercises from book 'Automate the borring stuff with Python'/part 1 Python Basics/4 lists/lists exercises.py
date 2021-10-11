"""

#Getting a List from Another List with Slices

spam = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(spam[0:3])

#Getting a List’s Length with the len() Function

spam = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
len(spam[5:])

spam = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
text = ['a', 'b', 'c', 'd']
print(len(text))

#Changing Values in a List with Indexes

spam = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
text = ['a', 'b', 'c', 'd']
print(spam)
spam[1] = 'a'
print(spam)

#List Concatenation and List Replication

spam = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
text = ['a', 'b', 'c', 'd']
newList = spam + text
print(newList)

spam = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
text = ['a', 'b', 'c', 'd']
newList = spam * 2
print(newList)

#Removing Values from Lists with del Statements

spam = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(spam)
print(len(spam))
del spam[1]
print(spam)
print(len(spam))

#working with lists my version

myCats = [0, 1, 2, 3, 4]
listIndex = 0
while listIndex < 5:
    print('enter cat name')
    myCats[listIndex] = input()
    listIndex = listIndex + 1
else:
    print('I have ' + str(listIndex) + ' cats. Their names are: ' + str(myCats))

#cat names exercise after reading the book
catNames = []
while True:
    print('enter the name of the cat #' + str(len(catNames) + 1) + ' or "done" to stop')
    name = input()
    if name == 'done':
        break
    catNames = catNames + [name]
print('I have ' + str(len(catNames) + 1) + ' cats. Their names are: ' + str(catNames))

##cat names exercise the book version
catNames = []
while True:
    print('enter the name of the cat #' + str(len(catNames) + 1) + ' or "done" to stop')
    name = input()
    if name == 'done':
        break
    catNames = catNames + [name]
print('I have ' + str(len(catNames)) + ' cats')
print('Their names are: ')
for name in catNames:
    print(' ' + name)

#Using for Loops with Lists
for i in range(4):
    print(i)

for i in [1, 2, 3, 4]:
    print(i)

cats = [1, 2, 3, 4]
for i in range(len(cats)):
    print('here it is ')

supplies = ['a', 'b', 'c']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in suplies is ' + supplies[i])

#The in and not in Operators
if 5 in [1, 2, 4]:
    print(True)
else:print(False)

spam =  [1, 2, 4]
if 6 in spam:
    print(True)
else:print(False)

import sys
myPets = []
while True:
    print('enter your cat name')
    name = input()
    if name == 'done':
        break
    myPets = myPets + [name]
print('now check you pets')

while True:
    check = input()
    if check in myPets:
        print('yh')
    if check not in myPets:
        print('no')

#The Multiple Assignment Trick
cat = ['a', 'b', 'c']
size, color, name = cat
print('the cat name is ' + name + ' the size is ' + size + ' and colour is ' + color)

#Using the enumerate() Function with Lists
supplies = ['a','b','c']
for index, item in enumerate(supplies):
    print('index ' + str(index) + ' in supplies list: ' + item)

#Using the random.choice() and random.shuffle() Functions with Lists
import random
pets = ['a','b','c']
print(random.choice(pets))

#Augmented Assignment Operators
x = 1
while x < 5:
    print(x)
    x += 1

x = 'hello'
x += ' world'
print(x)

y = 'a '
y *= 3
print(y)

#Finding a Value in a List with the index() Method
x = [1, 2, 3]
print(x.index(4))

#Adding Values to Lists with the append() and insert() Methods
x = [1, 2, 3]
x.append(10)
print(x)

x.insert(0, 'a')
print(x)

#Removing Values from Lists with the remove() Method
x = [1, 2, 3, 4]
x.remove(2)
print(x)

x = [1, 2, 3, 4]
del x[0]
print(x)

#Sorting the Values in a List with the sort() Method

x = [2, 3, 1, 5, 4, 7, 5, 5 , 4.1]
x.sort()
print(x)

#treat all the items in the list as if they were lowercase
x = ['a','c','f','d','A','Z','R','B']
x.sort(key=str.lower)
print(x)

#Reversing the Values in a List with the reverse() Method
x = [1, 2, 3]
x.reverse()
print(x)

import random
x = ['a','b','c','d','d','e','f']
print(x[random.randint(0, len(x)-1)])

x = 'Zophie'
for i in x:
    print('*** '+ i + ' ***')

#Mutable and Immutable Data Types
x = 'Zophie a cat'
newX = x[0:6] + ' the' + x[8:12]
print(newX)

#Converting Types with the list() and tuple() Functions

#PassingReferences
def x(someParametr):
    someParametr.append('hello')

spam = [1, 2, 3]
x(spam)
print(spam)
"""






















