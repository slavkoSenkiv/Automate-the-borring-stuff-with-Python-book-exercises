import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
sheet = ss[0]

first_column = sheet.getColumn(1)
second_column = sheet.getColumn(2)
third_column = sheet.getColumn(3)


# v1
for row in range(2, 15001):
    if int(ss[0].getRow(row)[0]) * int(ss[0].getRow(row)[1]) == int(ss[0].getRow(row)[2]):
        pass
    else:
        print(row)

print('end 1')

# v2
for row in range(2, 15001):
    if int(first_column[row]) * int(second_column[row]) == int(third_column[row]):
        pass
    else:
        print(row + 1)
print('end 2')

