from pathlib import Path
import re

# TODO: + asks what file u what to modify and opens that file
# TODO: + print actual content of the file
# TODO: + with regex finds if there are key-words
# TODO: if script find any keys in file it promt u to input your value for every keyword it found
# TODO: sript replace keys with your imputed value
# TODO: after all found keys are replaced it says it

fileName = input('what file to modify: ')
p = Path.cwd()/(fileName + '.txt')
file = open(p)
fileContent = file.read()
print(fileContent)

adjectiveRegex = re.compile(r'ADJECTIVE')
matchAdjective = adjectiveRegex.search(fileContent)
print(f'we found: {matchAdjective.group()}')
if matchAdjective:
    print('do smth')

nounRegex = re.compile(r'NOUN')
matchNoun = nounRegex.search(fileContent)
print(f'we found: {matchNoun.group()}')

verbRegex = re.compile(r'VERB')
matchVerb = verbRegex.search(fileContent)
print(f'we found: {matchVerb.group()}')

