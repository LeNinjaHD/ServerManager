print("ServerManager Linux Installer")
print("")
print("")
path = input("Where is the ServerManager Installation located? (for example: /home/user/servermanager) \n> ")
with open("/usr/bin/servermanager", "w") as f:
    f.write("#!/bin/bash\n")
    f.write("python3 " + path + "servermanager.py")