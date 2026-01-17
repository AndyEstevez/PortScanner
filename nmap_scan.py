import nmap
from colorama import Fore, Style

nm = nmap.PortScanner()

print(Fore.RED + "*"*85)
print("WARNING: PORT SCANNING MAY VIOLATE ACCEPTABLE USE POLICIES ON NETWORKS YOU DON'T OWN")
print("USE ONLY ON NETWORKS YOU HAVE EXPLICIT PERMISSION TO SCAN")
print("*"*85+ Style.RESET_ALL)

IP = input("Enter IP to scan: ")
ports = input("Select option to scan ports: \n1 - Top Ports \n2 - 1 to 1024 (COMMON PORTS) \n3 - 1 to 65535 (FULL SCAN)\n")
if int(ports) == 1:
    options = f"-oG - -v --top-ports 30 scan_results"
elif int(ports) == 2: 
    options = f"-sV -sC -p1-1024 scan_results"
elif int(ports) == 3:
    options = f"-sV -sC -p1-65535 scan_results"
else:
    options = f"-sV -sC -p1-200 scan_results"

nm.scan(IP, arguments=options)

for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    for protocol in nm[host].all_protocols():
        print("Protocol: %s" % protocol)
        ports = nm[host][protocol]
        print("-"*50)
        print(f"Listed ports on {IP}")
        for port, state in ports.items():
            if state['state'] == 'open':
                print("Port: %s\tStatus: %-20s\tService: %-10s" % (port, Fore.GREEN + state['state'] + Style.RESET_ALL, state['name']))
            else:
                print("Port: %s\tStatus: %-20s\tService: %-10s" % (port, Fore.RED + state['state'] + Style.RESET_ALL, state['name']))