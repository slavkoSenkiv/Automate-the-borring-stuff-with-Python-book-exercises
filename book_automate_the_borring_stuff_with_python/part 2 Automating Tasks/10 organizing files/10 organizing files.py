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
"""

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