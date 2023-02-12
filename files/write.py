def __writeFile__(file):
    file.write("Veamos que tal funciona esto de la escritura en python")

def __readFile__(file):
    print(file.read())

with open("test.txt", "w") as file:
    __writeFile__(file)

with open("test.txt", "r") as file:
    __readFile__(file)

# a for writing (truncating the file if it already exists)
# a+ for reading and writing (appending to the end of the file if it exists)