import os

def findAndPrintBigFiles(folder):
    for folderNames, subFolders, fileNames in os.walk(folder):
        for fileName in fileNames:
            if os.path.getsize(os.path.join(folderNames, fileName)) > 100000000:
                print(fileName, os.path.getsize(os.path.join(folderNames, fileName)))

path = 'C:\\для харду'
findAndPrintBigFiles(path)