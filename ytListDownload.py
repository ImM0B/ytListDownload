#!/usr/bin/env python3

import psutil,colorama,signal,os,time,sys
from colorama import Fore, Style, init
init()

def sig_handler(sig, frame):
    print(Fore.RED + "\n\n[!] Saliendo...\n")
    sys.exit(0)

signal.signal(signal.SIGINT, sig_handler)

def isConnected():
	interfaces = psutil.net_if_addrs()
	with open('IPs.txt', 'r') as wifiList:
		for line in wifiList:
			wifi = line.strip()
			for interface,ips in interfaces.items():
				for ip in ips:
					if wifi == ip.address :
						return True
	return False

def downloadVideos():
	with open('links.txt','r') as file :
		url = file.readline().strip()
		otherUrls= file.readlines()
	if url:
		os.system(f"python3 youtube-dl.py -f 'best[height<=480]/best[ext=mp4]/best' -o '/your/directory/%(title)s-%(id)s.%(ext)s' --no-warnings {url}")
		with open('links.txt','w') as file :
			file.writelines(otherUrls)

if __name__ == "__main__":
	while True :
		print(f"\n{Fore.GREEN}[!] Comprobando conexión ...{Style.RESET_ALL}")
		time.sleep(1)
		if isConnected() :
			time.sleep(1)
			os.system('clear')
			print(f"\n{Fore.GREEN}[+] Conectado {Style.RESET_ALL}\n")
			downloadVideos()
			os.system('clear')
			print(Fore.GREEN + "\n[⋆] Todos los videos descargados con éxito" + Style.RESET_ALL)
			time.sleep(1)
			sig_handler(None,None)
		else:
			time.sleep(1)
			os.system('clear')
			print(Fore.YELLOW + "\n[+] Esperando para comprobar de nuevo ..." + Style.RESET_ALL)
			time.sleep(300)


























