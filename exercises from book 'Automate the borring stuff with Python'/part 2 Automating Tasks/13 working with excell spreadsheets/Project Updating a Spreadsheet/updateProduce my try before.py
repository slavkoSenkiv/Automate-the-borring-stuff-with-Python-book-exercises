import openpyxl
wb = openpyxl.load_workbook('freezeExample.xlsx')
sheet = wb['Sheet']
celeryCases = 0
garlicCases = 0
lemonCases = 0

for row in range(2, sheet.max_row + 1):
    if sheet['A' + str(row)].value == 'Celery':
        sheet['B' + str(row)].value = 1.11
        celeryCases += 1
    if sheet['A' + str(row)].value == 'Garlic':
        sheet['B' + str(row)].value = 2.22
        garlicCases += 1
    if sheet['A' + str(row)].value == 'Lemon':
        sheet['B' + str(row)].value = 3.33
        lemonCases += 1

print(f'we found:\n'
      f' {celeryCases} celery items\n'
      f' {garlicCases} garlic items\n'
      f' {lemonCases} lemon items\n')

wb.save('edited_freezeExample_myverbeforebook.xlsx')
