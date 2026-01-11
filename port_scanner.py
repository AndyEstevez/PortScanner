import socket
import asyncio
import sys

import threading
from concurrent.futures import ThreadPoolExecutor


def port_scan(IP, starting_port, ending_port, task):
    print("TASK #", task, " STARTING")
    try:
        for port in range(starting_port, ending_port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)

            result = s.connect_ex((IP, port))
            if result ==0: 
                print(f"Port {port} is open -", f"Service running: {socket.getservbyport(port)}")
            s.close()

    except KeyboardInterrupt:
        print("\n Exiting")
        sys.exit()
    except socket.error:
        print("\n Server not responding")
        sys.exit()


def main():
    print("*" * 50)
    print("PORT SCANNER WILL SCAN FROM 1 to 1024")
    print("Enter IP to scan ports:")
    IP = input()
    print(f"IP Address: {IP}")

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