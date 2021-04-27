"""
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))


import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
print(wb.sheetnames) # the workbook sheet names

sheet = wb['Sheet3'] # get the sheet from the work book
print(sheet)

print(type(sheet))

print(sheet.title) # get the sheets title as a string

anotherSheet = wb.active # get the active sheet
print(anotherSheet)

# Getting Cells from the Sheets

import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1'] # get the sheet from the workbook
print(sheet['A1']) # get a cell from a sheet
print(sheet['a1'].value) # get the value from a cell
c = sheet['b1'] # get another cell from the sheet
print(c.value)
# get a row, a column a cell from the sheet
print('row %s, column %s is %s' % (c.row, c.column, c.value))
print('cell %s is %s' % (c.coordinate, c.value))
print(sheet['c1'].value)

print(sheet.cell(row=1, column=2))
print(sheet.cell(row=1, column=2).value)
for i in range(1, 8, 2): # go through every other row:
    print(i, sheet.cell(row=i, column=2).value)

import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
print(sheet.max_row)  # get the highest row number
print(sheet.max_column) # get the highest column number

# Converting Between Column Letters and Numbers
import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string
print(get_column_letter(1)) # translate column 1 to a letter
print(get_column_letter(2))
print(get_column_letter(27))
print(get_column_letter(900))

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
print(get_column_letter(sheet.max_column))
print(column_index_from_string('A')) # get a's number
print(column_index_from_string('AA'))


import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
print(tuple(sheet['a1':'c3'])) # get all cells from a1 to c3
for rowOfCellObjects in sheet['a1':'c3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('___ END OF ROW ___')
"""
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
print(list(sheet.columns)[1]) # get second column cell
for cellObj in list(sheet.columns)[1]:
    print(cellObj.value)




