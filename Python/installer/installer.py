import os
from time import *
import urllib

def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 
def DownloadFiles():
    files = urllib.URLopener()
    files.retrieve("https://randomsite.com/file.gz", "file.gz")
clear()
print("ServerManager Installer")
print("")
print("Made by LeNinjaHD and AstragoYT")
print("GitHub Repository: https://github.com/LeNinjaHD/ServerManager")
print("")
print("Installation Starts in 5 Seconds. Press Ctrl+C to Cancel")
try:
    sleep(5)
    
except KeyboardInterrupt:
    print("Cancelling...")
    quit()