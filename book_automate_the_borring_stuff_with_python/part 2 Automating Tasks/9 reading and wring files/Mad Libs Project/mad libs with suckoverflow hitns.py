from pathlib import Path
import re


fileName = input('what file to modify: ')
p = Path.cwd()/(fileName + '.txt')
with open(p, 'r') as file:
    fileContent = file.read()
print(fileContent)

adjective = input('AJECTIVE = ')
noun = input('NOUN = ')
verb = input('VERB = ')

fileContent = fileContent.replace('ADJECTIVE', adjective)
fileContent = fileContent.replace('NOUN', noun)
fileContent = fileContent.replace('VERB', verb)

with open(p, 'w') as file:
    file.write(fileContent)
print(fileContent)



