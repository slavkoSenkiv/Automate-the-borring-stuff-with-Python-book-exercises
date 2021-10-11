import shelve, sys, pyperclip

shelveFile = shelve.open('mcb')
while True:
    key = input('enter key: ')

    if key.lower() == 'save':
        code = input('enter code: ')
        value = input('enter value: ')
        shelveFile[code] = value

    elif key.lower() == 'list':
        print(str(list(shelveFile.keys())))

    elif key.lower() == 'delete':
        code = input('enter code: ')
        del shelveFile[code]

    elif key.lower() == 'deleteall':
        shelveFile.clear()

    elif key.lower() == 'print':
        code = input('enter code: ')
        print(shelveFile[code])


shelveFile.close()


