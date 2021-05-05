import openpyxl

fileName = 'myProduce'
insertFrom = 3
howManyInsert = 4

wb = openpyxl.load_workbook(f'{fileName}.xlsx')
sheet = wb.active

sheet.insert_rows(insertFrom + 1, howManyInsert)

wb.save(f'new_{fileName}.xlsx')
