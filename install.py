import urllib.request
import subprocess
import time

url = "http://dyn.astrago.de/McServermanager"


def download(url, filename):
    # with urllib.request.urlopen(url) as dl_file:
    #     with open(filename, 'wb') as out_file:
    #         out_file.write(dl_file.read())

    urllib.request.urlretrieve(url, filename)


print("installing dependencies...")
download(url + "/dependencies.txt", "dependencies.txt")
subprocess.call(["py", "-m", "pip", "install",
                 "-r", "dependencies.txt"], shell=True)
time.sleep(2)
subprocess.call(["rm", "-r", "dependencies.txt"])

print("downloading servermanager")
download(url + "/servermanager.py", "servermanager.py")
time.sleep(2)
subprocess.call(["rm", "-r", "install.py"])
