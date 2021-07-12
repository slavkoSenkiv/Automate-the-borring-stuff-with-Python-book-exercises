num = 645
print('num =', num)

withoutHundreds = num % 100
firstNum = int((num - withoutHundreds)/100)
thirdNum = withoutHundreds % 10
secondNum = int((num - (num - withoutHundreds) - thirdNum)/10)

print('firstNum = ', firstNum, '\nthirdNum =', thirdNum, '\nsecondNum =', secondNum, '\n')

if (firstNum > secondNum) and (firstNum > thirdNum):
   largest = firstNum
elif (secondNum > firstNum) and (secondNum > thirdNum):
   largest = secondNum
else:
   largest = thirdNum

if (firstNum < secondNum) and (firstNum < thirdNum):
   smallest = firstNum
elif (secondNum < firstNum) and (secondNum < thirdNum):
   smallest = secondNum
else:
   smallest = thirdNum

if (firstNum < secondNum) and (firstNum > thirdNum):
   middle = firstNum
elif (secondNum < firstNum) and (secondNum > thirdNum):
   middle = secondNum
elif (thirdNum < firstNum) and (thirdNum > secondNum):
   middle = thirdNum

print("The largest number is", largest, "\nThe smallest number is", smallest, "\nThe middle number is", middle)
newNum = str(largest) + str(middle) + str(smallest)
print('\nnewNum =', newNum)





