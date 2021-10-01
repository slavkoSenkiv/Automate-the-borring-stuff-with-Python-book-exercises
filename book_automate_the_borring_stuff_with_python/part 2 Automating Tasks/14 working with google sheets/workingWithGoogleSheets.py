import ezsheets
from googleapiclient.errors import HttpError
"""
# Creating, Uploading, and Listing Spreadsheets
ss1 = ezsheets.Spreadsheet('1VQgFJmMew4RGkyY5sLV8qiXQVL7zf8VQrvju3E8m5SI')
print(1, ss1)
print(1, ss1.title)
ss2 = ezsheets.Spreadsheet('test GSheet')
print(2, ss2)
print(2, ss2.title)
ss3 = ezsheets.Spreadsheet('https://docs.google.com/spreadsheets/d/1VQgFJmMew4RGkyY5sLV8qiXQVL7zf8VQrvju3E8m5SI/edit#gid=0')
print(3, ss3)
print(3, ss3.title)
ss = ezsheets.createSpreadsheet('python created spreadsheet')
print(ss.title)
ss = ezsheets.upload('ЦА.xlsx')
print(ss.title)

print(ezsheets.listSpreadsheets())

for spreadsheet in ezsheets.listSpreadsheets():
    print(spreadsheet)
    
ss = ezsheets.createSpreadsheet('demo')
print(ss.title)

# Spreadsheet Attributes
ss = ezsheets.Spreadsheet('1WJ0iN_JfGaNg7XjQlw9fiY0ZTLb0ivMax-4tT0tVPSI')
print(ss.title)
# ss.title = 'сімейні фінанси'
# print(ss.title)
print(ss.spreadsheetId)
print(ss.url)
print(ss.sheetTitles)
print(ss.sheets)
print(ss[0])
print(ss['видатки'])
ss.refresh()

# Downloading and Uploading Spreadsheets

ss = ezsheets.Spreadsheet('1WJ0iN_JfGaNg7XjQlw9fiY0ZTLb0ivMax-4tT0tVPSI')
print(ss.title)

ss.downloadAsExcel()
ss.downloadAsExcel('another name.xlsx')
ss.downloadAsHTML()
ss.downloadAsPDF()

# Deleting Spreadsheets
ss = ezsheets.Spreadsheet('Delete me 1')
print(ezsheets.listSpreadsheets())
ss.delete(permanent=True)
print(ezsheets.listSpreadsheets())

# Reading and Writing Data
ss = ezsheets.Spreadsheet('My Test Spreadsheet')
sheet = ss[0]  # Get the first sheet in this spreadsheet.
print(1, sheet.title)

sheet['A1'] = 'Name'  # Set the value in cell A1.
sheet['B1'] = 'Age'
sheet['C1'] = 'Favorite Movie'

print(2, sheet['A1'])  # Read the value in cell A1.
print(3, sheet['A2'])  # Empty cells return a blank string.
print(4, sheet[2, 1])  # Column 2, Row 1 is the same address as B1.

sheet['A2'] = 'Alice'
sheet['B2'] = 30
sheet['C2'] = 'RoboCop'

# Column and Row Addressing
print(ezsheets.convertAddress('A2'))
print(ezsheets.convertAddress(1, 2))
print(ezsheets.getColumnLetterOf(2))
print(ezsheets.getColumnLetterOf(999))
print(ezsheets.getColumnNumberOf('B'))
print(ezsheets.getColumnNumberOf('ZZZ'))

# Reading and Writing Entire Columns and Rows
ss = ezsheets.Spreadsheet('1XLzCCTjhX2DECuwpIlCh7Vhdkdj2GV79s7EYvy09LRE')
sheet = ss[0]
print(1, sheet.getRow(1))
print(2, sheet.getColumn(1))
print(3, sheet.getColumn(2))
print(4, sheet.getColumn(3)[:10])
print(5, sheet.updateRow(3, ['Pumpkin', '11.50', '20', '230']))
column_one = sheet.getColumn(1)
for cell, value in enumerate(column_one):
    column_one[cell] = value.upper()

print(6, sheet.updateColumn(1, column_one))
print(7, sheet.getColumn(1)[:10])

# Reading and Writing Entire Columns and Rows
ss = ezsheets.Spreadsheet('1XLzCCTjhX2DECuwpIlCh7Vhdkdj2GV79s7EYvy09LRE')
sheet = ss[0]
column_one = sheet.getColumn(1)[1:10]
print(column_one)

for cell in range(0, len(column_one)):
    print(cell, column_one[cell])

print()

for cell, value in enumerate(column_one):
    print(cell, value)
    
rows = sheet.getRows()
print(rows[0])
rows[1][0] = 'test'
print(rows[1][0])
sheet.updateRows(rows)



print(sheet.rowCount)
print(sheet.columnCount)

sheet.columnCount = 4
sheet.rowCount = 10

# Creating and Deleting Sheets
ss = ezsheets.Spreadsheet('1XLzCCTjhX2DECuwpIlCh7Vhdkdj2GV79s7EYvy09LRE')
sheet = ss[0]
print(ss.sheetTitles)
try:
# ss.createSheet('Span', 0)
#ss.refresh()
print(ss.sheetTitles)
except HttpError:
print('1')
ss['Span'].delete()

# Copying Sheets
ss = ezsheets.Spreadsheet('1XLzCCTjhX2DECuwpIlCh7Vhdkdj2GV79s7EYvy09LRE')
ss2 = ezsheets.createSpreadsheet('Second Spreadsheet')
ss[1].copyTo(ss2)
"""


