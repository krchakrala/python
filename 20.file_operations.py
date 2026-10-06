#file operations in Python
#syntax: file = open("sample.txt", "mode")


#Basic file operations in Python
import os
if os.path.exists("docs/sample.txt"):
    file = open("docs/sample.txt", "r")
    content = file.read()
    print(content)
    file.close()
else:
    with open("docs/sample.txt", "w") as file:
         file.write("Hello Python\n")

#Using "with" statement to open a file
with open("docs/sample.txt", "r") as file:
    content = file.read()

print(content)

#Reading a file line by line
with open("docs/sample.txt", "r") as file:
    print(file.readline())
    print("Read file with readlines(): ", file.readlines())

#Reading a file and printing each line
with open("docs/sample.txt", "r") as file:
    for line in file:
        print(line.strip())

#Reading a file and storing lines in a list
with open("docs/sample.txt", "r") as file:
    lines = file.readlines()

print(lines)

#Writing to a file
with open("docs/employee.txt", "w") as file:
    file.write("Name: Ravi Krishna\n")
    file.write("Technology: Python programmer\n")

#appending to a file
with open("docs/sample.txt", "a") as file:
    file.write("\nExperience: 5 years\n")
    file.write("Location: Hyderabad\n")

#create new file and write to it
with open("docs/new_file.txt", "w") as file:
    file.write("This is a new file created using Python.\n")
    file.write("It contains some sample text.\n")

#Writing multiple lines to a file using writelines()
technologies = [
    "Python\n",
    ".NET\n",
    "Azure\n"
]
with open("docs/technologies.txt", "w") as file:
    file.writelines(technologies)

#Writing multiple lines to a file using writelines() without newline characters
technologies = ["Python", ".NET", "Azure"]
with open("docs/technologies1.txt", "w") as file:
    file.writelines(technologies)

#Checking if a file exists
import os
if os.path.exists("docs/sample.txt"):
    print("File exists")
else:
    print("File does not exist")

# #Creating a new file using "x" mode
try:
    with open("docs/newfile3.txt", "x") as file:
        file.write("Hello Python")
except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print("Unexpected error:", e)

#Checking if a file exists before creating it
import os
if os.path.exists("docs/newfile7.txt"):
      print("File exists")
else:
    with open("docs/newfile7.txt", "x") as file:
        file.write("Hello Python")

#Creating directories using os.makedirs()
import os
os.makedirs("docs/new_directory", exist_ok=True)

#Creating a directory if it doesn't exist
if not os.path.exists("docs/PythonFiles"):
    os.mkdir("docs/PythonFiles")

#Creating nested directories using os.makedirs()
import os
if not os.path.exists("docs/Project/Data/Input"):
    os.makedirs("docs/Project/Data/Input")

#Removing a directory using os.rmdir()
import os
os.rmdir("docs/PythonFiles")

import shutil
shutil.rmtree("docs/Project")

#Removing a file using os.remove() if file exists
import os
if os.path.exists("docs/newfile7.txt"):
    os.remove("docs/newfile7.txt")
else:
    print("File does not exist")

#os.path.exists()	Check whether path exists
#os.path.isfile()	Check whether it is a file
#os.path.isdir()	Check whether it is a directory
#os.path.join()	    Combine paths
#os.path.abspath()	Get absolute path
#os.path.basename()	Get filename
#os.path.dirname()	Get directory
#os.path.splitext()	Separate extension
#os.path.getsize()	Get file size


