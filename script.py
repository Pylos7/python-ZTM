# Working With Files In Python

# Modes - r = read, w = write, a = append, r+ = read and write
with open('app/sad.txt', mode='r') as my_file: # No need to close the file
    print(my_file.read())