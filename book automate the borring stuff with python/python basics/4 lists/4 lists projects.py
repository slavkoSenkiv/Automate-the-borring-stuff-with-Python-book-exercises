
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

#The Dictionary Data Type
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])
print('my cat has ' + myCat['color'] + ' fur')

newDic ={1:'a', 2:'b'}
print(newDic[1])

birthday = {'alice': 'Apr 1', 'bob': 'Dec 12', 'Carol': 'Mar 14'}

while True:
    print('enter a name: (q to quit)')
    name = input()
    if name == 'q':
        break

    if name in birthday:
        print(birthday[name] + ' is the birthday of ' + name)
    else:
        print(' idk him/her')
        print('what is theit birthday?')
        bday = input()
        birthday[name] = bday
        print('birthday database updated')
"""






















