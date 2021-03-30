import os, re

def search (regex, text):
    search_regex = re.compile(regex, re.I)
    result = search_regex.findall(txt)
    print(result)

while True:
    dirs = input('enter folder u need to research: ')
    if os.path.exists(dirs) == True:
        print('this folder exists')
        break

    user_search = input('enter your regex: ')

    folder 