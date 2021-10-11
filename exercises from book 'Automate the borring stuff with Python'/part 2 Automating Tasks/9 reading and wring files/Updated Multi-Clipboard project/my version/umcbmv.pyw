import pyperclip, sys, shelve

umcbmvShelf = shelve.open('umcbmv')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    umcbmvShelf[sys.argv[2]] = pyperclip.paste()
if len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(umcbmvShelf.keys())))
    elif sys.argv[1] in umcbmvShelf:
        pyperclip.copy = str(umcbmvShelf[sys.argv[1]])

umcbmvShelf.close()


