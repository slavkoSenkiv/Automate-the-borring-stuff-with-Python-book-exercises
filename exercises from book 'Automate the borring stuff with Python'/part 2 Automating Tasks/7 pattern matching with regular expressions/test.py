"""listOfLists = [['ab'], ['cd'], ['ef']]
print('listOfLists → ' + str(listOfLists))
print('listOfLists[1] → ' + str(listOfLists[1]))
listOfLists[1] = list('q') + listOfLists[1]
print('listOfLists[1] → ' + str(listOfLists[1]))

    ([0-3][0-9]|[1-9])                  # day
    (\.|,|-|/|\\|\s)                    # separator
    ([0-1][0-2]|[1-9])                  # month
    (\.|,|-|/|\\|\s)                    # separator
    ([1-2][0-9][0-9][0-9]|[0-9][0-9])   # year
"""

import re
message1 = 'random test 1.12.23 and 1.12.2223 '
message2 = 'random test 1.12.2223 '
numRegex = re.compile(r'''
    ([12][0-9]|3[0-1]|0?[1-9])             # to detect days from 1 to 31
    ([./-])                                # to detect different separations
    (1[0-2]|0?[1-9])                       # to detect number of months
    ([./-])                                 # to detect different seperations
    (2?1?[0-9][0-9][0-9])                  # to detect number of years from 1000-2999 years
''', re.VERBOSE)

print(numRegex.findall(message1))
print(numRegex.findall(message2))



