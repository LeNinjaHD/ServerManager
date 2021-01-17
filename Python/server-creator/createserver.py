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
def line(lines):
    i=0
    while(i != lines):
        print("")
        i = i + 1
clear()
print("Create New Server")
line(2)
name = input("How should the Server be called? \n> ")
type = input("What Servertype should the Server be? (Spigot) \n> ")
if(type == "Spigot"):
    version = input("Which Version should the Spigot Server be? (1.16.4) \n> ")
    if(version == "1.16.4"):
        port = input("Which Port should the Server be? \n> ")
        line(1)
        os.mkdir(name)
        startscript = open(name + "/start.sh", "w")
        startscript.write("java -jar spigot.jar")
        startscript.close()
        eula = open(name + "/eula.txt", "w")
        eula.write("eula=true")
        eula.close()
        sp = open(name + "/server.properties", "w")
        sp.write("motd=Made with ServerManager by LeNinjaHD and Astrago\nserver-port=" + port)
        sp.close
        os.chmod(name + "/start.sh", 0o777)
        urllib.request.urlretrieve("https://leprofi.com/download/servermanager/spigot-1.16.4.jar", name + "/spigot.jar")
        print("Your New Server is in " + name + "/. Enter ./start.sh to start the Server. It will be available on Port " + port + ".")
else:
    print("Servertype not found.")