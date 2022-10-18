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



