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
"""

# Handling Absolute and Relative Paths
from pathlib import Path
print(1)
print(Path.cwd())
print(Path.cwd().is_absolute())
print(Path('spam/bacon/eggs').is_absolute())

print(2)
x = Path('my/relative/path')
print(Path.cwd()/x)
















