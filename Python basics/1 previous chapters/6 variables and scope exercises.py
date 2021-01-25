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


