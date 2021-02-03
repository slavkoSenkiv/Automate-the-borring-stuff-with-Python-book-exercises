# Working with Strings
"""
# String Literals
print('hello there')
print("hello ' there")
print('hello " there ')

print('hello \' there')
print('hello\nthere')
print('hello \\ there')
print('hello \t there')
print()
print('Hello there!\nHow are you\nI\'m doing fine\n \t Cool then')

#Raw Strings
print(r'i\'m fine \t And how are you?')

# Multiline Strings with Triple Quotes
print('''

ou

hello there
it was nice to meet you
bye

and here is ' character
''')

# Multiline Comments

'''
many
lines
coment global scope
'''

# Indexing and Slicing Strings
x = 'hello!'
print(x[0])
print(x[-1])
print(x[0:-1])

# The in and not in Operators with Strings
x = 'hello worls'
if 'hello' in x:
    print('+')
if 'dud' not in x:
    print('+')

"""
# Putting Strings Inside Other Strings
"""
print('hello there! my name is %s and i have %s fingers and %s legs' % ('OCTOPUS', 40, 8))

name1 = 'OCTOPUS'
fingers1 = 40
legs1 = 8

print(str(1) + ' hello there! my name is %s and i have %s fingers and %s legs' % (name1, fingers1, legs1))

print(str(2) + f' hello there! my name is {name1} and i have {fingers1} fingers and {legs1} legs')

print(str(3) + ' hello there! my name is {name1} and i have {fingers1} fingers and {legs1} legs')
"""

# Useful String Methods
"""

#The upper(), lower(), isupper(), and islower() Methods
lover = 'lover case here'
upper = 'UPPER CASE HERE'
fewUpper = 'One upper here'

print(lover.upper())
print(upper.lower())
print(fewUpper.lower() + '\n' + fewUpper.upper())

print('how are you')
feeling = input()
if feeling.lower() == 'great':
    print('+')
else:
    print('-')
    
x = 'hello'
y = 'HELLO'
z = 'Hello'

if x.lower():
    print('+')
if y.isupper():
    print('+')
if z.isupper():
    print('+')
else:
    print('no')
    
    # The isX() Methods
# input validation
while True:
    print('enter your age')
    age = input()
    if age.isnumeric():
        break
    print('enter numbers pls')

while True:
    print('enter your name')
    name = input()
    if name.isalpha() and name.istitle():
        print('thx')
        break
    print('enter only letter and start with a capital')
    
    
# The join() and split() Methods

x = ','

y = x.join(['a', 'b', 'c', 'd'])
print(y)


x = '1'

y = x.join('hello')
print(y)

# The join() and split() Methods

x = '1121314151617181910'
y = x.split('1')
print(y)

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment."
Please do not drink it.
Sincerely,
Bob'''

print(spam.split('\n'))

# Splitting Strings with the partition() Method


print('hello world'.partition('w'))
print('hewlwlo worwld'.partition('w'))

before, sep, after = 'hello, dear world'.partition('dear')
print(before)
print(sep)
print(after)

x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

# Justifying Text with the rjust(), ljust(), and center() Methods

x = 'hello'
y = 'hello'.rjust(30, '+')
z = 'hello'.ljust(30, '+')
print(x)
print(y)
print(z)

print('hello'.rjust(5, '+'))
print('hello'.rjust(6, '+'))
"""















