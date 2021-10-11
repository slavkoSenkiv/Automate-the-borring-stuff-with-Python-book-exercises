import openpyxl
from openpyxl.styles import Font

num = int(input('enter number...'))
wb = openpyxl.Workbook()
sheet = wb.active

for y in range(num + 1):
    for x in range(num + 1):

        # Check if in header row or column.
        isHeader = False

        if x == 0 and y == 0:
            isHeader = True
            n = ''

        elif x == 0:
            isHeader = True
            n = y

        elif y == 0:
            isHeader = True
            n = x

        else:
            n = x * y

        c = sheet.cell(row=y + 1, column=x + 1)

        if isHeader:
            c.font = Font(bold=True)

        c.value = n

f = 'multiplication_table_' + str(num) + '.xlsx'

wb.save(f)

print('Saved as ' + f)
