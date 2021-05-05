import openpyxl

workBookName = 'myProduce'
insertAfter = 4
howManyInsert = 2

inputWb = openpyxl.load_workbook(f'{workBookName}.xlsx')
inputSheet = inputWb.active

outputWb = openpyxl.Workbook()
outputSheet = outputWb.active



outputWb.save(f'new_{workBookName}_afterGitHub.xlsx')