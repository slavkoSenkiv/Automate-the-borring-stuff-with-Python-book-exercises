#! python 3.5
# regex search.py - opens all .txt files in a folder and searches for any line
# that matches a user-supplied regular expression

import os, re

def search_function(regex, content):                # this function print all found matches in the content
    search_regex = re.compile(regex, re.I)
    found_matches = search_regex.findall(content)
    print(found_matches)

while True:
    directory = input('Enter the absolute path to the folder, which files  you want to search for: \n')
    if os.path.exists(directory) == True:
        print('This folder exists')
        break

users_regex = input('Enter the regular expression: \n')

folders_files = os.listdir(directory)

for file in folders_files:
    if file.endswith('.txt'):
        print(os.path.join(directory, file))
        txtfile = open(os.path.join(directory, file), 'r+')
        file_content = txtfile.read()
        search_function(users_regex, file_content)