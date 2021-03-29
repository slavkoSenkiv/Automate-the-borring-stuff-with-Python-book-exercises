import re

file = open('testFile.txt')
text = file.read()
file.close()

regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')

for found_element in regex.findall(text):
    print(f'found_element = {found_element}')
    for item in found_element:
        if item != '':
            print(f'item = {item}')
            reg = re.compile(r'{}'.format(item))
            print(f'reg = {reg}')
