#! python3
# umcb.pyw - saves and loads pieces of text to the clipboard
# Usage: py.exe umcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe umcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe umcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

umcbShelf = shelve.open('umcb')

# TODO: Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    umcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:


# TODO: List keywords and load content.

    umcbShelf.close() Make your code look like the following:

