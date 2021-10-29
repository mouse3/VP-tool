import os
import time
def RunDebian():
  os.system("sudo apt-get update")
  os.system("sudo apt-get upgrade")
  os.system("sudo apt-get update")
  os.system("sudo apt-get install nmap")
  os.system("sudo apt-get install hostapd")
  while True:
    exit
print("1--Run (on debian)")
print("2--exit")
x = input("__--->")
if x == "1":
  RunDebian()
if x == "2":
  exit
