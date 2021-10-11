import os, zipfile

def backupToZip(folder):
    # make sure path is absolute
    folder = os.path.abspath(folder)

    """# defining name for new zip
    number = 1
    while True:
        newZipName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(newZipName):
            break
        number += 1

    # creating zip file
    print(f'Creating {newZipName}')
    newZipFile = zipfile.ZipFile(newZipName, 'w')

    for folderName, subfolders, filenames in os.walk(folder):
        print(f'Adding Files in {folderName}')
        newZipFile.write(folderName)


        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue
            newZipFile.write(os.path.join(folderName, filename))
            # newZipFile.write(filename)
    newZipFile.close()
    print('Done.')"""

    print('items')
    for items in os.walk(folder):
        print(items)

    for folderName, subFolders, fileNames in os.walk(folder):
        print(f'\nfolder name: {folderName}')
        for fileName in fileNames:
            print(f'file name: {fileName}')

        x = os.path.join(folderName, fileName)
        print('join is: ', x)

backupToZip('C:\\fl1')

