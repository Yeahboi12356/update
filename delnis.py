import os
from time import sleep
os.system("cp update/nisupgrade.py nisupgrade.py")
print("clik y to continue")
os.system("rd /s update")
print("restarting terminal..")
sleep(5)
os.system("py start-terminal.py") 
      
