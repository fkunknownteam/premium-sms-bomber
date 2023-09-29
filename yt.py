# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-05-22 23:34:12.924217
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")


import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit(' [У] Cant Install Rich Module, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64

def clear():
	os.system('clear')
def back():
	login()

ah="PREMIUM"
imt="-M4786=="
ak=" FK-"
myid=uuid.uuid4().hex[:10].upper()

logo = ("""\033[1;32m 
 \033[1;32m█████╗ ██╗     ██╗██╗   ██╗ █████╗ ███╗   ██╗
\033[1;33m██╔══██╗██║     ██║╚██╗ ██╔╝██╔══██╗████╗  ██║
\033[1;32m███████║██║     ██║ ╚████╔╝ ███████║██╔██╗ ██║
\033[1;33m██╔══██║██║     ██║  ╚██╔╝  ██╔══██║██║╚██╗██║
\033[1;32m██║  ██║███████╗██║   ██║   ██║  ██║██║ ╚████║
\033[1;33m╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝
                                              
\033[1;32m it can only be 
\033[;33m access  by premium users 🥰
        
••••••••••••••••••••••••••••••••••••••••••••••••••\033[1;33m
  \033[1;32mAuther      : Golu Molu
  \033[1;33mTelegram    : fkunknownteam
  \033[1;32mFacebook    : Fk Unknown Team
   \033[1;33mTools      :  Premium SMS bomber
••••••••••••••••••••••••••••••••••••••••••••••••••\033[1;32m""")

 
class Main:
	def __init__(self):
		self.loop = 0
		os.system("clear")
		print(logo)
		print("")
		print("\033[1;36m     Because of unsubscribe, Balong Ka is the best place to fly")
		print("")
		print("\033[1;32m [1] First Premium Sms Bomber ")
		print("\033[1;33m [2] Exit")
		print("")
		GOLU = input("\n\033[1;36m  Chose ==> \033[1;32m")
		if GOLU in ["", " "]:
			exit()
		elif GOLU in ["2", "02"]:
			print("    Thanks№ЅАтЅяИ")
			exit()
		elif GOLU in ["1", "01"]:
			os.system("test.py")
		

def Subscraption():
	key1=open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
	clear()
	print(logo)
	r1=requests.get("https://github.com/fkunknownteam/premium-sms-bomber/blob/main/premium-list.txt").text
	if key1 in r1:
		os.system('clear')
		print(logo)
		Main()
	else:
		os.system("clear")
		print(logo)
		print("\t \033[1;32m First Get Approvel\033[1;37m ")
		time.sleep(1)
		os.system("clear")
		print(logo)
		print ("")
		print(" \033[1;32m GOLU Toll Free BUT You Need Get Approved First\033[1;37m\n")
		print(" \033[1;32m Note : GOLU FREE HA BHAIYO ENJOYA   \033[1;37m")
		print ("")
		print(" Your Key is Not Approved ")
		print("")
		print(" Copy And Send Key To Admin")
		print ("")
		print (" Your Key : "+ak+ah+key1 )
		print ("")
		name = input(" Your Name : ")
		print ("")
		gf = input(" Your gf Name : ")
		print ("")
		lol = input(" Your Your Email : ")
		print ("")
		input(" Press Enter To Send Key")
		time.sleep(3.5)
		tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Email%20:%20'+lol+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+ak+ah+key1
		os.system('am start https://wa.me/+923344706269?text=' + tks)
		Subscraption()        
Subscraption()
