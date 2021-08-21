import time
import os

blue()
print("1 -->> Arch")
print("2 -->> Debian")
print("")
red()
x = input("-->> ")

if x == "1":
    yellow()
    print("Downloading...")
    os.system("sudo pacman -S git bash wpscan php dnsmasq hostap --noconfirm")
    time.sleep(1)
    red()
    print("Done!!")
    time.sleep(2)
    exit()

if x == "2":
    yellow()
    print("Downloading...")
    os.system("sudo apt install git bash wpscan php dnsmasq hostapd -y")
    try:
        os.system("sudo apt install git bash wpscan php dnsmasq hostapd -y /home/kali/VP-tool")
    while True:
            time.sleep(1)
            print("Done!")
            time.sleep(2)
            exit()
  
