import nmap
from colorama import Fore, Style

nm = nmap.PortScanner()

print("Enter IP to scan:")
IP = input()
print("Scan ports 1 to X:")
ports = input()
options = f"-sV -sC -p1-{ports} scan_results"

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
                print("Port: %s\tStatus: %-20s\tService: %-10s\tProduct: %s" % (port, Fore.GREEN + state['state'] + Style.RESET_ALL, state['name'], state['product']))
            else:
                print("Port: %s\tStatus: %-20s\tService: %-10s\tProduct: %s" % (port, Fore.YELLOW + state['state'] + Style.RESET_ALL, state['name'], state['product']))