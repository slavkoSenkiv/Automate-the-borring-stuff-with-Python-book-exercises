"""
program shoud find combitations that are numbers and write tem down in different variations of text
'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

"""

"""
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(9, 12):
        if not text[i].isdecimal():
            return False
    return True

print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))

"""

"""

# if there is a planty of text
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

print('start')


def checkRequirements(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(9, 12):
        if not text[i].isdecimal():
            return False
    return True


for i in range(len(message)):
    possiblePhoneNumberCombination = message[i:i+12]
    if checkRequirements(possiblePhoneNumberCombination):
        print('Phone number found: ' + possiblePhoneNumberCombination)

print('done')
"""


"""
# if there is a planty of text
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

print('start')


def checkRequirements(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(9, 12):
        if not text[i].isdecimal():
            return False
    return True


for i in range(len(message)):
    possiblePhoneNumberCombination = message[i:i+12]
    if checkRequirements(possiblePhoneNumberCombination):
        print('Phone number found: ' + possiblePhoneNumberCombination)

print('done')

import re
message = ' hello there 3434'
numberRegex = re.compile(r'\d\d\d')
case = numberRegex.search(message)
print('here it is ' + case.group())
"""
# More Pattern Matching with Regular Expressions

"""
# Grouping with Parentheses

import re
message = ' hello there 1-22-333'
numberRegex = re.compile(r'(\d)-(\d\d)-(\d\d\d)')
case = numberRegex.search(message)
print('here it is g1 ' + case.group(1))
print('here it is g2 ' + case.group(2))
print('here it is g3 ' + case.group(3))
print('here it is whole group ' + case.group())

# Grouping with Parentheses

import re
message = ' hello there 1-22-333'
numberRegex = re.compile(r'(\d)-(\d\d)-(\d\d\d)')
case = numberRegex.search(message)
print('here it is whole group ' + case.group())
firstNum, secNum, thirdNum = case.groups()
print('1 ' + firstNum)
print('2 ' + secNum)
print('2 ' + thirdNum)

# Grouping with Parentheses if there is parentheses

import re
message = ' hello there 1-(22)-333'
numberRegex = re.compile(r'(\d)-(\(\d\d\))-(\d\d\d)')
case = numberRegex.search(message)
print('here it is whole group ' + case.group())
firstNum, secNum, thirdNum = case.groups()
print('1 ' + firstNum)
print('2 ' + secNum)
print('2 ' + thirdNum)

# Grouping with Parentheses if there is parentheses

import re
message = ' hello there 1-(22)-333'
numberRegex = re.compile(r'(\d)-(\(\d\d\))-(\d\d\d)')
case = numberRegex.search(message)
print('here it is whole group ' + case.group())
firstNum, secNum, thirdNum = case.groups()
print('1 ' + firstNum)
print('2 ' + secNum)
print('2 ' + thirdNum)

# Matching Multiple Groups with the Pipe
import re

message = ' Batman, Flesh, Superman, Iron, Man, Tina'

heroRegex = re.compile(r'Batman|Tina')
case = heroRegex.search(message)
print(case.group())

# Matching Multiple Groups with the Pipe
import re

message = 'Batmobile lost a wheel'

heroRegex = re.compile(r'Bat(man|mobile|copter|bat)')
case = heroRegex.search(message)
print(case.group())
print(case.group(1))

# Optional Matching with the Question Mark
import re
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('the adventures of Batman')
print('1 ' + mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print('2 ' + mo2.group())

# Optional Matching with the Question Mark

import re

phoneRegex = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')

mo = phoneRegex.search('My phone number is 415-555-4242')
print(mo.group(1))
print(mo.group(2))
print(mo.group())

# Optional Matching with the Question Mark
import re
batRegex = re.compile(r'(петро)?(миро)?(яро)?слав')
mo1 = batRegex.search('сеньків ярослав миколайович')
print('1 ' + mo1.group())
mo2 = batRegex.search('сеньків мирослав миколайович')
print('2 ' + mo2.group())
mo3 = batRegex.search('сеньків петрослав миколайович')
print('3 ' + mo3.group())
(\(\+\d\d\d\))(\d\d\d\d\d\d\d\d\d\d)

# Matching Zero or More with the Star
import re
message = 'іва івпа впапрапр Петрослав Ярослав вапвапва Петрослав вапвапвпва Святослав мають телен   (+380)3-22-09 s (+38)0675968763 і'

phoneRegex = re.compile(r'(\(\+\d\d\))(\d\d\d\d\d\d\d\d)')
myNameRegex = re.compile(r'Ярослав')
anySlavName = re.compile(r'(Яро|Петро|Свято)слав')

moNumber = phoneRegex.search(message)
moMyName = myNameRegex.search(message)
moSlavName = anySlavName.search(message)

print(moNumber.group(1))
print(moNumber.group(2))
print(moNumber.group())

print(moMyName.group())
print(moSlavName.group())

"""

# Matching Specific Repetitions with Braces


















