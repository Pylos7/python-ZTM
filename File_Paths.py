# File Paths

# Absolute File Paths - The entire file path from the root folder
# C:\Users\YourName\Documents\myFile.txt

# Relative File Paths - The file path relative to the location of the python file
# myFile.txt

with open('app/sad.txt', mode='r') as my_file: # No need to close the file
    print(my_file.read())

import pathlib # Module for working with file paths - Compatible with Windows and Mac
# Pathlib is a module that allows us to work with file paths