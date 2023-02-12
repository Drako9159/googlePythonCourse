import os

def create_python_script(filename):
  comments = "# Start osdflkñlsdfjlñgjsdfñlgjñlakjdfñgljsdfgf a new Python program"
  with open(filename, "w") as file:
    file.write(comments)
    file.close()
    filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))