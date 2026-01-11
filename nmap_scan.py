import nmap

nm = nmap.PortScanner()


print("Enter IP to scan:")
IP = input()
print("Scan ports 1 to X:")
ports = input()
options = f"-sS -sV -p1-{ports} -sC scan_results"

nm.scan(IP, arguments=options)

for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    for protocol in nm[host].all_protocols():
        print("Protocol: %s" % protocol)
        ports = nm[host][protocol]
        print("-"*50)
        print(f"Open ports on the {IP}")
        for port, state in ports.items():
            print("Port: %s\tService: %s" % (port, state['name']))

