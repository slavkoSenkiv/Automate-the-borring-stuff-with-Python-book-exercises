import re

message = 'hello there 2 34 56'

dateRegex = re.compile(r'''(

    (\d\d|\d)           # day
    (\.|,|-|/|\\|\s)    # separator
    (\d\d|\d)           # month
    (\.|,|-|/|\\|\s)    # separator
    (\d\d\d\d|\d\d)     # year
    
    )''', re.VERBOSE)

matches = []

for groups in dateRegex.findall(message):
    if len(groups[1]) == 1:
        print('len groups[1] ( number ' + groups[1] + ') = 1')
        groups[1] = list('0') + groups[1]
"""    if len(groups[1]) == 2:
        print('len groups[1] ( number ' + groups[1] + ') = 2')
        print(groups[1][0])
"""

date = '.'.join([groups[1], groups[3], groups[5]])
matches.append(date)

if len(matches) > 0:
    print('these are matches')
    print('\n'.join(matches))
else:
    print('there is no matches')



