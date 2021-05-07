import openpyxl, pprint

print('loading workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
censusData = {}

print('reading rows...')
for row in range(2, sheet.max_row + 1):
    state  = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop    = sheet['D' + str(row)].value

    censusData.setdefault(state, {})

    censusData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    censusData[state][county]['tracts'] += 1
    censusData[state][county]['pop'] += pop

print('writing files...')
census2010 = open('census2010.py', 'w')
census2010.write('allData = ' + pprint.pformat(censusData))
census2010.close()