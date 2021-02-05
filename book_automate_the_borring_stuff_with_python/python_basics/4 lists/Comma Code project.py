"""
Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it. Be sure to test
the case where an empty list [] is passed to your function. and integers
"""

spam = ['a', 'b', 'c', 'd', 1, 2, 3]
oneItemSpam = ['one']
emptySpam = []

def grammar(argument):
    if len(argument) >= 2:
        for i in range(len(argument) - 1):
            print(str(argument[i]) + ', ', end='')
        print('and ' + str(argument[-1]))
    if len(argument) == 1:
        print(str(argument[0]) + '.')
    if len(argument) == 0:
        print('the list is empty')


grammar(spam)
grammar(oneItemSpam)
grammar(emptySpam)