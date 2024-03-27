''' 1. Write a Python script that lists all files and directories in the current working directory using the os.listdir() function.
2. Create a function that checks if a given path (file or directory) exists using os.path.exists() and os.path.isdir() or os.path.isfile() accordingly.
3. Develop a script that recursively searches for all files with a specific extension (e.g., ".txt") in a given directory and its subdirectories. Print the absolute paths of these files.
4. Develop a function that returns the last modified time of a file specified by its path using os.path.getmtime() and time.ctime() for a human-readable timestamp.
5. Create a script that checks the permissions (readable, writable, executable) of a file specified by its path using os.access() and the appropriate constants from the os module.
6. Create a python script that uses os module to give filepath for the pandas read. '''


# Q1

print(os.listdir())


# Q2
def path_exist(path):
  if os.path.exists(path):
    if os.path.isdir(path):
      return 'Path exists and it is a directory'
    elif os.path.isfile(path):
      return 'Path exists and it is a file'
  else:
    return 'Path doesn\'t exist.'
  

path_exist('/content/sample_data/anscombe.json')



# Q3  

text_files_abs_path = []
def all_text_files(path):
  if os.path.isdir(path):
    for subdir in os.listdir(path):
      all_text_files(os.path.join(path,subdir))
  elif os.path.isfile(path) and os.path.splitext(path)[1] == '.txt':
    text_files_abs_path.append(path)
  
  return text_files_abs_path

all_text_files('/content/sample_data') 


# Q4

import time

def last_modified_time(path):
  if os.path.exists(path):
    date_time = time.ctime(os.path.getmtime(path))
    return date_time
  
path = '/content/sample_data/newdirectory/newfile.py'
last_modified_time(path)


# Q5

def check_permission(path):
  if os.access(path,os.F_OK) and os.path.isfile(path):
    print('Path Exists')
    print('Write Access is granted') if os.access(path,os.W_OK) else print('Write Access is not granted')
    print('Read Access is granted') if os.access(path,os.R_OK) else  print('Read Access is not granted')
    print('File is executable') if os.access(path,os.X_OK) else print('File is not executable')   
  else:
    print('Path doesn\'t exist')
  

check_permission('/content/sample_data/newdirectory/newfile.py')



# Q6


import pandas as pd
import os

source_folder = 'source_folder'
source_file = 'source_sales.csv'


path =  os.path.join(os.path.dirname(__file__),source_folder,source_file) if os.path.isfile(os.path.join(os.path.dirname(__file__),source_folder,source_file)) else 'File doesn\'t exist'

print(path)
df = pd.read_csv(path)
print(df)
