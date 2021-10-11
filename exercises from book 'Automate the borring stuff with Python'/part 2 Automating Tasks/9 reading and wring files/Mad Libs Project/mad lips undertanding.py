import re
file = open('testFile.txt')
text = file.read()
file.close()
regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')

print(text, '\n')
for found_match in regex.findall(text):
    for item in found_match:
        if item != '':
            reg = re.compile(r'{}'.format(item))
            input_text = input(f'enter value for {item}')
            text = reg.sub(input_text, text, 1)

