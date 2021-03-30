import re, glob, os
from pathlib import Path

regex = re.compile(r'\d\d\d')

for filename in glob.glob('*.txt'):
    with open(os.path.join(Path.cwd(), filename), 'r') as file:
        file_content = file.read()
        found_matches = regex.findall(file_content)
        print(f'in {filename} we found {found_matches}\n')

