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
type = input("What Servertype should the Server be? (Paper) \n> ")
if(type == "Paper"):
    version = input("Which Version should the Spigot Server be? (1.16.5, 1.15.2, 1.14.4, 1.13.2, 1.12.2, 1.11.2, 1.10.2, 1.9.4, 1.8.8) \n> ")
    if(version == "1.16.5"):
        port = input("Which Port should the Server be? \n> ")
        line(1)
        os.mkdir(name)
        with open(name + "/start.sh", "w") as f:
            f.write("java -jar paper.jar nogui")
        with open(name + "/eula.txt", "w") as f:  
            f.write("eula=true")
        with open(name + "/server.properties", "w") as f:
            f.write("motd=Made with ServerManager by LeNinjaHD and Astrago\nserver-port=" + port)
        os.chmod(name + "/start.sh", 0o777)
        urllib.request.urlretrieve("https://papermc.io/api/v2/projects/paper/versions/1.16.5/builds/429/downloads/paper-1.16.5-429.jar", name + "/paper.jar")
        print("Your New Server is in " + name + "/. Enter ./start.sh to start the Server. It will be available on Port " + port + ".")
    elif(version == "1.15.2"):
        port = input("Which Port should the Server be? \n> ")
        line(1)
        os.mkdir(name)
        with open(name + "/start.sh", "w") as f:
            f.write("java -jar paper.jar nogui")
        with open(name + "/eula.txt", "w") as f:  
            f.write("eula=true")
        with open(name + "/server.properties", "w") as f:
            f.write("motd=Made with ServerManager by LeNinjaHD and Astrago\nserver-port=" + port)
        os.chmod(name + "/start.sh", 0o777)
        urllib.request.urlretrieve("https://papermc.io/api/v2/projects/paper/versions/1.15.2/builds/391/downloads/paper-1.15.2-391.jar", name + "/paper.jar")
        print("Your New Server is in " + name + "/. Enter ./start.sh to start the Server. It will be available on Port " + port + ".")
    elif(version == "1.14.4"):
        port = input("Which Port should the Server be? \n> ")
        line(1)
        os.mkdir(name)
        with open(name + "/start.sh", "w") as f:
            f.write("java -jar paper.jar nogui")
        with open(name + "/eula.txt", "w") as f:  
            f.write("eula=true")
        with open(name + "/server.properties", "w") as f:
            f.write("motd=Made with ServerManager by LeNinjaHD and Astrago\nserver-port=" + port)
        os.chmod(name + "/start.sh", 0o777)
        urllib.request.urlretrieve("https://papermc.io/api/v2/projects/paper/versions/1.14.4/builds/243/downloads/paper-1.14.4-243.jar", name + "/paper.jar")
        print("Your New Server is in " + name + "/. Enter ./start.sh to start the Server. It will be available on Port " + port + ".")
    elif(version == "1.13.2"):
        port = input("Which Port should the Server be? \n> ")
        line(1)
        os.mkdir(name)
        with open(name + "/start.sh", "w") as f:
            f.write("java -jar paper.jar nogui")
        with open(name + "/eula.txt", "w") as f:  
            f.write("eula=true")
        with open(name + "/server.properties", "w") as f:
            f.write("motd=Made with ServerManager by LeNinjaHD and Astrago\nserver-port=" + port)
        os.chmod(name + "/start.sh", 0o777)
        urllib.request.urlretrieve("https://papermc.io/api/v2/projects/paper/versions/1.13.2/builds/655/downloads/paper-1.13.2-655.jar", name + "/paper.jar")
        print("Your New Server is in " + name + "/. Enter ./start.sh to start the Server. It will be available on Port " + port + ".")
    elif(version == "1.12.2"):
        port = input("Which Port should the Server be? \n> ")
        line(1)
        os.mkdir(name)
        with open(name + "/start.sh", "w") as f:
            f.write("java -jar paper.jar nogui")
        with open(name + "/eula.txt", "w") as f:  
            f.write("eula=true")
        with open(name + "/server.properties", "w") as f:
            f.write("motd=Made with ServerManager by LeNinjaHD and Astrago\nserver-port=" + port)
        os.chmod(name + "/start.sh", 0o777)
        urllib.request.urlretrieve("https://papermc.io/api/v2/projects/paper/versions/1.12.2/builds/1618/downloads/paper-1.12.2-1618.jar", name + "/paper.jar")
        print("Your New Server is in " + name + "/. Enter ./start.sh to start the Server. It will be available on Port " + port + ".")
    elif(version == "1.11.2"):
        port = input("Which Port should the Server be? \n> ")
        line(1)
        os.mkdir(name)
        with open(name + "/start.sh", "w") as f:
            f.write("java -jar paper.jar nogui")
        with open(name + "/eula.txt", "w") as f:  
            f.write("eula=true")
        with open(name + "/server.properties", "w") as f:
            f.write("motd=Made with ServerManager by LeNinjaHD and Astrago\nserver-port=" + port)
        os.chmod(name + "/start.sh", 0o777)
        urllib.request.urlretrieve("https://papermc.io/api/v2/projects/paper/versions/1.11.2/builds/1104/downloads/paper-1.11.2-1104.jar", name + "/paper.jar")
        print("Your New Server is in " + name + "/. Enter ./start.sh to start the Server. It will be available on Port " + port + ".")
    elif(version == "1.10.2"):
        port = input("Which Port should the Server be? \n> ")
        line(1)
        os.mkdir(name)
        with open(name + "/start.sh", "w") as f:
            f.write("java -jar paper.jar nogui")
        with open(name + "/eula.txt", "w") as f:  
            f.write("eula=true")
        with open(name + "/server.properties", "w") as f:
            f.write("motd=Made with ServerManager by LeNinjaHD and Astrago\nserver-port=" + port)
        os.chmod(name + "/start.sh", 0o777)
        urllib.request.urlretrieve("https://papermc.io/api/v2/projects/paper/versions/1.10.2/builds/916/downloads/paper-1.10.2-916.jar", name + "/paper.jar")
        print("Your New Server is in " + name + "/. Enter ./start.sh to start the Server. It will be available on Port " + port + ".")
    elif(version == "1.9.4"):
        port = input("Which Port should the Server be? \n> ")
        line(1)
        os.mkdir(name)
        with open(name + "/start.sh", "w") as f:
            f.write("java -jar paper.jar nogui")
        with open(name + "/eula.txt", "w") as f:  
            f.write("eula=true")
        with open(name + "/server.properties", "w") as f:
            f.write("motd=Made with ServerManager by LeNinjaHD and Astrago\nserver-port=" + port)
        os.chmod(name + "/start.sh", 0o777)
        urllib.request.urlretrieve("https://papermc.io/api/v2/projects/paper/versions/1.9.4/builds/773/downloads/paper-1.9.4-773.jar", name + "/paper.jar")
        print("Your New Server is in " + name + "/. Enter ./start.sh to start the Server. It will be available on Port " + port + ".")
    elif(version == "1.8.8"):
        port = input("Which Port should the Server be? \n> ")
        line(1)
        os.mkdir(name)
        with open(name + "/start.sh", "w") as f:
            f.write("java -jar paper.jar nogui")
        with open(name + "/eula.txt", "w") as f:  
            f.write("eula=true")
        with open(name + "/server.properties", "w") as f:
            f.write("motd=Made with ServerManager by LeNinjaHD and Astrago\nserver-port=" + port)
        os.chmod(name + "/start.sh", 0o777)
        urllib.request.urlretrieve("https://papermc.io/api/v2/projects/paper/versions/1.8.8/builds/443/downloads/paper-1.8.8-443.jar", name + "/paper.jar")
        print("Your New Server is in " + name + "/. Enter ./start.sh to start the Server. It will be available on Port " + port + ".")
else:
    print("Servertype not found.")