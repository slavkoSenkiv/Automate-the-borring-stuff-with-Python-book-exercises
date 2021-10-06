import time
import pygsheets
import ezsheets
import gspread
import openpyxl

gs_name = 'test personal acc'
path_to_gspread_credentials_json = '/Users/ysenkiv/Code/access files/credentials.json'
path_to_gspread_authorized_user = '/Users/ysenkiv/Code/access files/authorized_user.json'


def mult1(list1, start_time):  # row, column,
    print(list1, '\n')
    row_index = 0
    for rows in list1:
        for cells in rows:
            new_value = int(cells) * 2
            row_index = list1.index(rows)
            cell_index = list1[row_index].index(cells)
            list1[row_index][cell_index] = new_value
        row_index += 1
    timer = round(time.time() - start_time, 2)
    print(timer)
    return list1


# <editor-fold desc="gspread">
"""start_gspread = time.time()
gc = gspread.oauth(credentials_filename=path_to_gspread_credentials_json, authorized_user_filename=path_to_gspread_authorized_user)
gs = gc.open(gs_name)
sheet1 = gs.worksheet('test2')
list_of_lists_gspread = sheet1.get_all_values()
sheet1.update('A1:Z1000', mult1(list_of_lists_gspread, start_gspread))
"""# </editor-fold>


gc = gspread.oauth(credentials_filename=path_to_gspread_credentials_json, authorized_user_filename=path_to_gspread_authorized_user)
gs = gc.open(gs_name)
sheet1 = gs.worksheet('test')
# sheet1.delete_rows(1, 2)

list1 = sheet1.col_values(1)
print(list1)