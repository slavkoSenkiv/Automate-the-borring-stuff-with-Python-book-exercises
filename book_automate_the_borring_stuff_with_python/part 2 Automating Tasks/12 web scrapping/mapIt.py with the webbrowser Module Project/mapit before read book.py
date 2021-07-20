#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

"""import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # get address from cmd
    address = sys.argv[1:]
    urlSuffix = ''
    for words in address:
        if words == address[-1]:
            urlSuffix += words
        else:
            urlSuffix += words + '+'
    webbrowser.open('https://www.google.com/maps/place/' + urlSuffix)"""

address = input('enter address...')
address = address.replace(' ', '+')
print(address)
