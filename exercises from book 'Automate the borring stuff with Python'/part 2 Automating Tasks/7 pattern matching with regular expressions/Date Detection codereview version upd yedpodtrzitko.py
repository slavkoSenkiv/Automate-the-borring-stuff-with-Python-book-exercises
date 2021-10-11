# there is datetime validation and this is not a part of a task

import re
from datetime import date

def date_detector(text):
    date_pattern = re.compile('''
    ([12][0-9]|3[0-1]|0?[1-9])             # to detect days from 1 to 31
    ([./-])                                # to detect different separations
    (1[0-2]|0?[1-9])                       # to detect number of months
    ([./-])                                # to detect different seperations
    (2?1?[0-9][0-9][0-9])                  # to detect number of years from 1000-2999 years
        ''', re.VERBOSE)

    # use only one list for storing all parts of match together
    parsed = []
    for match in date_pattern.findall(text):
        # year, month, day for easier passing to date()
        parsed.append([ int(match[4]), int(match[2]), int(match[0])] )

    valid = []
    for item in parsed:
        try:
            # pass list of [year, month, day] to date() and let it check its validity for us
            date(*item)
        except ValueError as e:
            pass # invalid date, dont do anything
        else:
            valid.append(item)

    for item in valid:
        print(item)

data = '30-06-2012, 31-12-2012, 15-02-2002, 29-02-2004, 29-02-2002, 31-02-2004, 31-06-2012'

date_detector(data)