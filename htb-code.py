#!/usr/bin/python
# -*- coding: utf-8 -*-


import base64
import requests
import os, sys

# Lets give a hand to the python2'ers
try: input = raw_input
except: pass

_version_ = 0.1

# Give some beauty colors
RED = '\033[1;31m'
BLUE = '\033[94m'
BOLD = '\033[1m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
END = '\033[0m'

def git_https_force():
	subprocess.Popen('git config --global url."https://github.com/".insteadOf git@github.com:;git config --global url."https://".insteadOf git://', shell=True).wait()

def self_update():
	# force https
	git_https_force()

	# try to update ourself first
	print("Trying to update myself first.. Then starting framework.")
	subprocess.Popen("git pull", shell=True).wait()

def check_internet():
	"""
	Check for internet access.
	"""
	try:
		print(YELLOW + "[i] Checking for an Internet connection..."+ END)
		rhost = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		rhost.connect(('google.com', 0))
		rhost.settimeout(2)
		return 1

	except Exception:
		return 0

def help_menu():
	print("Some commands:")
	print("-h  or  --help\t Displays this help menu")
	print("--"*20)
	print("Usage: python %s <number>" % sys.argv[0])
	print("The number is how many codes you want to generate")

# Who doesn't use a banner?
def banner():
	banner = RED + """                                                                                                                                                                                                     
	██╗  ██╗ █████╗  ██████╗██╗  ██╗████████╗██╗  ██╗███████╗██████╗  ██████╗ ██╗  ██╗
	██║  ██║██╔══██╗██╔════╝██║ ██╔╝╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╔═══██╗╚██╗██╔╝
	███████║███████║██║     █████╔╝    ██║   ███████║█████╗  ██████╔╝██║   ██║ ╚███╔╝ 
	██╔══██║██╔══██║██║     ██╔═██╗    ██║   ██╔══██║██╔══╝  ██╔══██╗██║   ██║ ██╔██╗ 
	██║  ██║██║  ██║╚██████╗██║  ██╗   ██║   ██║  ██║███████╗██████╔╝╚██████╔╝██╔╝ ██╗
	╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝
	██╗███╗   ██╗██╗   ██╗██╗████████╗███████╗                        
	██║████╗  ██║██║   ██║██║╚══██╔══╝██╔════╝                        
	██║██╔██╗ ██║██║   ██║██║   ██║   █████╗                          
	██║██║╚██╗██║╚██╗ ██╔╝██║   ██║   ██╔══╝                          
	██║██║ ╚████║ ╚████╔╝ ██║   ██║   ███████╗                        
	╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝   ╚═╝   ╚══════╝   
	"""
	banner += RED + """[+] Version: """ + END + YELLOW + str(_version_) + "\n"+ END
	banner += GREEN + "\t[+] hackthebox.eu Invite Code Generator\n" + END
	banner += GREEN + "\t[+] Author: AgentWhite (@_agentwhite_)\n" + END
	banner += GREEN + "\t[+] Website: https://thegibson.xyz\n" + END
	banner += YELLOW +"\t[+] World Designed By Technology Is A World Designed To Be Broken.\n" + END
	banner += RED + "\t-----------------------------------------------------------------------------\n" + END
	banner += BOLD + BLUE + """
	This was meant to help generate an invite code for HTB (hackthebox.eu)
	This is kind of cheating since getting the invite code will be the 'first'
	hack you will do on the platform but also on the actual HTB.
	So I encourage you to not use this script but rather do it yourself""" + END	

	return banner

print(banner())

# Ummmm... Still need explanation what this function does?
def get_code(num):
	for i in range(int(num)):
		os.system("bash test.sh")
		print("\n")
	sys.exit()


if __name__ == "__main__":
	if "--no-network-connection" not in sys.argv:
		# check internet connection
		if check_internet() != 0:
			print(RED + "Unable to detect Internet connection. Needed for HTB Invite Code Generator.")
			print("We will now exit. Launch again when you got a connection.")
			print("You can also run ptf with the --no-network-connection argument to bypass the network check." + END)
			sys.exit()
		else:
			print(GREEN + "[i] Found an internet connection..." + END)
	else:
		# Grab latest update if any
		#self_update()
		try:
			if '-h' in sys.argv or '--help' in sys.argv:
				print(help_menu())
				sys.exit()
			get_code(sys.argv[1])
		except IndexError:
			print(help_menu())
			sys.exit()