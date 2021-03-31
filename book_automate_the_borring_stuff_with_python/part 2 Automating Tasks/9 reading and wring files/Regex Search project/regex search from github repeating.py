import re, os


def search_function(regex, content):
    regex = re.compile(regex, re.I)
    found_matches = regex.findall(content)
    print(found_matches)

while True:
    directory = input('inter an absolute path to the directory: \n')
    if os.path.exists(directory) == True:
        print('directory exists')
        break

user_regex = input('enter your regex:\n')

folders_files = os.listdir(directory)

for file in folders_files:
    if file.endswith('.txt'):
        print(os.path.join(file))
        file_content = open(os.path.join(directory, file), 'r+')
        inside_text = file_content.read()
        search_function(user_regex, inside_text)

