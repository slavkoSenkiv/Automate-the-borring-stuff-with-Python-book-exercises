import shutil, re, os

datePattern = re.compile(r'''
    ^(.*?) # any text before date
    ((0|1)\d)- # month
    ((0|1|2|3)\d)- # day
    ((19|20)\d\d) # year
    (.*?)$ # any text after date
''', re.VERBOSE)

filesToCheck = os.listdir('.')
for amerFileName in filesToCheck:
    mo = datePattern.search(amerFileName)
    if mo == None:
        continue
    else:
        beforePart = mo.group(1)
        monthPart = mo.group(2)
        dayPart = mo.group(4)
        yearPart = mo.group(6)
        afterPart = mo.group(8)

        euroFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

        # direction
        absWorkingDir = os.path.abspath('.')
        amerFileName = os.path.join(absWorkingDir, amerFileName)
        euroFileName = os.path.join(absWorkingDir, euroFileName)

        print(f'{amerFileName} was renamed to {euroFileName}')

        shutil.move(amerFileName, euroFileName)