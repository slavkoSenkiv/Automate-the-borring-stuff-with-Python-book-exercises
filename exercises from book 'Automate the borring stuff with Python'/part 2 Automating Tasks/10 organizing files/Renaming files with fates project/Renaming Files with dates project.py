#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY format to European DD-MM-YYYY.
import re, shutil, os
# TODO: 1. Create regex that identifies text pattern of American-style dates.
datePattern = re.compile(r"""
    ^(.*?)          # all the text before the date
    ((0|1)?\d)-      # one or two digits for the month
    ((0|1|2|3)?\d)-  # one or two digits for the day
    ((19|20)\d\d)   # four digits for the year
    (.*?)$          # all the text after the dates
""", re.VERBOSE)

# Making an outline of the regular expression, with
# just the parentheses and group numbers, gives clearer understanding of your regex
''' 
datePattern = re.compile(r"""
    ^(1) # all text before the date
    (2 (3) )- # one or two digits for the month
    (4 (5) )- # one or two digits for the day
    (6 (7) ) # four digits for the year
    (8)$ # all text after the date
""", re.VERBOSE)
'''

# TODO: Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

# TODO: Skip files without a date.
    if mo == None:
        continue

# TODO: Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

# TODO: Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

# TODO: Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

# TODO: Rename the files.
    print(f'Ranaming "{amerFilename}" to {euroFilename}...')
    shutil.move(amerFilename, euroFilename) # uncomment after texting





