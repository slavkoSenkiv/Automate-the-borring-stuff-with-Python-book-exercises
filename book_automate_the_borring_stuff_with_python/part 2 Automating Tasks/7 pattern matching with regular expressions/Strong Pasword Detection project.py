# last repeat 23.02.21
"""
+ AT LEAST 8 character long
+ does not contain special characters
- contains BOTH uppercase and lowercase
- has AT LEAST 1 digit
"""

import re
def passValid(password):
    numRegex = re.compile(r'[0-9]+')
    lowerCaseRegex = re.compile(r'[a-z]+')
    upperCaseRegex = re.compile(r'[A-Z]+')
    totalRegex = re.compile(r'[0-9A-Za-z]{8,}')
    characterRegex = re.compile(r'[^0-9A-Za-z]')

    passScore = 0

    if numRegex.search(password):
        passScore += 1
    if lowerCaseRegex.search(password):
        passScore += 1
    if upperCaseRegex.search(password):
        passScore += 1
    if totalRegex.search(password):
        passScore += 1
    if characterRegex.search(password):
        passScore -= 1

    if passScore == 4:
        print('pass is good')
    else:
        print('pass is bad')

x = 'a97qweqf'
passValid(x)