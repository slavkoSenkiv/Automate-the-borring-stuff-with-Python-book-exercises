"""
Input Validation
Add try and except statements to the previous project to detect whether the
user types in a noninteger string. Normally, the int() function will raise a
ValueError error if it is passed a noninteger string, as in int('puppy'). In the
except clause, print a message to the user saying they must enter an integer
"""

def collatz(number):

        if number % 2 == 0:
            print('this is even')
        if number % 2 == 1:
            print('this is odd')

while True:
    print('enter a number')
    try:
        x = input()
        collatz(int(x))
    except ValueError:
        print('please enter a only numbers here')
