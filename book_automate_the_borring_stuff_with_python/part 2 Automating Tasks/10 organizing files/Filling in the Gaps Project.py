import os, shutil, re

def findGap(folder):
    for folderNames, subFolders, fileNames in os.walk(folder):
        number = 1
        for fileName in fileNames:
            name = os.path.basename(fileName)
            if name.startswith('text_'):
                lastCharacter = name[-5]
                if int(lastCharacter) == number:
                    print(name, ' is ok')
                    number += 1
                else:
                    print(f'{name} was renamed to {name[:7] + str(number) + name[-4:]}')
                    shutil.move(os.path.join(folder, name), os.path.join(folder, f'{name[:7] + str(number) + name[-4:]}'))
                    number += 1

path = 'C:\\для харду\\програмування\\код\\Here-im-learning-python\\book_automate_the_borring_stuff_with_python\\part 2 Automating Tasks\\10 organizing files\\a'
findGap(path)