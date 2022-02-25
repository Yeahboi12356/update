import os
from time import sleep
import urllib.request

import urllib.request

url = "https://whoamilinix.000webhostapp.com/update.txt"
file = urllib.request.urlopen(url)

for line in file:
    decoded_line= line.decode("utf-8").strip()
    print(decoded_line)
    if decoded_line == "NOT AVAILABLE":
      print("all pankages up to date no update available")
      n = input("are you sure to upgrade pankages? y/n: ")
      if n == "y":
        os.system("git clone https://github.com/Yeahboi12356/update")
        os.system("update.bat")
      elif n == "n":
        print("starting...")
        sleep(3)
        os.system("start-terminal.exe")
      else:
        os.system("py nisupgrade.py")
    else:
        print("update available")
        n = input("are you sure to upgrade pankages? y/n: ")
        if n == "y":
          files = input("your username: ")
          os.system("git clone https://github.com/Yeahboi12356/update")
          os.system("update.bat")
        elif n == "n":
          print("restarting terminal")
          os.system("start-terminal.exe")
        else:
            print("number not valid")
            os.system("py nisupgrade.py")
