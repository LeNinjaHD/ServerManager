import pathlib
print("ServerManager Linux Installer")
print("")
print("")
#path = input("Where is the ServerManager Installation located? (for example: /home/user/servermanager) \n> ")
path = pathlib.Path(__file__).parent.absolute()
print(path)
with open("/usr/bin/servermanager", "w") as f:
    f.write("#!/bin/bash\n")
    f.write("python3 " + path + "/servermanager.py")