# 4. Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 



import os

# Specify the directory path
directory_path = 'E:\\Bani test folder'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print the contents
print(contents)

