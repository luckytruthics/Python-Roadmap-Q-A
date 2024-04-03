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

def all_text_files(file_path):
  paths = []
  def inner_fun(file_path):
    nonlocal paths
    if os.path.isdir(file_path):
      for subdir in os.listdir(file_path):
        inner_fun(os.path.join(file_path,subdir))
    elif os.path.isfile(path) and os.path.splitext(file_path)[1] == '.txt':
      paths.append(path)

  inner_fun(path)
  return paths

all_text_files('/content/sample_data')


# Q4

import time

def last_modified_time(file_path):
  if os.path.exists(file_path):
    date_time = time.ctime(os.path.getmtime(file_path))
    return date_time
  
file_path = '/content/sample_data/newdirectory/newfile.py'
last_modified_time(file_path)


# Q5

def check_permission(file_path):
  if os.access(file_path,os.F_OK) and os.path.isfile(file_path):
    print('Path Exists')
    print('Write Access is granted') if os.access(file_path,os.W_OK) else print('Write Access is not granted')
    print('Read Access is granted') if os.access(file_path,os.R_OK) else  print('Read Access is not granted')
    print('File is executable') if os.access(file_path,os.X_OK) else print('File is not executable')   
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
