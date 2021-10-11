"""while True:
    age = input('enter age: ')
    try:
        age = int(age)
    except:
        print('enter digits')
        continue
    if age < 1:
        print('pls enter positive number')
        continue
    break

    import pyinputplus
age = pyinputplus.inputEmail(prompt='enter mail...')


# The min, max, greaterThan, and lessThan Keyword Arguments
import pyinputplus as pyip
x = pyip.inputNum('enter num: x ', min=3)
y = pyip.inputNum('enter num: y ', greaterThan=10)
z = pyip.inputNum('enter num: z ', max=5)
a = pyip.inputNum('enter num: a ', lessThan=10)

print(x, y, z, a)

# The blank Keyword Argument
import pyinputplus as pyip

a = pyip.inputNum('entre num: ', blank=True)
b = pyip.inputNum('entre num: ', blank=True)
print('a', a)
print('b', b)

# The limit, timeout, and default Keyword Arguments
import pyinputplus as pyip

a = pyip.inputNum('entre num a : ', limit=3)
b = pyip.inputNum('entre num b : ', timeout=10)
c = pyip.inputNum('entre num c : ', limit=2, default=100)
d = pyip.inputNum('entre num d : ', limit=2, default='dont know')
print('a', a)
print('b', b)
print('c', c)
print('d', d)

# The allowRegexes and blockRegexes Keyword Arguments
import pyinputplus as pyip

# a = pyip.inputNum('entre num a : ', allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
# b = pyip.inputNum('entre num b : ', blockRegexes=[r'[1-5]$'])
c = pyip.inputNum('entre num c : ', allowRegexes=[r'1'], blockRegexes=[r'[1-2]'])

# print('a', a)
# print('b', b)
print('c', c)

# Passing a Custom Validation Function to i     nputCustom()
import pyinputplus as pyip

def validNumber(number):
    numberList = list(number)
    summOfNumbers = 0
    for digit in numberList:
        summOfNumbers += int(digit)
    if summOfNumbers != 10:
        raise Exception('the digits sum must be 10, not %s.' % (summOfNumbers))
    else:
        print('+')

response = pyip.inputCustom(validNumber)

    """
# Passing a Custom Validation Function to i     nputCustom()
import pyinputplus as pyip

def validNumber(number):
    numberList = list(number)
    summOfNumbers = 0
    for digit in numberList:
        summOfNumbers += int(digit)
    if summOfNumbers != 10:
        raise Exception('the digits sum must be 10, not %s.' % (summOfNumbers))
    else:
        print('+')

response = pyip.inputCustom(validNumber)







