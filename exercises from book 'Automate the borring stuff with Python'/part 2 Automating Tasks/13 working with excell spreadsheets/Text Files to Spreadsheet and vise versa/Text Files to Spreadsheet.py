import openpyxl
import os
from pathlib import Path

wb = openpyxl.Workbook()
sheet = wb.active

fileNameColumn = 1
lineRow = 1

for fileName in os.listdir(Path.cwd()):
    if fileName.endswith('.txt'):
        print('\n', fileName, '\n')
        txtFile = open(fileName, 'r')  # column

        rowNum = 1
        for lines in txtFile:
            print(lines, '\n')
            sheet.cell(column=fileNameColumn, row=lineRow).value = lines
            lineRow += 1
        fileNameColumn += 1
        lineRow = 1

wb.save('testSheet.xlsx')
