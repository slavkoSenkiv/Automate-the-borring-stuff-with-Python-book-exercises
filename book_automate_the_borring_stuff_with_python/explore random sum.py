
import random

listOne = []
listTwo = []
volume = 1000000
sumOfListOne = 0
sumOfListTwo = 0

for i in range(volume):
    listOne.append(random.randint(0, 3))
    listTwo.append(random.randint(0, 3))
    sumOfListOne += listOne[i]
    sumOfListTwo += listTwo[i]

print(sumOfListOne)
print(sumOfListTwo)

print('the 1st list coef = ' + str(sumOfListOne / volume))
print('the 2d  list coef = ' + str(sumOfListTwo / volume))

# print('1st list sum = ' + str(sumOfListOne))
# print('2d list sum = ' + str(sumOfListTwo))
