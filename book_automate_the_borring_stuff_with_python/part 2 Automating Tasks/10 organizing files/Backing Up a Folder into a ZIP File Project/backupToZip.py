#!/usr/bin/env python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
    # Back up the entire contents of 'folder' into a ZIP file

    folder = os.path.abspath(folder)  # make sure folder is absolute
    print(folder)

    # Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if os.path.exists(zipFileName):
            break
        number += 1


    # Create the New ZIP File
    print(f'Creating {zipFileName}...')
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for folderName, subFolders, fileNames in os.walk(folder):
        print(f'Adding files in {folderName}...')
        # Add the current folder to the ZIP file
        backupZip.write(folderName)

        # Add all the files in this folder to the ZIP file
        for fileName in fileNames:
            # newBase = os.path.basename(folder) + '_'
            if fileName.startswith(os.path.basename(folder) + '_') and fileName.endswith('.zip'):
                continue  # don't back up the backup Zip files
            backupZip.write(os.path.join(folderName, fileName))
        backupZip.close()
        print('Done.')

backupToZip('C:\\fl1')

