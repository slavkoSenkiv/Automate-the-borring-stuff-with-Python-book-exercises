
"""
# Raising Exceptions
raise Exception('there is error here')

# Getting the Traceback as a String
def spam():
    bacon()
def bacon():
    raise Exception('Error message')
spam()


import traceback
try:
    raise Exception('my error')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('Traceback info was written to errorInfo.txt')

111
# Assertions
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.reverse()
print(ages)
assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
switchLights(market_2nd)
"""

# Logging Using the logging Module
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -%(levelname)s + %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' %(n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total
print(factorial(5))
logging.debug('End of program')
