"""import pyinputplus as pyip

while True:
    prompt = 'Whant to keep idiot busy for hours?\n'
    response  = pyip.inputYesNo(prompt)
    if response == 'no':
        break
print('thx, have a nice day')"""

import pyinputplus as pyip

while True:
    response = pyip.inputYesNo('хочеш зайняти ідіота на години?', yesVal='так', noVal='ні')
    if response == 'ні':
        break
print('thx')