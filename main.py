import os 
from pystyle import * 
import time 
import sys 
import psutil

RED = '\033[1;91m'
WHITE = '\033[0m'
GREEN = '\033[1;32m'
GRAY = '\033[1;90m'
GOLD = '\033[0;33m'
BLUE = '\033[1;34m'

def portM():
    prev_connections = set()
    
    while True:
        current_connections = set()
        for conn in psutil.net_connections(kind='inet'):
            if conn.laddr and conn.pid:
                current_connections.add((conn.pid, conn.laddr.port))
        
        opened = current_connections - prev_connections
        closed = prev_connections - current_connections
        
        for pid, port in opened:
            try:
                process = psutil.Process(pid)
                print(f"{GRAY}[{GOLD}INFO{GRAY}] {WHITE}- Opened: {port} by {process.name()} (PID {pid})")
            except psutil.NoSuchProcess:
                pass
        
        for pid, port in closed:
            print(f"{GRAY}[{GOLD}INFO{GRAY}] {WHITE}- Closed: {port} by PID {pid}")
        
        prev_connections = current_connections


os.system("cls")
os.system("title ")
art = """
  /$$$$$$                        /$$                                                             /$$$$$$ /$$   /$$ /$$$$$$$$ /$$$$$$ 
 /$$__  $$                      | $$                                                            |_  $$_/| $$$ | $$| $$_____//$$__  $$
| $$  \__/ /$$   /$$  /$$$$$$$ /$$$$$$    /$$$$$$  /$$$$$$/$$$$                                   | $$  | $$$$| $$| $$     | $$  \ $$
|  $$$$$$ | $$  | $$ /$$_____/|_  $$_/   /$$__  $$| $$_  $$_  $$             /$$$$$$              | $$  | $$ $$ $$| $$$$$  | $$  | $$
 \____  $$| $$  | $$|  $$$$$$   | $$    | $$$$$$$$| $$ \ $$ \ $$            |______/              | $$  | $$  $$$$| $$__/  | $$  | $$
 /$$  \ $$| $$  | $$ \____  $$  | $$ /$$| $$_____/| $$ | $$ | $$                                  | $$  | $$\  $$$| $$     | $$  | $$
|  $$$$$$/|  $$$$$$$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$ | $$ | $$                                 /$$$$$$| $$ \  $$| $$     |  $$$$$$/
 \______/  \____  $$|_______/    \___/   \_______/|__/ |__/ |__/                                |______/|__/  \__/|__/      \______/ 
           /$$  | $$                                                                                                                 
          |  $$$$$$/                                                                                                                 
           \______/ 
"""
print()
print(Colorate.Vertical(Colors.white_to_black, Center.XCenter(art)))
portM()
