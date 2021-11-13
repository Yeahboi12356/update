import os
import itertools
import sys
import time
import threading
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
      done = False
      def log():
                for c in itertools.cycle(['|','/','-','|','/','-','|']):
                    if done:
                        break
                    sys.stdout.write('\rchecking pankages' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\r     ')
      t = threading.Thread(target=log)
      t.start()
      time.sleep(5)
      done = True
      print("starting...")
      sleep(3)
      os.system("start-terminal.exe")
    else:
        n = input("are you sure to upgrade pankages? y/n: ")
        if n == "y":
          files = input("your username: ")
          os.system("git clone https://github.com/Yeahboi12356/update && cp update/terminal.py home/" + files )
          print("clik y to continue")
          os.system("rd /s update")
          print("restarting terminal..")
          sleep(5)
          os.system("start-terminal.exe")
        elif n == "n":
          print("restarting terminal")
          os.system("start-terminal.exe")
        else:
            print("number not valid")
            os.system("py nisupgrade.py")
