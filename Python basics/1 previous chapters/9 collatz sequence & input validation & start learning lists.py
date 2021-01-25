"""
#The Collatz Sequence

#template
def collatz(number):
    if number == 4:
        print('ok')

collatz(4)

#2d try
def collatz(number):
    if number % 2 == 0:
        print('even')
    if number % 2 == 1:
        print('odd')
while True:
    print('enter a number')
    inputNumber = int(input())
    collatz(inputNumber)

#The Collatz Sequence & Input Validation

try:
    def collatz(number):
        if number % 2 == 0:
            print(str(number // 2))
        if number % 2 == 1:
            print(str(3 * number + 1))
    while True:
        print('enter a number')
        inputNumber = int(input())
        collatz(inputNumber)

except ValueError:
    print('enter only numbers')

#lists & indexes

spam = ['hello', 123, 1]
print(spam[0])

spam = [[1, 2, 3, 4], ['a', 'b', 'c', 'd']]
print('2 = ' + spam[0][1])
print('c = ' + spam[1][2])

"""



