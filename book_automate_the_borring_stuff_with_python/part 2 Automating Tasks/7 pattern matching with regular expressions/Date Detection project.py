import re

def dataDetection(text):
    dateRegex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
    matchObject = dateRegex.search(text)

    day = matchObject.group(1)
    month = matchObject.group(2)
    year = matchObject.group(3)

    month_with_30 = ['04','06','09','11']
    month_with_31 = ['01','03','05','07','08','10','12']

    if month in month_with_30:
        if int(day) > 30:
            print('incorrect date, this month cant has more then 30')
            return False
    elif month in month_with_31:
        if int(day) > 31:
            print('incorrect date, this month cant has more then 31')
            return False
    elif month == '02':
        if int(year) % 4 == 0:
            if int(day) > 29:
                print('incorrect date for february')
                return False
        else:
            if int(day) > 28:
                print('incorrect date for february')
                return False
    else:
        print('incorrect month')
        return False
    print('the date was found ' + matchObject.group())


dataDetection('here it is  06/01/1995') # correct simple date
dataDetection('here it is  40/01/1995') # incorrect simple date
dataDetection('here it is  29/02/2000') # correct leap year
dataDetection('here it is  29/13/2000') # incorrect month

