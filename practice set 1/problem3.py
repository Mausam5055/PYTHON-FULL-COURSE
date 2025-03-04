# Q:WRITE A PYTHON PROGRAM TO PRINT THE CONTENTS OF THE DISK DRIVE PRESNT 
# IN THS LAPTOP USING 'OS MODULE'

import os

# specify the directory you want to list
directory_path = '/'

# list all the files and the directories in the specified path 
contents = os.listdir(directory_path)

# print each file and directory NameErrorfor item in contents:
for item in  contents:
    print(item)