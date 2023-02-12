import os
import datetime

def __removeFile__(filePath):
    if os.path.exists(filePath):
        os.remove(filePath)
        print("File removed successfully")
    else:
        print("File does not exist")

__removeFile__("remove.txt")

def __createFile__(filePath):
    file = open(filePath, "w")
    file.write("This is a test file")
    file.close()
    print("File created successfully")

def __renameFile__(filePath, newFilePath):
    os.rename(filePath, newFilePath)
    print("File renamed successfully")



def __checkSize__(filePath):
    print(os.path.getsize(filePath))
__checkSize__("test2.txt")

def __checkLastModified__(filePath):
    timestamp = os.path.getmtime(filePath)
    print(datetime.datetime.fromtimestamp(timestamp))

__checkLastModified__("test2.txt")

def __checkDirectory__(filePath):
    print(os.path.abspath(filePath))
__checkDirectory__("test2.txt")