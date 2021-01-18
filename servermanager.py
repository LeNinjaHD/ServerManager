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
clear()
print("ServerManager v1.0 - Main Menu")
line(2)
print("Select Something:")
print("[1] Create New Server")
print("[2] Exit")
action = input("Select An Action: ")
if(action == "1"):
    importlib.import_module("createserver")
elif(action == "2"):
    quit()
else:
    print("Action Not Found!")
