import shelve, pyperclip, sys

shelveFile = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        shelveFile[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del shelveFile[sys.argv[2]]

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(shelveFile.keys())))
    elif sys.argv[1].lower() == 'deleteall':
        shelveFile.clear()
    elif sys.argv[1] in shelveFile:
        pyperclip.copy(shelveFile[sys.argv[1]])

shelveFile.close()


