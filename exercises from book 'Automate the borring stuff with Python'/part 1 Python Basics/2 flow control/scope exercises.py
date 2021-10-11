"""
print('hello')
print('world')

print('hello', end=' 234')
print('world')

print('cats', 'dogs', 'mice' )
print('cats', 'dogs', 'mice', sep=', ')

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()

Local Scopes Cannot Use Variables in Other Local Scopes
def spam():
    eggs = 31337
spam()
print(eggs)

Local Scopes Cannot Use Variables in Other Local Scopes

def spam():
     eggs = 99
     bacon()
     print(eggs)
def bacon():
     ham = 101
     eggs = 0
spam()

working exmpl
def spam():
    print(bacon())

def bacon():
    return 22

spam()

Global Variables Can Be Read from a Local Scope

def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)

Local and Global Variables with the Same Name

def spam():
    eggs = 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)
"""




"""
lines = 0
space = ' '
while lines <= 10:
    print(space * lines +'****' + ' № of lines = ' + str(lines))
    lines = lines + 1

while lines <= 20:
    print(space * lines + '****'+ ' № of lines = '+ str(lines))
    lines = lines - 1
    if lines <= -1:
        break

long zigzag my version
y = 100
def x():
    lines = 10
    space = ' '
    while lines >= 0:
        print(space * lines + '****' + ' № of lines = ' + str(lines) + ' y right now is ' + str(y))
        lines = lines - 1
        if lines <= 0:
            break

    while lines <= 10:
        print(space * lines + '****' + ' № of lines = ' + str(lines) + ' y right now is ' + str(y))
        lines = lines + 1
        if lines >= 11:
            break

while y >= 0:
    x()
    y = y - 1
    


"""
import time, sys
indent = 0 # How many spaces to indent
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: #the main program loop
        print(' ' * indent, end='')
        print('****')
        time.sleep(0.1) #pause for 1/10 of a second

        if indentIncreasing:
            # increase the number of spaces
            indent = indent + 1
            if indent == 20:
                #change direction
                indentIncreasing = False

        else:
            #decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()


"""


