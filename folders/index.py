import os

## this show the current directory
print(os.getcwd())

# create a new directory

def __createFolder__():
    if not os.path.exists("newFolder"):
        os.makedirs("newFolder")

__createFolder__()

# change the current directory
def __changeDirectory__():
    os.chdir("newFolder")

# remove a directory
def __removeDirectory__():
    if os.path.exists("newFolder"):
        os.rmdir("newFolder")

# show the content of a directory
def __showDirectory__(folderpath):
    print(os.listdir(folderpath))

# show if is a file or a directory
def __isFileOrDirectory__(folderpath):
    print(os.path.isdir(folderpath))
    print(os.path.isfile(folderpath))

__isFileOrDirectory__("newFolder")