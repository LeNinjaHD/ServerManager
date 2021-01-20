import sys
import importlib
import os

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
#clear()
print("ServerManager v1.0 - Main Menu")
line(2)
if sys.version_info.major != 3:
    print("Python 3 is required.")
    quit()
print("Select Something:")
print("[1] Create New Server")
print("[2] Create Server from Template")
print("[0] Exit")
action = input("Select An Action: ")
if(action == "1"):
    importlib.import_module("module_servercreator")
elif(action == "2"):
    importlib.import_module("module_servertemplate")
elif(action == "0"):
    quit()
else:
    print("Action Not Found!")
