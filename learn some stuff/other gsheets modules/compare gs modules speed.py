import time
import pygsheets
import ezsheets
import gspread
import openpyxl


# <editor-fold desc="functions">
def summ(list, row, column, start_time):
    for rows in list:
        for cells in rows:
            cells = cells * cells

    timer = round(time.time() - start_time, 2)
    result_sheet.cell(row=row, column=column).value = timer
# </editor-fold>


# <editor-fold desc="variables">
gs_name = 'test personal acc'
path_to_gspread_credentials_json = '/Users/ysenkiv/Code/Here-im-learning-python/learn some stuff/other gsheets modules/acces_files/credentials-sheets.json'
path_to_gspread_authorized_user = '/Users/ysenkiv/Code/Here-im-learning-python/learn some stuff/other gsheets modules/acces_files/authorized_user.json'
path_to_client_secret = '/Users/ysenkiv/Code/Here-im-learning-python/learn some stuff/other gsheets modules/acces_files/client_secret.json'
wb = openpyxl.Workbook()
result_sheet = wb.active
result_sheet['A1'].value = 'gspread'
result_sheet['B1'].value = 'ezsheets'
result_sheet['C1'].value = 'pygsheets'
result_sheet['D1'].value = 'gspread import time'
result_sheet['E1'].value = 'ezsheets import time'
result_sheet['F1'].value = 'pygsheets import time'
# </editor-fold>

for row in range(2, 4):
    """# <editor-fold desc="pygsheets">
    start_pygsheets = time.time()
    client = pygsheets.authorize(client_secret=path_to_client_secret)
    gs_pygsheets = client.open(gs_name)
    sheet = gs_pygsheets.worksheet('title', 'Sheet1')
    list_of_lists_pygsheets = sheet.range('A1:Z1000', returnas='matrix')
    summ(list_of_lists_pygsheets, row, 3, start_pygsheets)
    # </editor-fold>"""

    """# <editor-fold desc="ezsheets">
    start_ezsheets = time.time()
    gs_ezsheets = ezsheets.Spreadsheet(gs_name)
    sheet = gs_ezsheets['Sheet1']
    list_of_lists_ezsheets = sheet.getRows()
    summ(list_of_lists_ezsheets, row, 2, start_ezsheets)
    # </editor-fold>"""

    # <editor-fold desc="gspread">
    start_gspread = time.time()
    gc = gspread.oauth(credentials_filename=path_to_gspread_credentials_json, authorized_user_filename=path_to_gspread_authorized_user)
    gs = gc.open(gs_name)
    sheet1 = gs.get_worksheet(0)
    list_of_lists_gspread = sheet1.get_all_values()
    summ(list_of_lists_gspread, row, 1, start_gspread)
    # </editor-fold>

"""print(1)
for row in range(5, 7):
    # <editor-fold desc="gspread">
    start_gspread = time.time()
    gc = gspread.oauth(credentials_filename=path_to_gspread_credentials_json, authorized_user_filename=path_to_gspread_authorized_user)
    gs = gc.open(gs_name)
    sheet1 = gs.get_worksheet(0)
    list_of_lists_gspread = sheet1.get_all_values()
    summ(list_of_lists_gspread, row, 1, start_gspread)
    # </editor-fold>

    # <editor-fold desc="pygsheets">
    start_pygsheets = time.time()
    client = pygsheets.authorize(client_secret=path_to_client_secret)
    gs_pygsheets = client.open(gs_name)
    sheet = gs_pygsheets.worksheet('title', 'Sheet1')
    list_of_lists_pygsheets = sheet.range('A1:Z1000', returnas='matrix')
    summ(list_of_lists_pygsheets, row, 3, start_pygsheets)
    # </editor-fold>

    # <editor-fold desc="ezsheets">
    start_ezsheets = time.time()
    gs_ezsheets = ezsheets.Spreadsheet(gs_name)
    sheet = gs_ezsheets['Sheet1']
    list_of_lists_ezsheets = sheet.getRows()
    summ(list_of_lists_ezsheets, row, 2, start_ezsheets)
    # </editor-fold>

print(2)
for row in range(8, 10):
    # <editor-fold desc="ezsheets">
    start_ezsheets = time.time()
    gs_ezsheets = ezsheets.Spreadsheet(gs_name)
    sheet = gs_ezsheets['Sheet1']
    list_of_lists_ezsheets = sheet.getRows()
    summ(list_of_lists_ezsheets, row, 2, start_ezsheets)
    # </editor-fold>

    # <editor-fold desc="gspread">
    start_gspread = time.time()
    gc = gspread.oauth(credentials_filename=path_to_gspread_credentials_json,
                       authorized_user_filename=path_to_gspread_authorized_user)
    gs = gc.open(gs_name)
    sheet1 = gs.get_worksheet(0)
    list_of_lists_gspread = sheet1.get_all_values()
    summ(list_of_lists_gspread, row, 1, start_gspread)
    # </editor-fold>

    # <editor-fold desc="pygsheets">
    start_pygsheets = time.time()
    client = pygsheets.authorize(client_secret=path_to_client_secret)
    gs_pygsheets = client.open(gs_name)
    sheet = gs_pygsheets.worksheet('title', 'Sheet1')
    list_of_lists_pygsheets = sheet.range('A1:Z1000', returnas='matrix')
    summ(list_of_lists_pygsheets, row, 3, start_pygsheets)
    # </editor-fold>"""


wb.save('fastest gsheets module.xlsx')











