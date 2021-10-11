import re

file = open('testFile.txt')
file_content = file.read()
file.close()

regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')

print(file_content, '\n')
for found_match in regex.findall(file_content):
    for item in found_match:
        if item != '':
            reg = re.compile(r'{}'.format(item))
            new_value = input(f'enter value for {item}')
            file_content = reg.sub(new_value, file_content, 1)

file = open('testFile.txt', 'w')
file.write(file_content)
file.close()