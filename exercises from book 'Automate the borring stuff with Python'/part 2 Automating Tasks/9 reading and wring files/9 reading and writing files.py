# Files and File Paths





"""
# Backslash on Windows and Forward Slash on macOS and Linux
from pathlib import Path
x = Path('bacon', 'bacon', 'eggs')
print(str(x))

from pathlib import Path

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\ Users\Al', filename))
    
# Using the / Operator to Join Paths

# print(Path('код', 'atbs', 'part2', '9 reading files'))

homeFolder = Path('C:/Users/Al')
subFolder = Path('spam')

print(Path(homeFolder/subFolder))

# The Current Working Directory
from pathlib import Path
import os
print(Path.cwd())
os.chdir('C:\\Windows\\System32')
print(Path.cwd())

# The Home Directory
from pathlib import Path

print(Path.home())

# Absolute vs. Relative Paths
#Creating New Folders Using the os.makedirs() Function

from pathlib import Path
import os
os.makedirs('C:\\delicious\\walnut\\waffles')
Path(r'C:\spam').mkdir()

# Handling Absolute and Relative Paths
from pathlib import Path
import os
import sys
print(1)
print(Path.cwd())
print(Path.cwd().is_absolute())
print(Path('spam/bacon/eggs').is_absolute())

print(2)
x = Path('my/relative/path')
y = Path.cwd()/x
print(y)
print(y.is_absolute())

print(3)
print(os.path.abspath('.'))
print(os.path.abspath('.\\Scripts'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(4)
print(os.path.relpath('C:\\Windows', 'C:\\'))
print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))

# Getting the Parts of a File Path
from pathlib import Path

p = Path('C:/Users/Al/spam.txt')
print(f'p = {p}')
print(f'anchor = {p.anchor}')
print(f'parent = {p.parent}')
print(f'name = {p.name}')
print(f'stem = {p.stem}')
print(f'suffix = {p.suffix}')
print(f'drive = {p.drive}')

print(2)

print(Path.cwd())
print(0, Path.cwd().parents[0])
print(1, Path.cwd().parents[1])
print(2, Path.cwd().parents[2])
print(3, Path.cwd().parents[3])
print(4, Path.cwd().parents[4])
print(5, Path.cwd().parents[5])
print(6, Path.cwd().parents[6])

# Finding File Sizes and Folder Contents
import os
from pathlib import Path
print('os.path.getsize(path)')
print('Size of Path.cwd() = ', os.path.getsize(Path.cwd()))
print('Size of C:\\ = ', os.path.getsize('C:\\'))
print('Size of C:\\Users\\Yaroslav\\Videos = ', os.path.getsize('C:\\Users\\Yaroslav\\Videos'))
print('Size of C:\\Users\\Yaroslav\\Videos\\Пользовательские исследования.mkv = ', os.path.getsize('C:\\Users\\Yaroslav\\Videos\\Пользовательские исследования.mkv'))

print(' os.listdir(path)')
print(os.listdir('C:\\для харду\\програмування\\код\\Here-im-learning-python\\book_automate_the_borring_stuff_with_python\\part 2 Automating Tasks\\8 input validation'))

print('totalSize')
totalSize = 0

for filename in os.listdir('C:\\для харду\\програмування\\код\\Here-im-learning-python\\book_automate_the_borring_stuff_with_python\\part 2 Automating Tasks\\8 input validation'):
    totalSize += os.path.getsize(os.path.join('C:\\для харду\\програмування\\код\\Here-im-learning-python\\book_automate_the_borring_stuff_with_python\\part 2 Automating Tasks\\8 input validation', filename))
print(f'totalSize = {totalSize}')

# Modifying a List of Files Using Glob Patterns
from pathlib import Path
p = Path('C:/Users/Yaroslav/Desktop')
print(p.glob('*'))
print(list(p.glob('*'))) # Make a List from the generator

# Checking Path Validity
from pathlib import Path

p = Path.cwd()
print(p)
x = p / '123.txt'
print(x)

print('exists ', p.exists())
print('p isFile', p.is_file())
print('x isFile', x.is_file())
print('p isDir', p.is_dir())
print('x isDir', x.is_dir())

# The File Reading/Writing Process
from pathlib import Path
p = Path('spam.txt')
p.write_text('Hello, world!')
print(p.read_text())

# Opening Files with the open() Function
# Reading the Contents of Files

from pathlib import Path
p = Path.home()/'Documents'/'testDoc.txt'
print(p.exists())
testDoc = open(p)
testDocContent = testDoc.read()
print('testDocContent', testDocContent)
testDocContentListed = testDoc.readlines()
print('testDocContentListed', testDocContentListed)

print(1.1)
p1 = Path.home()/'Documents'/'testDoc.txt'
testDoc = open(p1)
testDocContentListed = testDoc.readlines()
print('testDocContentListed', testDocContentListed)

print(2)
x = Path.home()/'Documents'/'sonnet.txt'
print(p.exists())
sonnetDoc = open(x)
sonnetDocContentListed = sonnetDoc.readlines()
print('sonnetDocContentListed', sonnetDocContentListed)

# Writing to Files
from pathlib import Path
import os
print(Path.cwd())
p = Path('testDoc.txt')
file = open('testDoc.txt')
fileContent = file.read()
print(fileContent)

# Writing to Files
from pathlib import Path
import os
print(Path.cwd())
p = Path('testDoc.txt')
file = open('testDoc.txt', 'w')
file.write('hello world!\n')
file.close()
file = open('testDoc.txt', 'a')
file.write('bacon is not a vegetable')
file.close()
file = open('testDoc.txt')
print(file.read())
file.close()

# Saving Variables with the shelve Module
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()



"""
# Saving Variables with the pprint.pformat() Function
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()




