from getpass import getpass
import os
from time import sleep
import sys
import signal
import itertools
import threading
import time
import urllib.request
import random

logins = ["""\033[1;32;40m /$$                     /$$          
| $$                    |__/          
| $$  /$$$$$$   /$$$$$$  /$$ /$$$$$$$ 
| $$ /$$__  $$ /$$__  $$| $$| $$__  $$
| $$| $$  \ $$| $$  \ $$| $$| $$  \ $$
| $$| $$  | $$| $$  | $$| $$| $$  | $$
| $$|  $$$$$$/|  $$$$$$$| $$| $$  | $$
|__/ \______/  \____  $$|__/|__/  |__/
               /$$  \ $$              
              |  $$$$$$/              
               \______/               ""","""\033[1;32;40m
 _        _______  _______  __    _       
( \      (  ___  )(  ____ \/  \  ( (    /|
| (      | (   ) || (    \/\/) ) |  \  ( |
| |      | |   | || |        | | |   \ | |
| |      | |   | || | ____   | | | (\ \) |
| |      | |   | || | \_  )  | | | | \   |
| (____/\| (___) || (___) |__) (_| )  \  |
(_______/(_______)(_______)\____/|/    )_)
                                          ""","""\033[1;32;40m                                                           
 ____                _____          _____  _____   ______   
|    |          ____|\    \     ___|\    \|\    \ |\     \  
|    |         /     /\    \   /    /\    \\\    \| \     \ 
|    |        /     /  \    \ |    |  |____|\|    \  \     |
|    |  ____ |     |    |    ||    |    ____ |     \  |    |
|    | |    ||     |    |    ||    |   |    ||      \ |    |
|    | |    ||\     \  /    /||    |   |_,  ||    |\ \|    |
|____|/____/|| \_____\/____/ ||\ ___\___/  /||____||\_____/|
|    |     || \ |    ||    | /| |   /____ / ||    |/ \|   ||
|____|_____|/  \|____||____|/  \|___|    | / |____|   |___|/
  \(    )/        \(    )/       \( |____|/    \(       )/  
   '    '          '    '         '   )/        '       '   
                                      '                     """, """\033[1;32;40m                               
,--.              ,--.         
|  | ,---.  ,---. `--',--,--,  
|  || .-. || .-. |,--.|      \ 
|  |' '-' '' '-' '|  ||  ||  | 
`--' `---' .`-  / `--'`--''--' 
           `---'                """]
sh = ["HELLO WORLD!","script by who","type nise to install or update","visit my site https://whoamilinix.000webhostapp.com"]
def utama():
    os.system("cls")
    print("\nif you want update pls connect to wifi")
    print("are you want to update pankages?:")
    print("1.update")
    print("2.skip")
    y = int(input(">"))
    if y == 1:
        ayimation = ["[□□□□□□□□□□]0%","[■□□□□□□□□□]10%","[■■□□□□□□□□]20%", "[■■■□□□□□□□]30%", "[■■■■□□□□□□]40%","[■■■■■□□□□□]50%", "[■■■■■■□□□□]60%", "[■■■■■■■□□□]70%", "[■■■■■■■■□□]80%", "[■■■■■■■■■□]90%", "[■■■■■■■■■■]100%"]
        for i in range(len(ayimation)):
            time.sleep(1)
            sys.stdout.write("\rchecking pankages " + ayimation[i % len(ayimation)])
            sys.stdout.flush()     
        sleep(3)
        print("\033[1;32;40m|OK\033[1;37;40m")
        animation = ["[□□□□□□□□□□]0%","[■■■■■□□□□□]50%", "[■■■■■■□□□□]60%", "[■■■■■■■□□□]70%", "[■■■■■■■■□□]80%", "[■■■■■■■■■□]90%", "[■■■■■■■■■■]100%"]
        for i in range(len(animation)):
            time.sleep(2)
            sys.stdout.write("\rchecking update   " + animation[i % len(animation)])
            sys.stdout.flush()
        print("\033[1;32;40m|OK\033[1;37;40m")
        print("update complete")
        print("New pankages:\n")
        sleep(5)
        url = "https://whoamilinix.000webhostapp.com/update.txt"
        file = urllib.request.urlopen(url)

        for line in file:
            decoded_line= line.decode("utf-8").strip()
            print(decoded_line)
            if decoded_line == "NOT AVAILABLE":
                print("all pankages up to date no update available")
                sleep(5)
                login()
            else:
                n = input("are you want to upgrade pankages? y/n: ")
                if n == "y":
                    files = input("your username: ")
                    os.system("git clone https://github.com/Yeahboi12356/update")
                    os.system("update.bat")
                elif n == "n":
                    print("restarting terminal")
                    os.system("start-terminal.exe")
                else:
                    print("input not valid upgrade has been canceled")
                    sleep(3)
                    login()
    elif y == 2:
        login()
    else:
        login()
                
def login():
    print("\n")
    os.system("cls")
    print(random.choice(logins))
    print(random.choice(sh))
    p = input("\033[1;33;40musernames: \033[1;37;40m")
    print("\033[1;31;40mpassword security sensor mode=ON")
    y = getpass("\033[1;36;40mpassword: \033[1;37;40m")
    filess = open("user/share/jasp/password.txt",'r')
    files = open("user/share/jasp/username.txt",'r')
    filess = open("user/share/jasp/password.txt",'r')
    if p == files.readline() and y == filess.readline():
        print("\033[1;32;40mlogin complete")
        hostname()
    else:
        print("\033[1;31;40mlogin denied")
        sleep(2)
        os.system("cls")
        login()


def hostname():
    t = input("\033[1;33;40mcustom/default: \033[1;37;40m")
    if t == "custom":
        terminal()
    elif t == "default":
        default()
    else:
        print("\033[1;31;40mtype the hostname correctly!! \033[1;37;40m")
        hostname()
def changehost():
    print("1.custom hostname")
    print("2.default hostname")
    p = int(input("select number:>"))
    if p == 1:
        terminal()
    elif p == 2:
        default()
    else:
        print("use default hostname")
        default()
def terminal():
    files = open("user/share/jasp/username.txt",'r')
    filesss = open("user/share/jasp/hostname-custom.txt",'r')
    print("\033[1;34;40m┌──(" + "\033[1;31;40m" + files.readline() + "\033[1;32;40m@" + "\033[1;33;40m" + filesss.readline() + "\033[1;34;40m)────(~)")
    gj = input("\033[1;34;40m└─" + "\033[1;31;40m# \033[1;37;40m")

    if gj == "ls":    
        os.system("dir")
        terminal()
    elif gj == "dir":
        os.system("dir")
        terminal()
    elif gj == "help":
        print("nise             pankages for terminal ")
        print("ls/dir           show folder and file")
        print("version          check version terminal")
        print("list pankages    show pankages or tools")
        print("clear/cls        clearing terminal")
        print("network          showing ssid and pass wifi ever connected to wifi")
        print("ifconfig         showing network interfaces")
        print("ping             showing ping ip or website")
        print("\n")
        terminal()
    elif gj == "nise":
        print("update                       update pankages")
        print("upgrade                      upgrade terminal")
        print("install                      install pankages")
        print("list pankages                check pangkages")
        print("\n")
        terminal()
    elif gj == "nise ":
        print("update                       update pankages")
        print("upgrade                      upgrade terminal")
        print("install                      install pankages")
        print("list pankages                check pangkages")
        print("\n")
        terminal()
    elif gj == "ping":
        p = input("input> ")
        os.system("ping " + p)
        terminal()
    elif gj == "nise update":
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
        time.sleep(10)
        done = True
        print("pankages up to date")
        print("cleaning 5 seconds..")
        sleep(5)
        os.system("cls")
        terminal()
    elif gj ==  "ifconfig":
        os.system("ipconfig")
        terminal()
    elif gj == "version":
        print("version:1.2.0.1")
        print("nise pankages: 1.2.0.1")
        terminal()
    elif gj == "nise upgrade":
        done = False
        def loading():
                for c in itertools.cycle(['|','/','-','|','/','-','|']):
                    if done:
                        break
                    sys.stdout.write('\rchecking pankages' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\r     ')
        t = threading.Thread(target=loading)
        t.start()
        time.sleep(10)
        done = True
        print("update complete")
        print("New pankages:")
        os.system("python gisupgrade.py")

    elif gj == "list pankages":
        print("list pankages:>")
        print("\n")
        print("sqlmap")
        print("XAMPP/xampp")
        print("php")
        print("wireshark")
        print("camera-security")
        print("phoneinfoga")
        print("\n")
        terminal()
    elif gj == "nise list pankages":
        print("list pankages:>")
        print("\n")
        print("sqlmap")
        print("XAMPP/xampp")
        print("php")
        print("wireshark")
        print("camera-security")
        print("phoneinfoga")
        print("\n")
        terminal()
    elif gj == "cls":
        os.system("cls")
        terminal()
    elif gj == "clear":
        os.system("cls")
        terminal()
    elif gj == "python":
        os.system("python")
        terminal()
    elif gj == "python --help":
        print("python has modified by who for work in this terminal")
        print("python -f running file but just type python -f do not like python -f main.py dont do this!!")
        print("python --help for more information")
        terminal()
    elif gj == "python -f":
        y = input("input you file: ")
        os.system("python " + y)
        print(" ")
        terminal()
    elif gj == "python -h":
        print("python has modified by who for work in this terminal")
        print("python -f running file but just type python -f do not like python -f main.py dont do this!!")
        print("python --help for more information")
        terminal()
    elif gj == "nise install sqlmap":
        z = input("do you want install sqlmap? y/n: ")
        if z == "y":
            done = False
            def load():
                    for c in itertools.cycle(['|','/','-','|','/','-','|']):
                        if done:
                            break
                        sys.stdout.write('\rchecking pankages' + c)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    sys.stdout.write('\r     ')
            t = threading.Thread(target=load)
            t.start()
            time.sleep(10)
            done = True
            os.system("cd user/share && git clone https://github.com/sqlmapproject/sqlmap")
            print("pankages has been installed")
            print("if you wanna run sqlmap just type sqlmap -h or sqlmap --help if you type sqlmap command not found")
            print ("cleaning 10 seconds...")
            sleep(10)
            os.system("cls")
            terminal()
        elif z == "n":
            terminal()
        else:
            terminal()
    elif gj == "nise install phoneinfoga":
        print("requirements:")
        print("""requests==2.21.0 bs4==0.0.1 
        html5lib==1.0.1 phonenumbers==8.10.2
        argparse==1.2.1 urllib3==1.24.2
        colorama==0.4.1""")
        e = input("do you want install phoneinfoga? y/n: ")
        if e == "y":
            done = False
            def load():
                    for c in itertools.cycle(['|','/','-','|','/','-','|']):
                        if done:
                            break
                        sys.stdout.write('\rchecking pankages' + c)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    sys.stdout.write('\r     ')
            t = threading.Thread(target=load)
            t.start()
            time.sleep(10)
            done = True
            os.system("cd user/share && git clone https://github.com/Yeahboi12356/phoneinfoga && cd phoneinfoga && pip install -r requirements.txt")
            print("pankages has been installed")
            print("if you wanna run phoneinfoga just type phoneinfoga -h or phoneinfoga --help")
            print ("cleaning 10 seconds...")
            sleep(10)
            os.system("cls")
            terminal()
        elif e == "n":
            terminal()
        else:
            terminal()
    elif gj == "finduserwifi":
        try:
            ri = open("user/share/liduserwifi/finduserwifi/map-7.92/tes.py")
            os.system("cd user/share/liduserwifi/finduserwifi/map-7.92 && python tes.py")
            terminal()
        except:
            print("you haven't installed finduserwifi")
            print("type nise install finduserwifi")
            terminal()
    elif gj == "nise install finduserwifi":
        print("pankages and app need to install:")
        print("terminaltables nmap npcap")
        r = input('are you sure want to install? y/n: ')
        if r == "y":
            os.system("pip install terminaltables && cd user/share && git clone https://github.com/Yeahboi12356/liduserwifi && cd liduserwifi && finduserwifi.bat")
            terminal()     
        elif r == "n":
            terminal()
        else:
            terminal()
    elif gj == "phoneinfoga -h":
        try:
            ri = open("user/share/phoneinfoga/phoneinfoga.py", "r")
            print("    ___ _                       _____        __                   ")
            print("   / _ \ |__   ___  _ __   ___  \_   \_ __  / _| ___   __ _  __ _ ")
            print("  / /_)/ '_ \ / _ \| '_ \ / _ \  / /\/ '_ \| |_ / _ \ / _` |/ _` |")
            print(" / ___/| | | | (_) | | | |  __/\/ /_ | | | |  _| (_) | (_| | (_| |")
            print(" \/    |_| |_|\___/|_| |_|\___\____/ |_| |_|_|  \___/ \__, |\__,_|")
            print("                                                      |___/       ")
            print(" Coded by Sundowndev")
            print(" Modified by Who ")
            print("\n")
            print("phoneinfoga -n , --number    scanning number but just type phoneinfoga -n to run it")
            print("phoneinfoga -h , --help      showing help")
            print("\n")
            terminal()
        except:
            print("you haven't installed phoneinfoga")
            print("type nise install phoneinfoga")
            terminal()
    elif gj == "phoneinfoga --help":
        try:
            r = open("user/share/phoneinfoga/phoneinfoga.py", "r")
            print("    ___ _                       _____        __                   ")
            print("   / _ \ |__   ___  _ __   ___  \_   \_ __  / _| ___   __ _  __ _ ")
            print("  / /_)/ '_ \ / _ \| '_ \ / _ \  / /\/ '_ \| |_ / _ \ / _` |/ _` |")
            print(" / ___/| | | | (_) | | | |  __/\/ /_ | | | |  _| (_) | (_| | (_| |")
            print(" \/    |_| |_|\___/|_| |_|\___\____/ |_| |_|_|  \___/ \__, |\__,_|")
            print("                                                      |___/       ")
            print(" Coded by Sundowndev")
            print(" Modified by Who ")
            print("\n")
            print("phoneinfoga -n , --number    scanning number but just type phoneinfoga -n to run it")
            print("phoneinfoga -h , --help      showing help")
            print("\n")
            terminal()
        except:
            print("you haven't installed phoneinfoga")
            print("type nise install phoneinfoga")
            terminal()
    elif gj == "phoneinfoga":
        try:
            fil = open("user/share/phoneinfoga/phoneinfoga.py", "r")
            print("    ___ _                       _____        __                   ")
            print("   / _ \ |__   ___  _ __   ___  \_   \_ __  / _| ___   __ _  __ _ ")
            print("  / /_)/ '_ \ / _ \| '_ \ / _ \  / /\/ '_ \| |_ / _ \ / _` |/ _` |")
            print(" / ___/| | | | (_) | | | |  __/\/ /_ | | | |  _| (_) | (_| | (_| |")
            print(" \/    |_| |_|\___/|_| |_|\___\____/ |_| |_|_|  \___/ \__, |\__,_|")
            print("                                                      |___/       ")
            print(" Coded by Sundowndev")
            print(" Modified by Who ")
            print("\n")
            print("phoneinfoga -n , --number    scanning number but just type phoneinfoga -n to run it")
            print("phoneinfoga -h , --help      showing help")
            print("\n")
            terminal()
        except:
            print("you haven't installed phoneinfoga")
            print("type nise install phoneinfoga")
            terminal()
    elif gj == "phoneinfoga -n":
        try:
            fi = open("user/share/phoneinfoga/phoneinfoga.py", "r")
            print("    ___ _                       _____        __                   ")
            print("   / _ \ |__   ___  _ __   ___  \_   \_ __  / _| ___   __ _  __ _ ")
            print("  / /_)/ '_ \ / _ \| '_ \ / _ \  / /\/ '_ \| |_ / _ \ / _` |/ _` |")
            print(" / ___/| | | | (_) | | | |  __/\/ /_ | | | |  _| (_) | (_| | (_| |")
            print(" \/    |_| |_|\___/|_| |_|\___\____/ |_| |_|_|  \___/ \__, |\__,_|")
            print("                                                      |___/       ")
            print(" Coded by Sundowndev")
            print(" Modified by Who ")
            print("\n")
            print("use + exemple: +86")
            e =  input("number: ")
            y = os.system("python user/share/phoneinfoga/phoneinfoga.py -n " + e)
            terminal()
        except:
            print("you haven't installed phoneinfoga")
            print("type nise install phoneinfoga")
            terminal()
    elif gj == "phoneinfoga --number":
        try:
            fi = open("user/share/phoneinfoga/phoneinfoga.py", "r")
            print("    ___ _                       _____        __                   ")
            print("   / _ \ |__   ___  _ __   ___  \_   \_ __  / _| ___   __ _  __ _ ")
            print("  / /_)/ '_ \ / _ \| '_ \ / _ \  / /\/ '_ \| |_ / _ \ / _` |/ _` |")
            print(" / ___/| | | | (_) | | | |  __/\/ /_ | | | |  _| (_) | (_| | (_| |")
            print(" \/    |_| |_|\___/|_| |_|\___\____/ |_| |_|_|  \___/ \__, |\__,_|")
            print("                                                      |___/       ")
            print(" Coded by Sundowndev")
            print(" Modified by Who ")
            print("\n")
            print("use + exemple: +86")
            e =  input("number: ")
            y = os.system("python user/share/phoneinfoga/phoneinfoga.py -n " + e)
            terminal()
        except:
            print("you haven't installed phoneinfoga")
            print("type nise install phoneinfoga")
            terminal()
    elif gj == "nise install php":
        e = input("php folder is zip file are you sure want install php? y/n")
        if e == "y":
            print("ok don't forget to follow the instructions")
            print("1.chrome")
            print("2.terminal")
            h = int(input("your choose: "))
            if h == 1:
                def so():
                        for c in itertools.cycle(['|','/','-','|','/','-','|']):
                            if done:
                                break
                            sys.stdout.write('\rchecking browser' + c)
                            sys.stdout.flush()
                            time.sleep(0.1)
                            sys.stdout.write('\r     ')
                t = threading.Thread(target=so)
                t.start()
                time.sleep(10)
                done = True
                os.system("start chrome https://windows.php.net/downloads/releases/php-8.0.12-Win32-vs16-x64.ziphttps://windows.php.net/downloads/releases/php-8.0.12-Win32-vs16-x64.zip")
                print("instructions!!!")
                print("extract zip in your file manager")
                gd = input("done? y/n: ")
                if gd == "y":
                    print("open enviroment variables")
                    dgb = input("done? y/n: ")
                    if dgb == "y":
                        print("click Enviroment Variables")
                        print("choose Path on user variables")
                        print("clik edit")
                        gv = input("done? y/n")
                        if gv == "y":
                            print("clik new and type")
                            print("C:/user/Yourname/Phpfolderyourextract")
                            print("python cant use \ to text pls after copy thats text pls change / to \ ")
                            print("clik ok and ok and ok again")
                            gb = input("done? y/n: ")
                            if gb == "y":
                                print("php finished install")
                                sleep(3)
                                print("cleaning 10 seconds...")
                                sleep(10)
                                os.system("cls")
                            elif gb == "n":
                                terminal()
                            else:
                                terminal()
                        elif gv == "n":
                            terminal()
                        else:
                            terminal()
                    elif dgb == "n":
                        terminal()
                    else:
                        terminal()
                elif gd == "n":
                    terminal()
                else:
                    terminal()
            elif h == 2:
                done = False
                def lo():
                        for c in itertools.cycle(['|','/','-','|','/','-','|']):
                            if done:
                                break
                            sys.stdout.write('\rchecking pankages' + c)
                            sys.stdout.flush()
                            time.sleep(0.1)
                            sys.stdout.write('\r     ')
                t = threading.Thread(target=lo)
                t.start()
                time.sleep(10)
                done = True
                os.system("cd user/share && git clone https://github.com/Yeahboi12356/Php64bit && cd Php64bit && php64.bat")
                print("instructions!!!")
                gd = input("are you reddy? y/n: ")
                if gd == "y":
                    print("open enviroment variables")
                    dgb = input("done? y/n: ")
                    if dgb == "y":
                        print("click Enviroment Variables")
                        print("choose Path on user variables")
                        print("clik edit")
                        gv = input("done? y/n: ")
                        if gv == "y":
                            os.system("cls")
                            print("clik new and type")
                            print("C:/user/yourname/Desktop-or-where-you-put-folder-terminal-linux/terminal-linux/user/share/php/php")
                            print("python cant use \ to text pls after copy thats text pls change / to \ ")
                            print("clik ok and ok and ok again")
                            gb = input("done? y/n: ")
                            if gb == "y":
                                print("php finished install")
                                sleep(3)
                                print("cleaning 10 seconds...")
                                sleep(10)
                                os.system("cls")
                                terminal()
                            elif gb == "n":
                                terminal()
                            else:
                                terminal()
                        elif gv == "n":
                            terminal()
                    elif dgb == "n":
                        terminal()
                    else:
                        terminal()
                elif gd == "n":
                    terminal()
                else:
                    terminal()
    elif gj == "nise install camera-security":
        print("requirements: ")
        print("open-cv")
        y = input("are sure want to install camera-security y/n> ")
        if y == "y":
            done = False
            def lo():
                    for c in itertools.cycle(['|','/','-','|','/','-','|']):
                        if done:
                            break
                        sys.stdout.write('\rchecking pankages' + c)
                        sys.stdout.flush()
                        time.sleep(0.1)
                        sys.stdout.write('\r     ')
            t = threading.Thread(target=lo)
            t.start()
            time.sleep(10)
            done = True
            os.system("cd user/share && git clone https://github.com/Yeahboi12356/camera")
            os.system("pip install opencv-python")
            print("installation complete type camera for run it")
            terminal()
        elif y == "n":
            terminal()
        else:
            terminal()

    elif gj == "network":
        print("network --help                       show help")
        print("net                                  show help")
        print()
        print("network history:")
        print("network show wifi history            show history wifi ever used")
        print()
        print("informations network:")
        print("network ssid                         show informations network")
        print()
        print("password key:")
        print("network wifi key                     show wifi key")
        terminal()
    elif gj == "network ---help":
        print("network --help                       show help")
        print("net                                  show help")
        print()
        print("network history:")
        print("network show wifi history            show history wifi ever used")
        print()
        print("informations network:")
        print("network ssid                         show informations network")
        print()
        print("password key:")
        print("network wifi key                     show wifi key")
        terminal()
    elif gj == "net":
        print("network --help                       show help")
        print("net                                  show help")
        print()
        print("network history:")
        print("network show wifi history            show history wifi ever used")
        print()
        print("informations network:")
        print("network ssid                         show informations network")
        print()
        print("password key:")
        print("network wifi key                     show wifi key")
        terminal()
    elif gj == "network show wifi history":
        os.system("netsh wlan show profiles")
        terminal()
    elif gj == "network show wifi history ":
        os.system("netsh wlan show profiles")
        terminal()
    elif gj == "network ssid":
        yourdad = input("name ssid wifi:> ")
        os.system("netsh wlan show profiles " + yourdad)
        yourmom = input ("do you want to see the password?y/n:> ")
        if yourmom == "y":
            os.system("netsh wlan show profiles " + yourdad + " key=clear")
            print("password in Key Content")
            terminal()
        elif yourmom == "n":
            terminal()
        else:
            terminal()
    elif gj == "network wifi key":
        yourdad = input("name ssid wifi:> ")
        os.system("netsh wlan show profiles " + yourdad + " key=clear")
        print("password in Key Content")
        terminal()
    elif gj == "change hostname":
        changehost()
    elif gj == "camera":
        try:
            f = open("user/share/camera/camera-security.py")
            os.system("python user/share/camera/camera-security.py")
            terminal()
        except:
           print("you haven't installed camera-security")
           print("type nise install camera-security")
           terminal()
    elif gj == "camera-security":
        try:
            oy = open("user/share/camera/camera-security.py")
            print("type camera")
            terminal()
        except:
            print("you haven't installed camera-security")
            print("type nise install camera-security")
            terminal()
    elif gj == "nise install XAMPP":
        x = input("do you want install XAMPP? y/n: ")
        if x == "y":
            print("1.chrome")
            print("2.terminal")
            c = int(input("choose whats you want: "))
            if c == 1:
                done = False
                def lo():
                        for c in itertools.cycle(['|','/','-','|','/','-','|']):
                            if done:
                                break
                            sys.stdout.write('\rchecking browser XAMPP' + c)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        sys.stdout.write('\r     ')
                t = threading.Thread(target=lo)
                t.start()
                time.sleep(10)
                done = True
                os.system("start chrome https://downloadsapachefriends.global.ssl.fastly.net/8.0.12/xampp-windows-x64-8.0.12-0-VS16-installer.exe")
                print("install prosess cleaning 10 seconds")
                sleep(10)
                os.system("cls")
                terminal()
            elif c == 2:
                done = False
                def loa():
                        for c in itertools.cycle(['|','/','-','|','/','-','|']):
                            if done:
                                break
                            sys.stdout.write('\rchecking pankages' + c)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        sys.stdout.write('\r     ')
                t = threading.Thread(target=loa)
                t.start()
                time.sleep(10)
                done = True
                os.system("cd user/share && git clone https://github.com/Yeahboi12356/XAMPP && cd XAMPP && XAMPP.bat && XAMPP.exe")
                terminal()
    elif gj == "nise install xampp":
        x = input("do you want install XAMPP? y/n: ")
        if x == "y":
            print("1.chrome")
            print("2.terminal")
            c = int(input("choose whats you want: "))
            if c == 1:
                done = False
                def lo():
                        for c in itertools.cycle(['|','/','-','|','/','-','|']):
                            if done:
                                break
                            sys.stdout.write('\rchecking browser XAMPP' + c)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        sys.stdout.write('\r     ')
                t = threading.Thread(target=lo)
                t.start()
                time.sleep(10)
                done = True
                os.system("start chrome https://downloadsapachefriends.global.ssl.fastly.net/8.0.12/xampp-windows-x64-8.0.12-0-VS16-installer.exe")
                print("install prosess cleaning 10 seconds")
                sleep(10)
                os.system("cls")
                terminal()
            elif c == 2:
                done = False
                def loa():
                        for c in itertools.cycle(['|','/','-','|','/','-','|']):
                            if done:
                                break
                            sys.stdout.write('\rchecking pankages' + c)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        sys.stdout.write('\r     ')
                t = threading.Thread(target=loa)
                t.start()
                time.sleep(10)
                done = True
                os.system("cd user/share && git clone https://github.com/Yeahboi12356/XAMPP && cd XAMPP && XAMPP.bat && XAMPP.exe")
                terminal()
    elif gj == "nise install wireshark":
        r = input("are you sure want install wireshark? y/n: ")
        if r == "y":
            print("1.chrome")
            print("2.terminal")
            p = int(input("choose: "))
            if p == 1:
                done = False
                def lo():
                        for c in itertools.cycle(['|','/','-','|','/','-','|']):
                            if done:
                                break
                            sys.stdout.write('\rchecking browser wireshark' + c)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        sys.stdout.write('\r     ')
                t = threading.Thread(target=lo)
                t.start()
                time.sleep(10)
                done = True
                os.system("start chrome https://2.na.dl.wireshark.org/win64/Wireshark-win64-3.4.9.exe")
                print("install prosess cleaning 10 seconds")
                sleep(10)
                os.system("cls")
                terminal()
            elif p == 2:
                done = False
                def loa():
                        for c in itertools.cycle(['|','/','-','|','/','-','|']):
                            if done:
                                break
                            sys.stdout.write('\rchecking pankages' + c)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        sys.stdout.write('\r     ')
                t = threading.Thread(target=loa)
                t.start()
                time.sleep(10)
                done = True
                os.system("cd user/share && git clone https://github.com/Yeahboi12356/wireshark64bit.git && cd wireshark64bit && wiresharkk.bat && wireshark.exe")
                terminal()
        elif r == "n":
            terminal()
        else:
            terminal()
    elif gj == "sqlmap -h":
        try: 
            gggg = open("user/share/sqlmap/sqlmap.py")
            print ("""\n             .__                         
  ___________|  |   _____ _____  ______  
 /  ___/ ____/  |  /     \\__  \ \____ \ 
 \___ < <_|  |  |_|  Y Y  \/ __ \|  |_> >
/____  >__   |____/__|_|  (____  /   __/ 
     \/   |__|          \/     \/|__|     \n""")
            print("sqlmap -u                  starting sqlmap")
            print("sqlmap -h , --help         showing help")
            print("sqlmap -hd ,--helpd         showing default sqlmap help")
            print("\n")
            terminal()
        except:
            print("you haven't installed sqlmap")
            print("type nise install sqlmap")
            terminal()
    elif gj == "sqlmap --help":
        try: 
            gggg = open("user/share/sqlmap/sqlmap.py")
            print ("""\n             .__                         
  ___________|  |   _____ _____  ______  
 /  ___/ ____/  |  /     \\__  \ \____ \ 
 \___ < <_|  |  |_|  Y Y  \/ __ \|  |_> >
/____  >__   |____/__|_|  (____  /   __/ 
     \/   |__|          \/     \/|__|     \n""")
            print("sqlmap -u                  starting sqlmap")
            print("sqlmap -h , --help         showing help")
            print("\n")
            terminal()
        except:
            print("you haven't installed sqlmap")
            print("type nise install sqlmap")
            terminal()
    elif gj == "sqlmap -h":
        try: 
            ggggr = open("user/share/sqlmap/sqlmap.py")                   
            os.system("python user/share/sqlmap/sqlmap.py --help")
            terminal()
        except:
            print("you haven't installed sqlmap")
            print("type nise install sqlmap")
            terminal()
    elif gj == "sqlmap --help":
        try: 
            ggggr = open("user/share/sqlmap/sqlmap.py")                   
            os.system("python user/share/sqlmap/sqlmap.py --help")
            terminal()
        except:
            print("you haven't installed sqlmap")
            print("type nise install sqlmap")
            terminal()
    elif gj == "sqlmap -u":
        try:
            ggg = open("user/share/sqlmap/sqlmap.py")
            print("welcome to sqlmap modified by who!")
            y = input("are you sure want to use sqlmap y/n: ")
            if y == "y":
                h = input("website link: ")
                print("options>:")
                print ("1.dbs              DBMS database to enumerate")
                print ("2.tables           DBMS database table(s) to enumerate")
                print ("3.columns          Enumerate DBMS database table columns")
                print ("4.dump             Dump DBMS database table entries")
                print ("")
                print ("           extra                        ")
                print ("")
                print ("5.level            Level of tests to perform (1-5, default 1)")
                print ("6.another")
                w = int(input("input your chosee: "))
                if w == 1:
                    os.system("python user/share/sqlmap/sqlmap.py -u " + h + " --dbs")
                    terminal()
                elif w == 2:
                    l = input("database: ")
                    os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + l + " --tables")
                    terminal()
                elif w == 3:
                    ll = input("database: ")
                    lk = input("database tables: ")
                    os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + ll + " -T " + lk + " --columns")
                    terminal()
                elif w == 4:
                    lll = input("database: ")
                    lkk = input("database tables: ")
                    lr = input("columns: ")
                    os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + lll + " -T " + lkk + " -C " + lr + " --dump")
                    terminal()
                elif w == 5:
                    print("type the level you want")
                    lvl = input("level(1-5)> ")
                    print("another options>:")
                    print ("1.dbs              DBMS database to enumerate")
                    print ("2.tables           DBMS database table(s) to enumerate")
                    print ("3.columns          Enumerate DBMS database table columns")
                    print ("4.dump             Dump DBMS database table entries")
                    print ("")
                    e = int(input("input your chosee: "))
                    if e == 1:
                        os.system("python user/share/sqlmap/sqlmap.py -u " + h + " --dbs --level " + lvl )
                        terminal()
                    elif e == 2:
                        l = input("database: ")
                        os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + l + " --tables --level " + lvl)
                        terminal()
                    elif e == 3:
                        ll = input("database: ")
                        lk = input("database tables: ")
                        os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + ll + " -T " + lk + " --columns --level " + lvl)
                        terminal()
                    elif e == 4:
                        lll = input("database: ")
                        lkk = input("database tables: ")
                        lr = input("columns: ")
                        os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + lll + " -T " + lkk + " -C " + lr + " --dump --level " + lvl)
                        terminal()
                    else:
                        print("input not valid")
                        terminal()
                elif w == 6:
                    print("1.help")
                    print("2.another-command")
                    print("3.exit")
                    g = int(input("> "))
                    if g == 1:
                        os.system("python user/share/sqlmap/sqlmap.py --help")
                        terminal()
                    elif g == 2:
                        print("type another command in sqlmap>")
                        ano = input("sqlmap> ")
                        print("another options>:")
                        print ("1.dbs              DBMS database to enumerate")
                        print ("2.tables           DBMS database table(s) to enumerate")
                        print ("3.columns          Enumerate DBMS database table columns")
                        print ("4.dump             Dump DBMS database table entries")
                        print ("")
                        e = int(input("input your chosee: "))
                        if e == 1:
                            os.system("python user/share/sqlmap/sqlmap.py -u " + h + " --dbs " + ano)
                            terminal()
                        elif e == 2:
                            l = input("database: ")
                            os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + l + " --tables " + ano)
                            terminal()
                        elif e == 3:
                            ll = input("database: ")
                            lk = input("database tables: ")
                            os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + ll + " -T " + lk + " --columns " + ano)
                            terminal()
                        elif e == 4:
                            lll = input("database: ")
                            lkk = input("database tables: ")
                            lr = input("columns: ")
                            os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + lll + " -T " + lkk + " -C " + lr + " --dump " + ano)
                            terminal()
                    elif g == 3:
                        terminal()
                else:
                    print("number not valid")
                    terminal()
            elif y == "n":
                terminal()
            else:
                terminal()
        except: 
            print("you haven't installed sqlmap")
            print("type nise install sqlmap")
            terminal()
    elif gj == "sqlmap":
        try: 
            gggg = open("user/share/sqlmap/sqlmap.py")
            print ("""\n             .__                         
  ___________|  |   _____ _____  ______  
 /  ___/ ____/  |  /     \\__  \ \____ \ 
 \___ < <_|  |  |_|  Y Y  \/ __ \|  |_> >
/____  >__   |____/__|_|  (____  /   __/ 
     \/   |__|          \/     \/|__|     \n""")
            print("sqlmap -u                  starting sqlmap")
            print("sqlmap -h , --help         showing help")
            print("\n")
            terminal()
        except:
            print("you haven't installed sqlmap")
            print("type nise install sqlmap")
            terminal()
    elif gj == "php -r":
        v = input("input your file: ")
        os.system("php " + v ) 
        print(" ")
        terminal()
    elif gj == "wireshark":
        print("type nise install wireshark")
        terminal()
    elif gj == "nise install sherlock":
        print("requirements:")
        print("""certifi>=2019.6.16 colorama>=0.4.1
        PySocks>=1.7.0 requests>=2.22.0
        requests-futures>=1.0.0 stem>=1.8.0 
        torrequest>=0.1.0""")
        y = input("are sure want to install sherlock y/n> ")
        if y == "y":
            done = False
            def lo():
                    for c in itertools.cycle(['|','/','-','|','/','-','|']):
                        if done:
                            break
                        sys.stdout.write('\rchecking pankages' + c)
                        sys.stdout.flush()
                        time.sleep(0.1)
                        sys.stdout.write('\r     ')
            t = threading.Thread(target=lo)
            t.start()
            time.sleep(10)
            done = True
            os.system("cd user/share && git clone https://github.com/Yeahboi12356/xsherlock && cd xsherlock && pip install -r requirements.txt")
            print("installation complete")
            terminal()
        elif y == "n":
            terminal()
        else:
            terminal()
    elif gj == "sherlock":
        try:
            y = open("user/share/xsherlock/sherlock.py")
            print("""
        .__                 .__                 __    
    _____|  |__   ___________|  |   ____   ____ |  | __
    /  ___/  |  \_/ __ \_  __ \  |  /  _ \_/ ___\|  |/ /
    \___ \|   Y  \  ___/|  | \/  |_(  <_> )  \___|    < 
    /____  >___|  /\___  >__|  |____/\____/ \___  >__|_ |
        \/     \/     \/                       \/     \/
    """)
            print("sherlock -n, --name                Hunt down social media accounts by")
            print("                                   username across social networks")
            print("")
            print("sherlock -h, --help                showing help")
            terminal()
        except:
            print("you haven't installed sherlock")
            print("type nise install sherlock")
            terminal()
    elif gj == "sherlock -h":
        try:
            y = open("user/share/xsherlock/sherlock.py")
            print("""
        .__                 .__                 __    
    _____|  |__   ___________|  |   ____   ____ |  | __
    /  ___/  |  \_/ __ \_  __ \  |  /  _ \_/ ___\|  |/ /
    \___ \|   Y  \  ___/|  | \/  |_(  <_> )  \___|    < 
    /____  >___|  /\___  >__|  |____/\____/ \___  >__|_ |
        \/     \/     \/                       \/     \/
    """)
            print("sherlock -n, --name                Hunt down social media accounts by")
            print("                                   username across social networks")
            print("")
            print("sherlock -h, --help                showing help")
            terminal()
        except:
            print("you haven't installed sherlock")
            print("type nise install sherlock")
            terminal()
    elif gj == "sherlock --help":
        try:
            y = open("user/share/xsherlock/sherlock.py")
            print("""
        .__                 .__                 __    
    _____|  |__   ___________|  |   ____   ____ |  | __
    /  ___/  |  \_/ __ \_  __ \  |  /  _ \_/ ___\|  |/ /
    \___ \|   Y  \  ___/|  | \/  |_(  <_> )  \___|    < 
    /____  >___|  /\___  >__|  |____/\____/ \___  >__|_ |
        \/     \/     \/                       \/     \/
    """)
            print("sherlock -n, --name                Hunt down social media accounts by")
            print("                                   username across social networks")
            print("")
            print("sherlock -h, --help                showing help")
            terminal()
        except:
            print("you haven't installed sherlock")
            print("type nise install sherlock")
            terminal()
    elif gj == "sherlock -n":
        try:
            y = open("user/share/xsherlock/sherlock.py")
            n = input("usernames: ")
            print("""\033[1;32;40m
            .__                 .__                 __    
        _____|  |__   ___________|  |   ____   ____ |  | __
        /  ___/  |  \_/ __ \_  __ \  |  /  _ \_/ ___\|  |/ /
        \___ \|   Y  \  ___/|  | \/  |_(  <_> )  \___|    < 
        /____  >___|  /\___  >__|  |____/\____/ \___  >__|_ |
            \/     \/     \/                       \/     \/
        """)
            os.system("python user/share/xsherlock/sherlock.py " + n)
            terminal()
        except:
            print("you haven't installed sherlock")
            print("type nise install sherlock")
            terminal()
    elif gj == "sherlock --name":
        try:
            y = open("user/share/xsherlock/sherlock.py")
            n = input("usernames: ")
            print("""\033[1;32;40m
            .__                 .__                 __    
        _____|  |__   ___________|  |   ____   ____ |  | __
        /  ___/  |  \_/ __ \_  __ \  |  /  _ \_/ ___\|  |/ /
        \___ \|   Y  \  ___/|  | \/  |_(  <_> )  \___|    < 
        /____  >___|  /\___  >__|  |____/\____/ \___  >__|_ |
            \/     \/     \/                       \/     \/
        """)
            os.system("python user/share/xsherlock/sherlock.py " + n)
            terminal()
        except:
            print("you haven't installed sherlock")
            print("type nise install sherlock")
            terminal()
    elif gj == "exit":
        sys.exit
    elif gj == "exit ":
        sys.exit()
    elif gj == "":
        terminal()
    elif gj == " ":
        terminal()
    elif gj == "  ":
        terminal()
    elif gj == "   ":
        terminal()
    elif gj == "    ":
        terminal()
    elif gj == "     ":
        terminal()
    elif gj == "      ":
        terminal()
    elif gj == "       ":
        terminal()
    elif gj == "        ":
        terminal()
    elif gj == "restart":
        print ("restarting...")
        sleep(3)
        os.system("start-terminal.exe")
    elif gj == "restart ":
        os.system("start-terminal.exe")
    elif gj == "restart  ":
        print ("restarting...")
        sleep(3)
        os.system("start-terminal.exe")
    elif gj == "restart   ":
        print ("restarting...")
        sleep(3)
        os.system("start-terminal.exe")
    else:
        print(gj + " command not found")
        terminal()

def default():
    files = open("user/share/jasp/username.txt",'r')
    filesss = open("user/share/jasp/hostname.txt",'r')
    print("\033[1;34;40m┌──(" + "\033[1;31;40m" + files.readline() + "\033[1;32;40m@" + "\033[1;33;40m" + filesss.readline() + "\033[1;34;40m)────(~)")
    gj = input("\033[1;34;40m└─" + "\033[1;31;40m# \033[1;37;40m")
    if gj == "ls":    
        os.system("dir")
        default()
    elif gj == "dir":
        os.system("dir")
        default()
    elif gj == "help":
        print("nise             pankages for terminal ")
        print("ls/dir           show folder and file")
        print("version          check version terminal")
        print("list pankages    show pankages or tools")
        print("clear/cls        clearing terminal")
        print("network          showing ssid and pass wifi ever connected to wifi")
        print("ifconfig         showing network interfaces")
        print("ping             showing ping ip or website")
        print("\n")
        default()
    elif gj == "nise":
        print("update                       update pankages")
        print("upgrade                      upgrade terminal")
        print("install                      install pankages")
        print("list pankages                check pangkages")
        print("\n")
        default()
    elif gj == "nise ":
        print("update                       update pankages")
        print("upgrade                      upgrade terminal")
        print("install                      install pankages")
        print("list pankages                check pangkages")
        print("\n")
        default()
    elif gj == "nise update":
        done = False
        def loading():
                for c in itertools.cycle(['|','/','-','|','/','-','|']):
                    if done:
                        break
                    sys.stdout.write('\rchecking pankages' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\r     ')
        t = threading.Thread(target=loading)
        t.start()
        time.sleep(10)
        done = True
        print("pankages up to date")
        print("cleaning 5 seconds..")
        sleep(5)
        os.system("cls")
        default()
    elif gj == "version":
        print("version:1.2.0.1")
        print("nise pankages: 1.2.0.1")
        default()
    elif gj == "nise upgrade":
        done = False
        def loading():
                for c in itertools.cycle(['|','/','-','|','/','-','|']):
                    if done:
                        break
                    sys.stdout.write('\rchecking pankages' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\r     ')
        t = threading.Thread(target=loading)
        t.start()
        time.sleep(10)
        done = True
        os.system("python gisupgrade.py")

    elif gj == "list pankages":
        print("list pankages:>")
        print("\n")
        print("sqlmap")
        print("XAMPP/xampp")
        print("php")
        print("wireshark")
        print("camera-security")
        print("phoneinfoga")
        print("\n")
        default()
    elif gj == "nise list pankages":
        print("list pankages:>")
        print("\n")
        print("sqlmap")
        print("XAMPP/xampp")
        print("php")
        print("wireshark")
        print("camera-security")
        print("phoneinfoga")
        print("\n")
        default()
    elif gj == "cls":
        os.system("cls")
        default()
    elif gj == "clear":
        os.system("cls")
        default()
    elif gj == "python":
        os.system("python")
        default()
    elif gj == "python --help":
        print("python has modified by who for work in this terminal")
        print("python -f running file but just type python -f do not like python -f main.py dont do this!!")
        print("python --help for more information")
        default()
    elif gj == "python -f":
        y = input("input you file: ")
        os.system("python " + y)
        print(" ")
        default()
    elif gj == "python -h":
        print("python has modified by who for work in this terminal")
        print("python -f running file but just type python -f do not like python -f main.py dont do this!!")
        print("python --help for more information")
        default()
    elif gj == "nise install sqlmap":
        z = input("do you want install sqlmap? y/n: ")
        if z == "y":
            done = False
            def load():
                    for c in itertools.cycle(['|','/','-','|','/','-','|']):
                        if done:
                            break
                        sys.stdout.write('\rchecking pankages' + c)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    sys.stdout.write('\r     ')
            t = threading.Thread(target=load)
            t.start()
            time.sleep(10)
            done = True
            os.system("cd user/share && git clone https://github.com/sqlmapproject/sqlmap")
            print("pankages has been installed")
            print("if you wanna run sqlmap just type sqlmap -h or sqlmap --help if you type sqlmap command not found")
            print ("cleaning 10 seconds...")
            sleep(10)
            os.system("cls")
            default()
        elif z == "n":
            default()
        else:
            default()
    elif gj == "nise install php":
        e = input("php folder is zip file are you sure want install php? y/n")
        if e == "y":
            print("ok don't forget to follow the instructions")
            print("1.chrome")
            print("2.terminal")
            h = int(input("your choose: "))
            if h == 1:
                def so():
                        for c in itertools.cycle(['|','/','-','|','/','-','|']):
                            if done:
                                break
                            sys.stdout.write('\rchecking browser' + c)
                            sys.stdout.flush()
                            time.sleep(0.1)
                            sys.stdout.write('\r     ')
                t = threading.Thread(target=so)
                t.start()
                time.sleep(10)
                done = True
                os.system("start chrome https://windows.php.net/downloads/releases/php-8.0.12-Win32-vs16-x64.ziphttps://windows.php.net/downloads/releases/php-8.0.12-Win32-vs16-x64.zip")
                print("instructions!!!")
                print("extract zip in your file manager")
                gd = input("done? y/n: ")
                if gd == "y":
                    print("open enviroment variables")
                    dgb = input("done? y/n: ")
                    if dgb == "y":
                        print("click Enviroment Variables")
                        print("choose Path on user variables")
                        print("clik edit")
                        gv = input("done? y/n")
                        if gv == "y":
                            print("clik new and type")
                            print("C:/user/Yourname/Phpfolderyourextract")
                            print("python cant use \ to text pls after copy thats text pls change / to \ work")
                            print("clik ok and ok and ok again")
                            gb = input("done? y/n: ")
                            if gb == "y":
                                print("php finished install")
                                sleep(3)
                                print("cleaning 10 seconds...")
                                sleep(10)
                                os.system("cls")
                            elif gb == "n":
                                default()
                            else:
                                default()
                        elif gv == "n":
                            default()
                    elif dgb == "n":
                        default()
                    else:
                        default()
                elif gd == "n":
                    default()
                else:
                    default()
            elif h == 2:
                done = False
                def lo():
                        for c in itertools.cycle(['|','/','-','|','/','-','|']):
                            if done:
                                break
                            sys.stdout.write('\rchecking pankages' + c)
                            sys.stdout.flush()
                            time.sleep(0.1)
                            sys.stdout.write('\r     ')
                t = threading.Thread(target=lo)
                t.start()
                time.sleep(10)
                done = True
                os.system("cd user/share && git clone https://github.com/Yeahboi12356/Php64bit && cd Php64bit && php64.bat")
                print("instructions!!!")
                gd = input("are you reddy? y/n: ")
                if gd == "y":
                    print("open enviroment variables")
                    dgb = input("done? y/n: ")
                    if dgb == "y":
                        print("click Enviroment Variables")
                        print("choose Path on user variables")
                        print("clik edit")
                        gv = input("done? y/n: ")
                        if gv == "y":
                            os.system("cls")
                            print("clik new and type")
                            print("C:/user/yourname/Desktop-or-you-folder/terminal-linux/user/share/php/php")
                            print("python cant use \ to text pls after copy thats text pls change / to \ for working")
                            print("clik ok and ok and ok again")
                            gb = input("done? y/n: ")
                            if gb == "y":
                                print("php finished install")
                                sleep(3)
                                print("cleaning 10 seconds...")
                                sleep(10)
                                os.system("cls")
                                default()
                            elif gb == "n":
                                default()
                            else:
                                default()
                        elif gv == "n":
                            default()
                    elif dgb == "n":
                        default()
                    else:
                        default()
                elif gd == "n":
                    default()
                else:
                    default()
    elif gj == "nise install camera-security":
        print("open-cv")
        y = input("are sure want to install camera-security y/n> ")
        done = False
        def lo():
                for c in itertools.cycle(['|','/','-','|','/','-','|']):
                    if done:
                        break
                    sys.stdout.write('\rchecking pankages' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                    sys.stdout.write('\r     ')
        t = threading.Thread(target=lo)
        t.start()
        time.sleep(10)
        done = True
        os.system("cd user/share && git clone https://github.com/Yeahboi12356/camera")
        os.system("pip install opencv-python")
        print("installation complete type camera for run it")
        default()
    elif gj == "camera":
        try:
            f = open("user/share/camera/camera-security.py")
            os.system("python user/share/camera/camera-security.py")
            default()
        except:
           print("you haven't installed camera-security")
           print("type nise install camera-security")
           default()
    elif gj == "camera-security":
        try:
            oy = open("user/share/camera/camera-security.py")
            print("type camera")
            default()
        except:
            print("you haven't installed camera-security")
            print("type nise install camera-security")
            default()
    elif gj == "nise install XAMPP":
        x = input("do you want install XAMPP? y/n: ")
        if x == "y":
            print("1.chrome")
            print("2.terminal")
            c = int(input("choose whats you want: "))
            if c == 1:
                done = False
                def lo():
                        for c in itertools.cycle(['|','/','-','|','/','-','|']):
                            if done:
                                break
                            sys.stdout.write('\rchecking browser XAMPP' + c)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        sys.stdout.write('\r     ')
                t = threading.Thread(target=lo)
                t.start()
                time.sleep(10)
                done = True
                os.system("start chrome https://downloadsapachefriends.global.ssl.fastly.net/8.0.12/xampp-windows-x64-8.0.12-0-VS16-installer.exe")
                print("install prosess cleaning 10 seconds")
                sleep(10)
                os.system("cls")
                default()
            elif c == 2:
                done = False
                def loa():
                        for c in itertools.cycle(['|','/','-','|','/','-','|']):
                            if done:
                                break
                            sys.stdout.write('\rchecking pankages' + c)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        sys.stdout.write('\r     ')
                t = threading.Thread(target=loa)
                t.start()
                time.sleep(10)
                done = True
                os.system("cd user/share && git clone https://github.com/Yeahboi12356/XAMPP && cd XAMPP && XAMPP.bat && XAMPP.exe")
                default()
    elif gj == "nise install xampp":
        x = input("do you want install XAMPP? y/n: ")
        if x == "y":
            print("1.chrome")
            print("2.terminal")
            c = int(input("choose whats you want: "))
            if c == 1:
                done = False
                def lo():
                        for c in itertools.cycle(['|','/','-','|','/','-','|']):
                            if done:
                                break
                            sys.stdout.write('\rchecking browser XAMPP' + c)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        sys.stdout.write('\r     ')
                t = threading.Thread(target=lo)
                t.start()
                time.sleep(10)
                done = True
                os.system("start chrome https://downloadsapachefriends.global.ssl.fastly.net/8.0.12/xampp-windows-x64-8.0.12-0-VS16-installer.exe")
                print("install prosess cleaning 10 seconds")
                sleep(10)
                os.system("cls")
                default()
            elif c == 2:
                done = False
                def loa():
                        for c in itertools.cycle(['|','/','-','|','/','-','|']):
                            if done:
                                break
                            sys.stdout.write('\rchecking pankages' + c)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        sys.stdout.write('\r     ')
                t = threading.Thread(target=loa)
                t.start()
                time.sleep(10)
                done = True
                os.system("cd user/share && git clone https://github.com/Yeahboi12356/XAMPP && cd XAMPP && XAMPP.bat && XAMPP.exe")
                default()
    elif gj == "nise install wireshark":
        r = input("are you sure want install wireshark? y/n: ")
        if r == "y":
            print("1.chrome")
            print("2.terminal")
            p = int(input("choose: "))
            if p == 1:
                done = False
                def lo():
                        for c in itertools.cycle(['|','/','-','|','/','-','|']):
                            if done:
                                break
                            sys.stdout.write('\rchecking browser wireshark' + c)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        sys.stdout.write('\r     ')
                t = threading.Thread(target=lo)
                t.start()
                time.sleep(10)
                done = True
                os.system("start chrome https://2.na.dl.wireshark.org/win64/Wireshark-win64-3.4.9.exe")
                print("install prosess cleaning 10 seconds")
                sleep(10)
                os.system("cls")
                default()
            elif p == 2:
                done = False
                def loa():
                        for c in itertools.cycle(['|','/','-','|','/','-','|']):
                            if done:
                                break
                            sys.stdout.write('\rchecking pankages' + c)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        sys.stdout.write('\r     ')
                t = threading.Thread(target=loa)
                t.start()
                time.sleep(10)
                done = True
                os.system("cd user/share && git clone https://github.com/Yeahboi12356/wireshark64bit.git && cd wireshark64bit && wiresharkk.bat && wireshark.exe")
                default()
        elif r == "n":
            default()
        else:
            default()
    elif gj == "sqlmap -h":
        try: 
            gggg = open("user/share/sqlmap/sqlmap.py")
            print ("""\n             .__                         
  ___________|  |   _____ _____  ______  
 /  ___/ ____/  |  /     \\__  \ \____ \ 
 \___ < <_|  |  |_|  Y Y  \/ __ \|  |_> >
/____  >__   |____/__|_|  (____  /   __/ 
     \/   |__|          \/     \/|__|     \n""")
            print("sqlmap -u                  starting sqlmap")
            print("sqlmap -h , --help         showing help")
            print("\n")
            default()
        except:
            print("you haven't installed sqlmap")
            print("type nise install sqlmap")
            default()
    elif gj == "sqlmap --help":
        try: 
            gggg = open("user/share/sqlmap/sqlmap.py")
            print ("""\n             .__                         
  ___________|  |   _____ _____  ______  
 /  ___/ ____/  |  /     \\__  \ \____ \ 
 \___ < <_|  |  |_|  Y Y  \/ __ \|  |_> >
/____  >__   |____/__|_|  (____  /   __/ 
     \/   |__|          \/     \/|__|     \n""")
            print("sqlmap -u                  starting sqlmap")
            print("sqlmap -h , --help         showing help")
            print("\n")
            default()
        except:
            print("you haven't installed sqlmap")
            print("type nise install sqlmap")
            default()
    elif gj == "sqlmap -u":
        try:
            ggg = open("user/share/sqlmap/sqlmap.py")
            print("welcome to sqlmap modified by who!")
            y = input("are you sure want to use sqlmap y/n: ")
            if y == "y":
                h = input("website link: ")
                print("options>:")
                print ("1.dbs              DBMS database to enumerate")
                print ("2.tables           DBMS database table(s) to enumerate")
                print ("3.columns          Enumerate DBMS database table columns")
                print ("4.dump             Dump DBMS database table entries")
                print ("")
                print ("           extra                        ")
                print ("")
                print ("5.level            Level of tests to perform (1-5, default 1)")
                print ("6.another")
                w = int(input("input your chosee: "))
                if w == 1:
                    os.system("python user/share/sqlmap/sqlmap.py -u " + h + " --dbs")
                    default()
                elif w == 2:
                    l = input("database: ")
                    os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + l + " --tables")
                    default()
                elif w == 3:
                    ll = input("database: ")
                    lk = input("database tables: ")
                    os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + ll + " -T " + lk + " --columns")
                    default()
                elif w == 4:
                    lll = input("database: ")
                    lkk = input("database tables: ")
                    lr = input("columns: ")
                    os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + lll + " -T " + lkk + " -C " + lr + " --dump")
                    default()
                elif w == 5:
                    print("type the level you want")
                    lvl = input("level(1-5)> ")
                    print("another options>:")
                    print ("1.dbs              DBMS database to enumerate")
                    print ("2.tables           DBMS database table(s) to enumerate")
                    print ("3.columns          Enumerate DBMS database table columns")
                    print ("4.dump             Dump DBMS database table entries")
                    print ("")
                    e = int(input("input your chosee: "))
                    if e == 1:
                        os.system("python user/share/sqlmap/sqlmap.py -u " + h + " --dbs --level " + lvl )
                        default()
                    elif e == 2:
                        l = input("database: ")
                        os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + l + " --tables --level " + lvl)
                        default()
                    elif e == 3:
                        ll = input("database: ")
                        lk = input("database tables: ")
                        os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + ll + " -T " + lk + " --columns --level " + lvl)
                        default()
                    elif e == 4:
                        lll = input("database: ")
                        lkk = input("database tables: ")
                        lr = input("columns: ")
                        os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + lll + " -T " + lkk + " -C " + lr + " --dump --level " + lvl)
                        default()
                    else:
                        print("input not valid")
                        default()
                elif w == 6:
                    print("1.help")
                    print("2.another-command")
                    print("3.exit")
                    g = int(input("> "))
                    if g == 1:
                        os.system("python user/share/sqlmap/sqlmap.py --help")
                        default()
                    elif g == 2:
                        print("type another command in sqlmap>")
                        ano = input("sqlmap> ")
                        print("another options>:")
                        print ("1.dbs              DBMS database to enumerate")
                        print ("2.tables           DBMS database table(s) to enumerate")
                        print ("3.columns          Enumerate DBMS database table columns")
                        print ("4.dump             Dump DBMS database table entries")
                        print ("")
                        e = int(input("input your chosee: "))
                        if e == 1:
                            os.system("python user/share/sqlmap/sqlmap.py -u " + h + " --dbs " + ano)
                            default()
                        elif e == 2:
                            l = input("database: ")
                            os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + l + " --tables " + ano)
                            default()
                        elif e == 3:
                            ll = input("database: ")
                            lk = input("database tables: ")
                            os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + ll + " -T " + lk + " --columns " + ano)
                            default()
                        elif e == 4:
                            lll = input("database: ")
                            lkk = input("database tables: ")
                            lr = input("columns: ")
                            os.system("python user/share/sqlmap/sqlmap.py -u " + h + " -D " + lll + " -T " + lkk + " -C " + lr + " --dump " + ano)
                            default()
                    elif g == 3:
                        default()
                else:
                    print("number not valid")
                    default()
            elif y == "n":
                default()
            else:
                default()
        except: 
            print("you haven't installed sqlmap")
            print("type nise install sqlmap")
            default()
    elif gj == "sqlmap":
        try: 
            gggg = open("user/share/sqlmap/sqlmap.py")
            print ("""\n             .__                         
  ___________|  |   _____ _____  ______  
 /  ___/ ____/  |  /     \\__  \ \____ \ 
 \___ < <_|  |  |_|  Y Y  \/ __ \|  |_> >
/____  >__   |____/__|_|  (____  /   __/ 
     \/   |__|          \/     \/|__|     \n""")
            print("sqlmap -u                  starting sqlmap")
            print("sqlmap -h , --help         showing help")
            print("\n")
            default()
        except:
            print("you haven't installed sqlmap")
            print("type nise install sqlmap")
            default()
    elif gj == "nise install phoneinfoga":
        print("requirements:")
        print("""requests==2.21.0 bs4==0.0.1 
        html5lib==1.0.1 phonenumbers==8.10.2
        argparse==1.2.1 urllib3==1.24.2
        colorama==0.4.1""")
        e = input("do you want install phoneinfoga? y/n: ")
        if e == "y":
            done = False
            def load():
                    for c in itertools.cycle(['|','/','-','|','/','-','|']):
                        if done:
                            break
                        sys.stdout.write('\rchecking pankages' + c)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    sys.stdout.write('\r     ')
            t = threading.Thread(target=load)
            t.start()
            time.sleep(10)
            done = True
            os.system("cd user/share && git clone https://github.com/Yeahboi12356/phoneinfoga && cd phoneinfoga && pip install -r requirements.txt")
            print("pankages has been installed")
            print("if you wanna run phoneinfoga just type phoneinfoga -h or phoneinfoga --help")
            print ("cleaning 10 seconds...")
            sleep(10)
            os.system("cls")
            default()
        elif e == "n":
            default()
        else:
            default()
    elif gj == "phoneinfoga -h":
        try:
            r = open("user/share/phoneinfoga/phoneinfoga.py", "r")
            print("    ___ _                       _____        __                   ")
            print("   / _ \ |__   ___  _ __   ___  \_   \_ __  / _| ___   __ _  __ _ ")
            print("  / /_)/ '_ \ / _ \| '_ \ / _ \  / /\/ '_ \| |_ / _ \ / _` |/ _` |")
            print(" / ___/| | | | (_) | | | |  __/\/ /_ | | | |  _| (_) | (_| | (_| |")
            print(" \/    |_| |_|\___/|_| |_|\___\____/ |_| |_|_|  \___/ \__, |\__,_|")
            print("                                                      |___/       ")
            print(" Coded by Sundowndev")
            print(" Modified by Who ")
            print("\n")
            print("phoneinfoga -n , --number    scanning number but just type phoneinfoga -n to run it")
            print("phoneinfoga -h , --help      showing help")
            print("\n")
            default()
        except:
            print("you haven't installed phoneinfoga")
            print("type nise install phoneinfoga")
            default()
    elif gj == "phoneinfoga --help":
        try:
            ri = open("user/share/phoneinfoga/phoneinfoga.py", "r")
            print("    ___ _                       _____        __                   ")
            print("   / _ \ |__   ___  _ __   ___  \_   \_ __  / _| ___   __ _  __ _ ")
            print("  / /_)/ '_ \ / _ \| '_ \ / _ \  / /\/ '_ \| |_ / _ \ / _` |/ _` |")
            print(" / ___/| | | | (_) | | | |  __/\/ /_ | | | |  _| (_) | (_| | (_| |")
            print(" \/    |_| |_|\___/|_| |_|\___\____/ |_| |_|_|  \___/ \__, |\__,_|")
            print("                                                      |___/       ")
            print(" Coded by Sundowndev")
            print(" Modified by Who ")
            print("\n")
            print("phoneinfoga -n , --number    scanning number but just type phoneinfoga -n to run it")
            print("phoneinfoga -h , --help      showing help")
            print("\n")
            default()
        except:
            print("you haven't installed phoneinfoga")
            print("type nise install phoneinfoga")
            default()
    elif gj == "phoneinfoga":
        try:
            fil = open("user/share/phoneinfoga/phoneinfoga.py", "r")
            print("    ___ _                       _____        __                   ")
            print("   / _ \ |__   ___  _ __   ___  \_   \_ __  / _| ___   __ _  __ _ ")
            print("  / /_)/ '_ \ / _ \| '_ \ / _ \  / /\/ '_ \| |_ / _ \ / _` |/ _` |")
            print(" / ___/| | | | (_) | | | |  __/\/ /_ | | | |  _| (_) | (_| | (_| |")
            print(" \/    |_| |_|\___/|_| |_|\___\____/ |_| |_|_|  \___/ \__, |\__,_|")
            print("                                                      |___/       ")
            print(" Coded by Sundowndev")
            print(" Modified by Who ")
            print("\n")
            print("phoneinfoga -n , --number    scanning number but just type phoneinfoga -n to run it")
            print("phoneinfoga -h , --help      showing help")
            print("\n")
            default()
        except:
            print("you haven't installed phoneinfoga")
            print("type nise install phoneinfoga")
            default()
    elif gj == "phoneinfoga -n":
        try:
            fi = open("user/share/phoneinfoga/phoneinfoga.py", "r")
            print("    ___ _                       _____        __                   ")
            print("   / _ \ |__   ___  _ __   ___  \_   \_ __  / _| ___   __ _  __ _ ")
            print("  / /_)/ '_ \ / _ \| '_ \ / _ \  / /\/ '_ \| |_ / _ \ / _` |/ _` |")
            print(" / ___/| | | | (_) | | | |  __/\/ /_ | | | |  _| (_) | (_| | (_| |")
            print(" \/    |_| |_|\___/|_| |_|\___\____/ |_| |_|_|  \___/ \__, |\__,_|")
            print("                                                      |___/       ")
            print(" Coded by Sundowndev")
            print(" Modified by Who ")
            print("\n")
            print("use + exemple: +86")
            e =  input("number: ")
            y = os.system("python user/share/phoneinfoga/phoneinfoga.py -n " + e)
            default()
        except:
            print("you haven't installed phoneinfoga")
            print("type nise install phoneinfoga")
            default()
    elif gj == "phoneinfoga --number":
        try:
            fi = open("user/share/phoneinfoga/phoneinfoga.py", "r")
            print("    ___ _                       _____        __                   ")
            print("   / _ \ |__   ___  _ __   ___  \_   \_ __  / _| ___   __ _  __ _ ")
            print("  / /_)/ '_ \ / _ \| '_ \ / _ \  / /\/ '_ \| |_ / _ \ / _` |/ _` |")
            print(" / ___/| | | | (_) | | | |  __/\/ /_ | | | |  _| (_) | (_| | (_| |")
            print(" \/    |_| |_|\___/|_| |_|\___\____/ |_| |_|_|  \___/ \__, |\__,_|")
            print("                                                      |___/       ")
            print(" Coded by Sundowndev")
            print(" Modified by Who ")
            print("\n")
            print("use + exemple: +86")
            e =  input("number: ")
            y = os.system("python user/share/phoneinfoga/phoneinfoga.py -n " + e)
            default()
        except:
            print("you haven't installed phoneinfoga")
            print("type nise install phoneinfoga")
            default()
    elif gj == "php -r":
        v = input("input your file: ")
        os.system("php " + v ) 
        print(" ")
        default()
    elif gj == "wireshark":
        print("type nise install wireshark")
        default()
    elif gj == "network":
        print("network --help                       show help")
        print("net                                  show help")
        print()
        print("network history:")
        print("network show wifi history            show history wifi ever used")
        print()
        print("informations network:")
        print("network ssid                         show informations network")
        print()
        print("password key:")
        print("network wifi key                     show wifi key")
        default()
    elif gj == "network ---help":
        print("network --help                       show help")
        print("net                                  show help")
        print()
        print("network history:")
        print("network show wifi history            show history wifi ever used")
        print()
        print("informations network:")
        print("network ssid                         show informations network")
        print()
        print("password key:")
        print("network wifi key                     show wifi key")
        default()
    elif gj == "net":
        print("network --help                       show help")
        print("net                                  show help")
        print()
        print("network history:")
        print("network show wifi history            show history wifi ever used")
        print()
        print("informations network:")
        print("network ssid                         show informations network")
        print()
        print("password key:")
        print("network wifi key                     show wifi key")
        default()
    elif gj == "network show wifi history":
        os.system("netsh wlan show profiles")
        default()
    elif gj == "network show wifi history ":
        os.system("netsh wlan show profiles")
        default()
    elif gj == "network ssid":
        yourdad = input("name ssid wifi:> ")
        os.system("netsh wlan show profiles " + yourdad)
        yourmom = input ("do you want to see the password?y/n:> ")
        if yourmom == "y":
            os.system("netsh wlan show profiles " + yourdad + " key=clear")
            print("password in Key Content")
            default()
        elif yourmom == "n":
            default()
        else:
            default()
    elif gj == "network wifi key":
        yourdad = input("name ssid wifi:> ")
        os.system("netsh wlan show profiles " + yourdad + " key=clear")
        print("password in Key Content")
        default()
    elif gj == "change hostname":
        changehost()
    elif gj == "nise install sherlock":
        print("requirements:")
        print("""certifi>=2019.6.16 colorama>=0.4.1
        PySocks>=1.7.0 requests>=2.22.0
        requests-futures>=1.0.0 stem>=1.8.0 
        torrequest>=0.1.0""")
        y = input("are sure want to install sherlock y/n> ")
        if y == "y":
            done = False
            def lo():
                    for c in itertools.cycle(['|','/','-','|','/','-','|']):
                        if done:
                            break
                        sys.stdout.write('\rchecking pankages' + c)
                        sys.stdout.flush()
                        time.sleep(0.1)
                        sys.stdout.write('\r     ')
            t = threading.Thread(target=lo)
            t.start()
            time.sleep(10)
            done = True
            os.system("cd user/share && git clone https://github.com/Yeahboi12356/xsherlock && cd xsherlock && pip install -r requirements.txt")
            print("installation complete")
            terminal()
        elif y == "n":
            terminal()
        else:
            terminal()
    elif gj == "sherlock":
        try:
            y = open("user/share/xsherlock/sherlock.py")
            print("""
        .__                 .__                 __    
    _____|  |__   ___________|  |   ____   ____ |  | __
    /  ___/  |  \_/ __ \_  __ \  |  /  _ \_/ ___\|  |/ /
    \___ \|   Y  \  ___/|  | \/  |_(  <_> )  \___|    < 
    /____  >___|  /\___  >__|  |____/\____/ \___  >__|_ |
        \/     \/     \/                       \/     \/
    """)
            print("sherlock -n, --name                Hunt down social media accounts by")
            print("                                   username across social networks")
            print("")
            print("sherlock -h, --help                showing help")
            terminal()
        except:
            print("you haven't installed sherlock")
            print("type nise install sherlock")
            terminal()
    elif gj == "sherlock -h":
        try:
            y = open("user/share/xsherlock/sherlock.py")
            print("""
        .__                 .__                 __    
    _____|  |__   ___________|  |   ____   ____ |  | __
    /  ___/  |  \_/ __ \_  __ \  |  /  _ \_/ ___\|  |/ /
    \___ \|   Y  \  ___/|  | \/  |_(  <_> )  \___|    < 
    /____  >___|  /\___  >__|  |____/\____/ \___  >__|_ |
        \/     \/     \/                       \/     \/
    """)
            print("sherlock -n, --name                Hunt down social media accounts by")
            print("                                   username across social networks")
            print("")
            print("sherlock -h, --help                showing help")
            terminal()
        except:
            print("you haven't installed sherlock")
            print("type nise install sherlock")
            terminal()
    elif gj == "sherlock --help":
        try:
            y = open("user/share/xsherlock/sherlock.py")
            print("""
        .__                 .__                 __    
    _____|  |__   ___________|  |   ____   ____ |  | __
    /  ___/  |  \_/ __ \_  __ \  |  /  _ \_/ ___\|  |/ /
    \___ \|   Y  \  ___/|  | \/  |_(  <_> )  \___|    < 
    /____  >___|  /\___  >__|  |____/\____/ \___  >__|_ |
        \/     \/     \/                       \/     \/
    """)
            print("sherlock -n, --name                Hunt down social media accounts by")
            print("                                   username across social networks")
            print("")
            print("sherlock -h, --help                showing help")
            terminal()
        except:
            print("you haven't installed sherlock")
            print("type nise install sherlock")
            terminal()
    elif gj == "sherlock -n":
        try:
            y = open("user/share/xsherlock/sherlock.py")
            n = input("usernames: ")
            print("""\033[1;32;40m
            .__                 .__                 __    
        _____|  |__   ___________|  |   ____   ____ |  | __
        /  ___/  |  \_/ __ \_  __ \  |  /  _ \_/ ___\|  |/ /
        \___ \|   Y  \  ___/|  | \/  |_(  <_> )  \___|    < 
        /____  >___|  /\___  >__|  |____/\____/ \___  >__|_ |
            \/     \/     \/                       \/     \/
        """)
            os.system("python user/share/xsherlock/sherlock.py " + n)
            terminal()
        except:
            print("you haven't installed sherlock")
            print("type nise install sherlock")
            terminal()
    elif gj == "sherlock --name":
        try:
            y = open("user/share/xsherlock/sherlock.py")
            n = input("usernames: ")
            print("""\033[1;32;40m
            .__                 .__                 __    
        _____|  |__   ___________|  |   ____   ____ |  | __
        /  ___/  |  \_/ __ \_  __ \  |  /  _ \_/ ___\|  |/ /
        \___ \|   Y  \  ___/|  | \/  |_(  <_> )  \___|    < 
        /____  >___|  /\___  >__|  |____/\____/ \___  >__|_ |
            \/     \/     \/                       \/     \/
        """)
            os.system("python user/share/xsherlock/sherlock.py " + n)
            terminal()
        except:
            print("you haven't installed sherlock")
            print("type nise install sherlock")
            terminal()
    elif gj == "exit":
        sys.exit()
    elif gj == "exit ":
        sys.exit()
    elif gj == "":
        default()
    elif gj == " ":
        default()
    elif gj == "  ":
        default()
    elif gj == "   ":
        default()
    elif gj == "    ":
        default()
    elif gj == "     ":
        default()
    elif gj == "      ":
        default()
    elif gj == "       ":
        default()
    elif gj == "        ":
        default()
    elif gj == "restart":
        print ("restarting...")
        sleep(3)
        os.system("start-terminal.exe")
    elif gj == "ping":
        p = input("input> ")
        os.system("ping " + p)
        default()
    elif gj == "restart ":
        print ("restarting...")
        sleep(3)
        os.system("start-terminal.exe")
    elif gj == "restart  ":
        print ("restarting...")
        sleep(3)
        os.system("start-terminal.exe")
    elif gj == "restart   ":
        print ("restarting...")
        sleep(3)
        os.system("start-terminal.exe")
    elif gj ==  "ifconfig":
        os.system("ipconfig")
        default()
    elif gj == "rm":
        os.system("rm -rf user/share/jasp/password.txt")
        default()
    elif gj == "finduserwifi":
        try:
            ri = open("user/share/liduserwifi/finduserwifi/map-7.92/tes.py")
            os.system("cd user/share/liduserwifi/finduserwifi/map-7.92 && python tes.py")
            terminal()
        except:
            print("you haven't installed finduserwifi")
            print("type nise install finduserwifi")
            terminal()
    elif gj == "nise install finduserwifi":
        print("pankages and app need to install:")
        print("terminaltables nmap npcap")
        r = input('are you sure want to install? y/n: ')
        if r == "y":
            os.system("pip install terminaltables && cd user/share && git clone https://github.com/Yeahboi12356/liduserwifi && cd liduserwifi && finduserwifi.bat")
            terminal()     
        elif r == "n":
            terminal()
        else:
            terminal()
    else:
        print(gj + " command not found")
        default()
        
def signal_handler(signal, frame):
    print('\nyou clik ctrl + c if you want exit type exit\n')
    print("error hostname back to the default")
    default()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    utama()

login()