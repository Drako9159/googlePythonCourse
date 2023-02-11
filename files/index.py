file = open("test.txt")
print(file.readline())
print(file.read())
file.close()

#creta block of code
with open("test.txt") as file:
    print(file.read())


def __readLines__(file):
    lines = file.readlines()
    lines.sort()
    print(lines)

__readLines__(open("test.txt"))