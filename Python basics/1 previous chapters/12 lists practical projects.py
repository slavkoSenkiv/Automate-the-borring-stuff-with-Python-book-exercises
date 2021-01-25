
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
"""

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

index = 0
while index <= 10000:
    if lineOfFlips[index] == 'H':
        print('H has this index' + index)
        index = index + 1















