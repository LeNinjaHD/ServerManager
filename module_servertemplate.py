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
def createtemplate(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise
clear()
print("Create Server from Template")
line(2)
folder = input("In which Folder is the Template Stored? \n> ")
target = input("How should the new Server be called? \n> ")
createtemplate(folder, target)
port = input("Which Port should the Server be? \n> ")
with open(target + "/server.properties", "w") as f:
            f.write("motd=Made with ServerManager by LeNinjaHD and Astrago\nserver-port=" + port)