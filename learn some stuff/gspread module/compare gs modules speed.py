import time
import pygsheets
import ezsheets
import gspread
gs_name = 'test gs'

# <editor-fold desc="gspread">
start_gspread = time.time()
gc = gspread.oauth()
gs = gc.open(gs_name)
sheet = gs.get_worksheet(0)
print('gspread')
print(sheet.acell('A1').value)
gspread_time = round(time.time() - start_gspread, 2)
# </editor-fold>

# <editor-fold desc="ezsheets">
start_ezsheets = time.time()
gs_ezsheets = ezsheets.Spreadsheet(gs_name)
sheet = gs_ezsheets['Аркуш1']
print('ezsheets')
print(sheet['A1'])
ezsheets_time = round(time.time() - start_ezsheets, 2)
# </editor-fold>

# <editor-fold desc="pygsheets">
start_pygsheets = time.time()
client = pygsheets.authorize()
gs_pygsheets = client.open(gs_name)
sheet = gs_pygsheets['Аркуш1']
print('pygsheets')
print(sheet['A1'].value)
pygsheets_time = round(time.time() - start_pygsheets, 2)
# </editor-fold>



