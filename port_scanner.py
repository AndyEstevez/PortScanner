import socket
import asyncio
import sys
from colorama import Fore, Style
import ipaddress
import threading
from concurrent.futures import ThreadPoolExecutor

top_ports_dict = {
    21: "ftp",
    22: "ssh",
    23: "telnet",
    25: "smtp",
    53: "dns",
    80: "http",
    110: "pop3",
    123: "ntp",
    135: "msrpc",
    139: "netbios-ssn",
    143: "imap",
    161: "snmp",
    443: "https",
    445: "microsoft-ds",
    993: "imaps",
    995: "pop3s",
    3306: "mysql",
    3389: "ms-wbt-server"
}

def port_scan(IP, starting_port, ending_port, task):
    try:
        for port in range(starting_port, ending_port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)
            result = s.connect_ex((IP, port))
            if result == 0: 
                print(Fore.GREEN + f"{port}\t", f"open\t", f"{socket.getservbyport(port)}" + Style.RESET_ALL)
            elif top_ports_dict.get(port):
                    print(Fore.RED + f"{port}\t", f"closed\t", f"{socket.getservbyport(port)}" + Style.RESET_ALL)
          
            s.close()

    except KeyboardInterrupt:
        print("\n Exiting")
        sys.exit()
    except socket.error:
        print("\n Server not responding")
        sys.exit()


def main():
    print(Fore.RED + "*"*85)
    print("WARNING: PORT SCANNING MAY VIOLATE ACCEPTABLE USE POLICIES ON NETWORKS YOU DON'T OWN")
    print("USE ONLY ON NETWORKS YOU HAVE EXPLICIT PERMISSION TO SCAN")
    print("*"*85+ Style.RESET_ALL)
    print("PORT SCANNER WILL SCAN FROM 1 to 1024")
    while True:
        try:
            print("Enter IP to scan ports:")
            IP = input()
            print(ipaddress.ip_address(IP))
            break

        except ValueError:
            print("NOT VALID IP ADDRESS. Example - 127.0.0.1")

    print("Enter IP to scan ports:")
    IP = input()
    print(f"IP Address: {IP}")
    print("Port\t Status\t Service")
    # ASYNC CONCURRENT
    # await task1 = asyncio.create_task(port_scan(IP, starting_port=1, ending_port=50, task=1))
    # await task2 = asyncio.create_task(port_scan(IP, starting_port=51, ending_port=100, task=2))

    # async with asyncio.TaskGroup() as task_group:
    #     task_group.create_task(port_scan(IP, starting_port=1, ending_port=100, task=1))
    #     task_group.create_task(port_scan(IP, starting_port=101, ending_port=200, task=2))
    #     task_group.create_task(port_scan(IP, starting_port=201, ending_port=300, task=3))

# asyncio.run(main())


    # THREADING
    # t1 = threading.Thread(target=port_scan(IP, starting_port=1, ending_port=50, task=1))
    # t2 = threading.Thread(target=port_scan(IP, starting_port=51, ending_port=100, task=2))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    # THREAD POOL
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(port_scan, IP, 1, 300, 1)
        executor.submit(port_scan, IP, 301, 600, 2)
        executor.submit(port_scan, IP, 601, 1024, 3)

if __name__ == "__main__":
    main()