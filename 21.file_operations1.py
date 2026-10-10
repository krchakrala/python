#get file path, directory and extension using os.path module
import os
path = "C:/Projects/Python/report.pdf"
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.splitext(path))

#shutil package provides a higher level interface for file operations
import shutil
shutil.copy(
    "docs/sample2.txt",
    "docs/sample2.txt"
)


#move operation in shutil module can be used to move a file from one location to another
import shutil
shutil.move(
    "docs/sample.txt",
    "docs/new_directory/sample.txt"
)

#rmtree() function in shutil module can be used to delete a directory and all its contents
import shutil
shutil.rmtree("docs/Project")

#pathlib module provides an object-oriented approach to handle file system paths. It is available in Python 3.4 and later versions.
from pathlib import Path
import pathlib
import shutil
file_path = Path("docs/sample2.txt")
print(file_path)
file = Path("docs/sample2.txt")
print("file exists: ",file.exists())
print("is file: ",file.is_file())
folder = Path("docs/new_directory")
print("folder exists: ",folder.exists())
print("is directory: ",folder.is_dir())

folder = Path("docs/Data")
folder.mkdir(
    parents=True,
    exist_ok=True
)

file = Path("docs/Data/sample.txt")
file.write_text("Hello Python")
data = file.read_text()
print(data)
#file.unlink()  # delete the file
file.rename("docs/Data/sample.txt") 

##Creating a directory and writing a file in it
import os
folder = "docs/Employees"
if not os.path.exists(folder):
    os.mkdir(folder)

file_path = os.path.join(
    folder,
    "employee.txt"
)

with open(file_path, "w") as file:
    file.write("Name: Ravi\n")
    file.write("Technology: Python\n")
    file.write("Experience: 8 years\n")

with open(file_path, "r") as file:
    print(file.read())

#Listing all files in a directory using OS module
import os
folder = "docs"
for file in os.listdir(folder):

    if file.endswith(".txt"):
        print(file)
        
#Listing all files in a directory using pathlib module
from pathlib import Path
folder = Path("docs")
for file in folder.glob("*.txt"):
    print(file.name)

#OS module: getcwd() - chdir() -listdir() -mkdir() - makedirs() - rmdir() - remove() - rename() - os.path
#shutil module: copy() - copy2() - move() - copytree() - rmtree()
#pathlib.path: exists() - is_file() - is_dir() - mkdir() - read_text() - write_text() - unlink() - rename()
