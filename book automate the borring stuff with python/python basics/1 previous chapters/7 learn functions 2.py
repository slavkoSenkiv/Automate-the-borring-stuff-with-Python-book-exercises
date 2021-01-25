"""
The global Statement

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

def spam():
    global eggs
    eggs = 'spam'

def bacon():
    global eggs
    eggs = 'bacon'

def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)
bacon()
ham()

def spam():
    print(eggs)
    global eggs
    eggs = 'spam local'

eggs = 'global'
spam()

Exception Handling
def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('error: invalid argument - u used 0')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


def spam(divideBy):
    return 42 / divideBy
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))

except ZeroDivisionError:
    print('error: invalid argument - u used 0')

A Short Program: Zigzag

"""















