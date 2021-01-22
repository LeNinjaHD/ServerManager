import os
from time import *
import shutil, errno

def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 
def line(lines):
    i=0
    while(i != lines):
        print("")
        i = i + 1
def createbackup(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise
print("Create Server Backup")
line(2)
src = input("Where is the Server located? \n> ")
target = input("Where should the Backup be stored? \n> ")
createbackup(src, target)