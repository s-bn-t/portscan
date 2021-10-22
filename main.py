import sys 
import socket 
from datetime import datetime
from colorama import Fore, Back, Style


def banner():

    r = Fore.RED
    g = Fore.GREEN

    print(f"""
                         
        {r}     _____ ______ _   _ _____ _       _____ _____   ___   _   _ 
        {g}    /  __ \| ___ \ | | |  ___| |     /  ___/  __ \ / _ \ | \ | |
        {r}    | /  \/| |_/ / | | | |__ | |     \ `--.| /  \// /_\ \|  \| |
        {g}    | |    |    /| | | |  __|| |      `--. \ |    |  _  || . ` |
        {r}    | \__/\| |\ \| |_| | |___| |____ /\__/ / \__/\| | | || |\  |
        {g}    \____/\_| \_|\___/\____/\_____/ \____/ \____/\_| |_/\_| \_/
                                                                         
                                                                   
    
    
    
    """)


banner()


if len(sys.argv) == 2:
    if sys.argv[0] == 1:
        print("Supply a target: ")
    target = socket.gethostbyname(sys.argv[1])  
    print("-" * 50) 
    print("Scanning Target: " + target) 
    print("Scanning started at:" + str(datetime.now())) 
    print("-" * 50)

try:
    for port in range(1,1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        socket.setdefaulttimeout(1) 
          
        result = s.connect_ex((target,port))
        if result ==0: 
            print("Port {} is open".format(port)) 
        s.close()

except KeyboardInterrupt:
        print("\n Exitting Program")
        sys.exit()
except socket.gaierror: 
        print("\n Hostname Could Not Be Resolved !!!!") 
        sys.exit() 
except socket.error: 
        print("\ Server not responding !!!!") 
        sys.exit()
