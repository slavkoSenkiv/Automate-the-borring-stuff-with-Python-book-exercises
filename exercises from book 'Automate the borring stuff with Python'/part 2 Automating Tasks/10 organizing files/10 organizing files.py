# the shutil Module
"""
# copying files and folders
import shutil, os
from pathlib import Path


p = Path.cwd()
shutil.copy(p/'spam.txt', p/'some folder')
shutil.copy(p/'eggs.txt', p/'some folder/eggs2.txt')

import os, shutil
from pathlib import Path

p = Path.home()
shutil.copytree(p/'spam', p/'spam backup')

import shutil
from pathlib import Path

p = Path.cwd()
shutil.copytree(p/'spam', p/'spam backup')

# Moving and Renaming Files and Folders

import shutil
from pathlib import Path
p = Path.cwd()/'spam'
shutil.move(p / '1 level doc.txt', p / '1 level folder')

import shutil
from pathlib import Path
p = Path.cwd()/'spam'
shutil.move(p / '1 level doc.txt', p / '1 level folder'/'new doc.txt')

# Permanently Deleting Files and Folders
import os
from pathlib import Path

p = Path.cwd()/'spam backup'/'1 level doc.txt'
os.unlink(p)

# Safe Deletes with the send2trash Module
import send2trash
bacon_file = open('bacon.txt', 'a') # creates the file
bacon_file.write('Bacon is not a vegetable')
bacon_file.close()
send2trash.send2trash('bacon.txt')

# Walking a Directory Tree
import os
from pathlib import Path
p = Path.cwd()/'spam'

for folderName, subFolders, fileNames in os.walk(p):
    print('the current folder name is: ' + folderName)

    for subfolder in subFolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in fileNames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print('')

# Compressing Files with the zipfile Module
import zipfile, os
from pathlib import Path

p = Path.home()
example_zip = zipfile.ZipFile(p / 'abc.zip')
print(example_zip.namelist())
spam_info = example_zip.getinfo('1 level doc.txt')
print(spam_info.file_size)
print(spam_info.compress_size)
print(f'compressed file is {round(spam_info.file_size / spam_info.compress_size, 2)}X smaller')


# Extracting from ZIP Files
import zipfile, os
from pathlib import Path
p = Path.home()
abcZip = zipfile.ZipFile(p / 'abc.zip')
abcZip.extractall(Path.home())
abcZip.close()

import zipfile
from pathlib import Path

p = Path.home()
abcZip = zipfile.ZipFile(p / 'abc.zip')
abcZip.extract('1 level doc.txt')
abcZip.close()

# Creating and Adding to ZIP Files

import zipfile
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('newSpam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
"""






