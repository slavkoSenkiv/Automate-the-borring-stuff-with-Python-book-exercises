import ezsheets
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

"""
# Reading and Writing Entire Columns and Rows



