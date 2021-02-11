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





