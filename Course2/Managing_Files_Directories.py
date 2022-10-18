import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as file:
    file.write(comments)
    file.close()
    filesize = os.stat(filename).st_size
  return(filesize)

print(create_python_script("program.py"))

import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
          
          parent_dir = os.path.abspath(os.getcwd())
          path = os.path.join(parent_dir, directory)
          os.mkdir(path)
          print(os.getcwd())
          print(os.listdir(os.getcwd()))

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open(filename, "w") as file:
       file.close()

  # Return the list of files in the new directory
  return (os.listdir(os.getcwd()))

print(new_directory("PythonPrograms", "script.py"))

import os
import os.path, time
import datetime
from datetime import date

def file_date(filename):
  with open(filename, "w") as file :
    file.close()
  #print(os.listdir(os.getcwd()))

  modTimesinceEpoc = os.path.getmtime(filename)
  # Convert seconds since epoch to readable timestamp
  modificationTime = time.strftime('%Y-%m-%d', time.localtime(modTimesinceEpoc))
  return ("{}".format(modificationTime))

print(file_date("newfile.txt"))


import os
def parent_directory():
      # Create a relative path to the parent 
      # of the current working directory 

      directory = os.path.basename(os.getcwd())
      parent_dir = os.path.abspath(os.getcwd())
      relative_parent = os.path.join(parent_dir, directory)
      os.mkdir(relative_parent)
      print(os.getcwd())
      print(os.listdir(os.getcwd()))

print(parent_directory())
