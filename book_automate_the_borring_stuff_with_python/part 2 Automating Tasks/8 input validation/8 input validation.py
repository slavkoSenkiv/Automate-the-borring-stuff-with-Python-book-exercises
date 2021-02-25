"""while True:
    age = input('enter age: ')
    try:
        age = int(age)
    except:
        print('enter digits')
        continue
    if age < 1:
        print('pls enter positive number')
        continue
    break"""

import pyinputplus
age = pyinputplus.inputEmail('enter mail...')
