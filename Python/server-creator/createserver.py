import os
from time import *
import urllib.request

def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 
def line():
    print("")
clear()
print("Create New Server")
line()
line()
name = input("How should the Server be called? \n> ")
type = input("What Servertype should the Server be? (Spigot) \n> ")
if(type == "Spigot"):
    version = input("Which Version should the Spigot Server be? (1.16.4) \n> ")
    if(version == "1.16.4"):
        line()
        os.mkdir(name)
        startscript = open(name + "/start.sh", "w")
        startscript.write("java -jar spigot.jar")
        startscript.close()
        eula = open(name + "/start.sh", "w")
        eula.write("eula=true")
        eula.close()
        sp = open(name + "/server.properties", "w")
        sp.write("motd=§6Server Made with §2ServerManager §6by §3LeNinjaHD and Astrago")
        sp.close
        os.chmod(name + "/start.sh", 0o777)
        urllib.request.urlretrieve("https://leprofi.com/download/servermanager/spigot-1.16.4.jar", name + "/spigot.jar")
else:
    print("Servertype not found.")