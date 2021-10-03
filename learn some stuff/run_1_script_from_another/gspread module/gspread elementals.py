import time
"""
gspread
123
1.54

ezsheets
123
2.24

gspread
123
1.5

ezsheets
123
2.25

"""

start_gspread = time.time()
import gspread
gc = gspread.oauth()
gs = gc.open('test gs')
sheet = gs.get_worksheet(0)
print('gspread')
print(sheet.acell('A1').value)
print(round(time.time() - start_gspread, 2))

start_ezsheets = time.time()
import ezsheets
gs_name = 'test gs'
gs_ezsheets = ezsheets.Spreadsheet(gs_name)
sheet = gs_ezsheets['Sheet1']
print('ezsheets')
print(sheet['A1'])
print(round(time.time() - start_ezsheets, 2))



