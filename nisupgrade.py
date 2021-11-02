import os
from time import sleep
print("\nnew pankages: camera-security,version,default")
n = input("are you sure to upgrade pankages? y/n: ")
if n == "y":
  files = input("your username: ")
  os.system("git clone https://github.com/Yeahboi12356/update && cp update/terminal.py home/" + files)
  print("clik y to continue")
  os.system("rd /s update")
  print("restarting terminal..")
  sleep(5)
  os.system("py start-terminal.py")
elif n == "n":
  print("restarting terminal")
  os.system("py start-terminal.py")
else:
    print("number not valid")
    os.system("py nisupgrade.py")
