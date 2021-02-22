import re
def dateDetection(inputDate):
    date = re.compile(r'((\d{2})/(\d{2})/(\d{4}))')
    inputDate = date.search(inputDate)
    # print('Before Verification date: '+[inputdate.group](https://inputdate.group)())

    month = inputDate.group(2)
    day   = inputDate.group(3)
    year  = inputDate.group(4)

    month_range_30 = ['04','06','09','11']
    month_range_31 = ['01','03','05','07','08','10','12']

    if month in month_range_31:
        if int(day) > 31:
            print('incorrect Date....')
            return False
    elif month in month_range_30:
        if int(day) > 30:
            print('incorrect Date....')
            return False
    elif month == '02':
        if int(year) % 4 == 0:
            if int(day) > 29:
                print('wrong days for February.....')
                return False
        elif int(year) % 100 == 0 and int(year) % 400 == 0:
            if int(day) > 29:
                print('wrong days for February.....')
                return False
        else:
            if int(day) > 28:
                print('wrong days for February.....')
                return False
    else:
        print('incorrect Month .....')
        return False
    print('After Verification Date: ' + inputDate.group())

dateDetection('today is like 02/32/2020') # returns False
dateDetection('today is like 02/28/2020') # returns True
dateDetection('today is like 13/28/2020') # returns False