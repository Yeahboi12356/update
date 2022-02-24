import os
from time import sleep
os.system("del gisugrade.py")
os.system("""copy "update\gisupgrade.py" gisupgrade.py""")
print("clik y to continue")
os.system("rd /s update")
print("restarting terminal..")
sleep(5)
os.system("start-terminal.exe")
      
