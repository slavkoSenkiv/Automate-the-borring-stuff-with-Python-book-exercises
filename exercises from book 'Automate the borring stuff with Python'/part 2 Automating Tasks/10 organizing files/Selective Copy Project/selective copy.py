import os, shutil

def selectiveCopy(startFolder, endFolder):

    for folderName, subFolders, fileNames in os.walk(startFolder):
        print(f'Copying files from {folderName}')
        for fileName in fileNames:
            if fileName.endswith('.txt'):
                print(f'Copying {fileName} from {folderName} to {endFolder}..')
                shutil.copy(os.path.join(folderName, fileName), endFolder)

a = 'C:\\Users\\Yaroslav\\a'
b = 'C:\\Users\\Yaroslav\\b'
selectiveCopy(a, b)
