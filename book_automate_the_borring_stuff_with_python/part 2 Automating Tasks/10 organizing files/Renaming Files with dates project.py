#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY format to European DD-MM-YYYY.
import re, shutil, os
# TODO: 1. Create regex that identifies text pattern of American-style dates.
datePattern = re.compile(r"""
    ^(.*?)          # all the text before the date
    ((0|1)?\d)      # one or two digits for the month
    ((0|1|2|3)?\d)  # one or two digits for the day
    ((19|20)\d\d)   # four digits for the year
    (.*?)$          # all the text after the dates

""", re.VERBOSE)



# TODO: 2. Call os.listdir() to find all the files in the working directory.
# TODO: 3. Loop over each filename, using regex to check whether it has date.
# TODO: 4. If it has a date, rename the file with shutil.move().


