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

# Matching Specific Repetitions with Braces
import re

message = "HaHaHaHaHa"
regex = re.compile(r'(Ha){2}')
mo = regex.search(message)
print(mo.group())

# Matching with question mark
import re

message1 = "Admentures of Batman"
message2 = "Admentures of Batwoman"
regex = re.compile(r'Bat(wo)?man')
mo1 = regex.search(message1)
mo2 = regex.search(message2)
print(mo1.group())
print(mo2.group())

# Matching with question mark
import re

message1 = "+380675968763"
message2 = "0675968763"
regex = re.compile(r'(\+\d\d)?(\d\d\d\d\d\d\d\d)')
mo1 = regex.search(message1)
mo2 = regex.search(message2)

print(mo1.group(1))
print(mo1.group(2))
print(mo1.group())

print(mo2.group(1))
print(mo2.group(2))
print(mo2.group())

# Matching with star
import re

message1 = "Admentures of Batwoman"
message2 = "Admentures of Batwowoman"
message3 = "Admentures of Batwowowoman"
message4 = "Admentures of Batwoman & Batwowoman & Batwowowoman"
message5 = "Admentures of Batwowowoman & Batwoman & Batwowoman"
message6 = "Admentures of Batman"

regex = re.compile(r'Bat(wo)*man')

mo1 = regex.search(message1)
mo2 = regex.search(message2)
mo3 = regex.search(message3)
mo4 = regex.search(message4)
mo6 = regex.search(message6)

print(mo1.group())
print(mo2.group())
print(mo3.group())
print(mo4.group())
print(mo6.group())

import re
# The findall() Method
message = 'Cell: 3-22-09 Work: 3-44-52'
regex = re.compile(r'(\d)-(\d\d)-(\d\d)')
mo = regex.findall(message)

print(mo)

import re
# Character Classes
xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, \n '
                       '9 ladies, 8 maids, 7 swans, 6 geese, \n '
                       '5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

print(mo)

import re
# Making Your Own Character Classes

vowelRegex = re.compile(r'[aeiouAEIOU]')
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

import re

message = 'Hello there dear world'
regex = re.compile(r'[^aeiouyAEIOUY]') # all exept
regex2 = re.compile(r'[aeiouyAEIOUY]') # all in the brackets
mo = regex.findall(message)
mo2 = regex2.findall(message)
print(mo)
print(mo2)

import re
message = 'Hello there dear world'
regex = re.compile(r'^Hell')
mo = regex.search(message)
print(mo)

regex2 = re.compile(r'[ld$]')
mo2 = regex2.search(message)
print(mo2)

import re
message = '12345667890'
regex = re.compile(r'^\d+$')
mo = regex.search(message)
print(mo)

import re
message = 'The cat in the hat sat on the flat mat.'
regex = re.compile(r'.at')
print(regex.findall(message))

import re
regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = regex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

# Case-Insensitive Matching
import re

message = 'RoboCop is part man, part machine, all cop.'
message1 = 'ROBOCOP protects the innocent..'
message2 = 'Al, why does your programming book talk about robocop so much?.'

regex = re.compile(r'robocop', re.IGNORECASE)
print(regex.search(message).group())
print(regex.search(message1).group())
print(regex.search(message2).group())

# Substituting Strings with the sub() Method

import re
regex = re.compile(r'Agent \w+')
print(regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

import re
regex = re.compile(r'Agent (\w)\w*')
print(regex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

"""

# Managing Complex Regexes
import re
regex = re.compile(r'''(
(\d{3}|\(\d{3}\))?          # area code
(\s|-|\.)?                  # separator
\d{3}                       # first 3 digits
(\s|-|\.)                   # separator
\d{4}                       # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)

# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE




















